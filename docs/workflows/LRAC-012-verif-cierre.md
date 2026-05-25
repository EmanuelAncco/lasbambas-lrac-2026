---
id: LRAC-012
modulo: M1.A
nombre: Verificación visual de cierre (auditoría de segundo nivel)
brecha: Auditoría CCV humana 5% muestreo · ICMM 2024 reporta confiabilidad real 42%
stack: FastAPI + YOLOv8 + ViT crack detection + Gemini Vision + n8n
metrica: 5% muestra mensual auditada por IA · score auditoría ≥85
acciones: [A-05]
pilar: R
estado: diseno (componentes existentes)
---

# LRAC-012 · Verificación visual de cierre (auditoría de segundo nivel)

## Brecha que ataca

La auditoría de CCV en Las Bambas se hace típicamente por **muestreo del 5 % por equipo interno**. Esto deja el 95 % de los controles dependiendo de la confiabilidad declarada. Cuando ICMM (2024) reporta que **83 % de las fatalidades del año se vincularon a fallas en controles críticos** (a pesar de pasar verificaciones documentadas), el mensaje es claro: la verificación de primer nivel no es suficiente.

LRAC-012 es la **verificación de la verificación**: cada mes, una muestra estadísticamente representativa de cierres es re-auditada por IA, no por humano. Genera reporte de discrepancias para auditoría externa.

## Stack técnico

- **YOLOv8** (cuando el RACS original era EPP).
- **ViT crack detection** (Vision Transformer entrenado en grietas estructurales).
- **Gemini Vision Pro** (casos generalistas: derrame limpiado, señalética instalada, objeto removido).
- **n8n** orquesta el muestreo aleatorio mensual y la generación del reporte.
- **Postgres** + **pgvector** para búsqueda semántica de RACS similares.

## Flujo del workflow

```
Primer día hábil del mes
1. n8n cron dispara
2. Postgres SELECT con muestreo aleatorio:
   - 5 % de CCV cerrados el mes anterior
   - estratificado por VP y por fatal-risk relacionado
3. Para cada cierre seleccionado:
   - Recuperar foto original + foto de cierre + clasificación
   - Enviar a la cadena de modelos (YOLO / ViT / Gemini Vision)
   - Calcular score de coincidencia "esperado vs observado"
4. Generar reporte de discrepancias:
   - Cierres aprobados por IA (~90 % esperado)
   - Cierres marcados como "duda" (~5–8 %): requieren revisión humana
   - Cierres rechazados (~2–5 %): se reabren automáticamente + se notifica al supervisor original
5. Reporte se envía a:
   - Auditoría Interna (revisión)
   - Auditor Externo (cada trimestre)
6. Dashboard publica las métricas mensuales: % aprobados, % dudas, % rechazados, por VP
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| Confiabilidad real CCV (post-auditoría) | 42 % (benchmark ICMM) | 60 % | 80 % |
| % de la muestra auditada por IA | 0 % | 5 % | 10 % |
| % reabiertos post-auditoría | n/d | medir | tendencia ↓ |
| Score auditoría externa anual | n/d | ≥75 | ≥85 |

## Estado actual y dependencias

- **Estado:** **diseño** (componentes de IA existen en producción individualmente; integración nueva).
- **Dependencias:**
  - LRAC-003 ya operativo (porque eso es la fuente de los cierres a auditar).
  - Set de calibración de 200–500 fotos antes/después reales.
  - Acuerdo con Auditoría Interna sobre umbrales de confiabilidad.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| IA produce muchos "dudas" que saturan revisión humana | Threshold tuning + UI cómoda para revisión |
| Sesgo del modelo hacia ciertas clases | Re-entrenamiento trimestral con casos revisados manualmente |
| Auditor externo desconfía de IA | Transparencia: explicabilidad (Grad-CAM, attention maps) + auditoría humana paralela los primeros 90 días |

## Referencias

- Selleck, R., Hassall, M. E., Cattani, M. (2022). *Determining the reliability of critical controls in mining.* Safety, 8(3), 64.
- ICMM (2024). *Benchmarking 2024 Safety Data.* — 42 fatalidades vs 36 en 2023.
- isoMetrix (2024). *Managing What Matters Most: CCM & Verification.*
