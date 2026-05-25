# Workflows n8n exportables · GAIATECH M1.0

> JSON skeletons listos para importar en n8n self-hosted v1.50+.
>
> Cada archivo contiene la **estructura arquitectónica completa** de un workflow con: nodos, conexiones, queries SQL, prompts Gemini, llamadas HTTP, lógica de routing y respuesta. Las credenciales y las URLs están parametrizadas vía `$env.*` o `REPLACE_*` para que no haya secretos quemados.

## Workflows incluidos

| Archivo | Workflow | Módulo | Nodos | Pilares LRAC |
|---|---|---|---|---|
| `LRAC-001-racs-guiado.json` | RACS guiado conversacional vía WhatsApp | M1.B | 13 | L · R |
| `LRAC-003-cierre-bucle.json` | Cierre de bucle con verificación IA (YOLO + ViT + Gemini Vision) | M1.B + M1.A | 14 | R |
| `LRAC-004-capsula-quiz.json` | Cápsula semanal multimedia + quiz adaptativo | M1.B | 12 | A · C |
| `LRAC-031-reporte-gemini.json` | Reporte ejecutivo semanal Gemini Pro a VPs | M1.D | 8 | L · A |

## Cómo importar

### En n8n self-hosted

1. Abrir `https://flows.tu-vps.nip.io` (o tu dominio n8n).
2. Workflows → Import from File → seleccionar el `.json`.
3. n8n detecta credenciales faltantes y marca los nodos correspondientes.
4. Configurar credenciales en `Settings → Credentials`:
   - `lrac-pgvector` (Postgres)
   - `evolution-api` (HTTP Header Auth con el token)
   - `gemini-api` (la API key va vía variable de entorno `GEMINI_API_KEY`)
   - `gmail-oauth` (OAuth Google Workspace)
   - `gdrive-oauth` (OAuth Google Workspace)
5. Antes de activar, revisar variables de entorno:
   ```
   GEMINI_API_KEY=AIzaSy...
   EVOLUTION_URL=https://evolution.tu-vps.nip.io
   EVOLUTION_INSTANCE=lrac-bot
   IEM_API_URL=https://iem.mmg.internal
   FASTAPI_INFER_URL=http://vision-pro:8088
   VIDEO_GEN_URL=http://davinci-mcp:8090
   PDFKIT_URL=http://pdfkit:3000
   GDRIVE_REPORTES_SHE=<folder_id>
   VP_SHE_EMAIL=vp.she@mmg.com
   VP_OPS_EMAIL=vp.ops@mmg.com
   VP_PROY_EMAIL=vp.proy@mmg.com
   VP_SUPPLY_EMAIL=vp.supply@mmg.com
   ```
6. Activar el workflow desde el toggle de la esquina superior derecha.

### Esquema de Postgres requerido

Los workflows asumen el siguiente schema mínimo en `lrac` (Postgres con extensión `pgvector`):

```sql
CREATE EXTENSION IF NOT EXISTS vector;

-- Sesiones conversacionales del bot
CREATE TABLE lrac_sesiones (
  telefono TEXT PRIMARY KEY,
  estado TEXT NOT NULL,
  payload JSONB NOT NULL DEFAULT '{}',
  vigente BOOLEAN NOT NULL DEFAULT true,
  actualizado TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- Registros RACS
CREATE TABLE lrac_racs (
  id SERIAL PRIMARY KEY,
  telefono TEXT NOT NULL,
  vp TEXT, gerencia TEXT,
  tipo TEXT, severidad TEXT, fatal_risk TEXT, regla_vida INT,
  descripcion TEXT,
  gps JSONB, foto_url TEXT,
  payload_ia JSONB,
  embedding vector(768),
  ticket_iem TEXT,
  estado TEXT DEFAULT 'ABIERTO',
  confidence_cierre REAL,
  observacion_ia TEXT,
  creado TIMESTAMPTZ DEFAULT NOW(),
  cerrado TIMESTAMPTZ,
  reabierto TIMESTAMPTZ
);
CREATE INDEX ON lrac_racs USING ivfflat (embedding vector_cosine_ops);

-- Trabajadores
CREATE TABLE lrac_trabajadores (
  telefono TEXT PRIMARY KEY,
  nombre TEXT,
  vp TEXT, gerencia TEXT,
  activo BOOLEAN DEFAULT true,
  consentimiento BOOLEAN DEFAULT false,
  contratista TEXT,
  alta TIMESTAMPTZ DEFAULT NOW()
);

-- Temas de cápsulas semanales
CREATE TABLE lrac_temas (
  id SERIAL PRIMARY KEY,
  titulo TEXT, contenido_md TEXT,
  regla_vida INT, prioridad INT DEFAULT 5,
  ultima_emision TIMESTAMPTZ
);

-- Logs de envío
CREATE TABLE lrac_envios_capsula (
  id SERIAL PRIMARY KEY,
  telefono TEXT, gerencia TEXT, vp TEXT,
  tema_id INT, video_url TEXT, quiz_id TEXT,
  enviado TIMESTAMPTZ DEFAULT NOW(),
  visto_at TIMESTAMPTZ,
  quiz_score INT
);

-- Métricas para el reporte ejecutivo
CREATE TABLE lrac_metricas_diarias (
  fecha DATE PRIMARY KEY, lrac_4p REAL, fto REAL, q3 REAL, ccv REAL, acc REAL, nmap REAL, vea_p1 REAL, desempenho REAL
);

CREATE TABLE lrac_metricas_semanal (
  semana_inicio DATE, vp TEXT, gerencia TEXT, lrac_4p REAL,
  PRIMARY KEY (semana_inicio, vp, gerencia)
);

CREATE TABLE lrac_reportes_ejecutivos (
  id SERIAL PRIMARY KEY, fecha DATE, semana TEXT, markdown TEXT, pdf_drive_id TEXT, destinatarios TEXT
);

-- Alertas generadas por IA
CREATE TABLE lrac_ia_alertas (
  id SERIAL PRIMARY KEY,
  racs_id INT REFERENCES lrac_racs(id),
  motivo TEXT, confidence REAL,
  creado TIMESTAMPTZ DEFAULT NOW()
);

-- Detecciones EPP (workflow LRAC-011 no incluido en este lote)
CREATE TABLE lrac_detecciones (
  id SERIAL PRIMARY KEY,
  camara TEXT, gerencia TEXT,
  clase TEXT, confidence REAL, foto_blureada_url TEXT,
  timestamp TIMESTAMPTZ DEFAULT NOW()
);
```

## Diagrama de dependencias entre workflows

```
LRAC-001 (captura RACS)
   └── escribe en lrac_racs
        └── LRAC-003 (cierre con IA visual)
              └── escribe estado_cerrado/reabierto
                    └── LRAC-031 (reporte semanal Gemini)
                          └── lee agregados últimos 7 días

LRAC-004 (cápsula + quiz)
   ├── lee lrac_trabajadores
   ├── escribe lrac_envios_capsula
   └── (corre en paralelo, cron lunes 7:00)

LRAC-031 (reporte ejecutivo)
   ├── lee lrac_racs, lrac_detecciones, lrac_metricas_*
   ├── llama Gemini Pro
   └── envía Gmail + archiva Drive
```

## Workflows no incluidos en este lote (skeletons disponibles bajo demanda)

- `LRAC-002` (captura voz · refactor del LRAC-001 con Whisper)
- `LRAC-010` (detección EPP en accesos · ConstEdge integration)
- `LRAC-011` (detección EPP continua · cámaras IP loop)
- `LRAC-012` (auditoría 2do nivel CCV · muestreo aleatorio mensual)
- `LRAC-020` (vibración relaves · MQTT + LSTM-AE inference)
- `LRAC-021` (geofence 6-4-2 · PWA + GPS daily aggregation)
- `LRAC-030` (dashboard SHE · queries de Next.js, no n8n)
- `LRAC-032` (cumplimiento OSINERGMIN · PDF + firma digital + RPA VVO)

Los 4 incluidos son los más representativos arquitectónicamente (uno por módulo M1.A/B/C/D + un cron + un agentic + un end-to-end). El resto sigue los mismos patrones.

## Notas técnicas

- **Versionado n8n:** los JSON usan `typeVersion` actuales al 2026-05. Si tu instancia es más antigua, n8n te avisará al importar y sugerirá migración automática.
- **Credenciales:** los `credentials.id = REPLACE_PG_LRAC` y similares son placeholders. Reemplazar por los IDs reales de tu instancia o usar el wizard de n8n.
- **Postgres pgvector:** la tabla `lrac_racs` incluye columna `embedding vector(768)` que requiere extensión `pgvector` instalada en el cluster Postgres.
- **Idempotencia:** los workflows asumen Postgres como fuente única de verdad. Si se reintenta, la `ON CONFLICT` de `lrac_sesiones` y el `UPSERT` aseguran consistencia.
- **Observabilidad:** todos los workflows escriben en tablas de log + el panel n8n nativo muestra ejecuciones.

## Cómo correr el bot Aecodito Minero en un VPS limpio

```bash
# 1) Docker compose con n8n + Postgres + Evolution API
docker compose up -d n8n postgres evolution

# 2) Cargar schema
psql -h postgres -U lrac < n8n-workflows/schema.sql

# 3) Importar workflows
for f in n8n-workflows/*.json; do
  n8n import:workflow --input="$f"
done

# 4) Set env vars
export GEMINI_API_KEY=...
export EVOLUTION_URL=...
# ... (resto del .env)

# 5) Activar
n8n update:workflow --active=true --id=<workflow_id>
```

El tiempo de despliegue piloto en un VPS limpio es ~3 horas con docker compose.
