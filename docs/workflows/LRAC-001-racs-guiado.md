---
id: LRAC-001
modulo: M1.B
nombre: RACS guiado conversacional
brecha: Calidad del reporte preventivo (55%), FTO PLANTA 45%
stack: WhatsApp Business + Evolution API + n8n + Gemini Pro + Postgres pgvector
metrica: ≥2 reportes/trabajador/mes con foto+GPS ≥90%
acciones: [A-02, A-11]
pilar: L · R
estado: produccion
---

# LRAC-001 · RACS guiado conversacional

## Brecha que ataca

El instructivo del caso indica que la calidad de los reportes RACS (Reporte de Actos y Condiciones Subestándar) de Mina Juanita está en **55 %**. El análisis del Excel revela que la gerencia **PLANTA tiene FTO de 45 %** en enero 2026 (la peor del set) y **MEDIO AMBIENTE tiene 3Q de 39 %**. La fricción de los formatos en papel y la falta de guía estructurada producen reportes genéricos, sin foto, sin GPS, sin contexto y **subreporte sistémico** por miedo, vergüenza o tiempo (Reason, 1997).

## Stack técnico

- **WhatsApp Business** vía Evolution API self-hosted (canal universal en Perú minero).
- **n8n** self-hosted con un workflow de 50+ nodos (orquestación, branching por tipo de mensaje, retries).
- **Gemini Pro** como modelo principal (clasificación + extracción estructurada) + **Gemini Flash-Lite** para preview rápido.
- **Postgres** con extensión **pgvector** para embeddings y búsqueda semántica de reportes similares.
- Identidad del reportador resuelta por **número de teléfono** (alta previa por RR.HH.).

## Flujo del workflow

```
1. Trigger: el trabajador envía "RACS" al bot
2. Bot responde: "¡Vamos a reportar! Envíame primero una foto"
3. Operador → foto (multimedia handler n8n)
4. Bot extrae EXIF GPS si existe; si no, pide ubicación en vivo
5. Bot: "Descríbeme lo que viste (texto o nota de voz)"
6. Si voz → Whisper / Gemini Multimodal transcribe
7. Gemini Pro clasifica:
   - tipo: acto sub-estándar / condición sub-estándar / cuasi-accidente
   - severidad: leve / moderada / alta / inminente
   - fatal-risk relacionado: 1 de los 12 corporativos
   - 13 Reglas para la Vida: ¿incumple alguna?
8. Workflow guarda en Postgres con embedding
9. n8n hace push a IEM corporativo (REST API o webhook)
10. Bot confirma al operador: "RACS #2026-04823 creado. Tu supervisor lo recibirá ahora."
11. Bot notifica al supervisor con foto + clasificación + link al ticket
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| Reportes / trabajador / mes | 0.4 (estimado) | 1.5 | 2.5 |
| Reportes con foto + GPS | <30 % | 80 % | 95 % |
| Tiempo medio de captura | n/d | 90 s | 60 s |
| Reportes rechazados por calidad | n/d | <5 % | <2 % |

## Estado actual y dependencias

- **Estado:** **producción** sobre la plataforma Aecodito v3.0 (50 nodos n8n, 10 herramientas externas integradas). Adaptación al dominio LRAC implica reentrenar el clasificador Gemini con un set inicial de ~200 RACS reales etiquetados.
- **Dependencias:**
  - WhatsApp Business + Evolution API operativos.
  - VPS Gen+ (187.77.250.111) ya tiene n8n self-hosted (GEN+ FLOWS).
  - API a IEM corporativo MMG (a coordinar con CTO MMG; fallback a CSV nocturno).
- **Tiempo de despliegue piloto:** 2 semanas con 50 trabajadores piloto.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Conectividad 4G inestable en mina | Buffering local + sync diferido cuando vuelve la señal |
| Privacidad biométrica (Ley 29733) | Anonimización del reportador en publicaciones; consentimiento informado |
| Saturación del bot ante avalancha de reportes | Rate limiting + horarios pico anticipados |
| Mal uso (reportes falsos para ganar puntos) | Triangulación foto+GPS+timestamp; auditoría de muestreo |

## Referencias

- DS 024-2016-EM, Art. 7 (Reporte de Actos y Condiciones Subestándar).
- Buenaventura. *P-COR-09.02 Procedimiento RACS.*
- Tong et al. (2019). *Critical safety behaviors targeted intervention.* IJERPH.
- Reason, J. (1997). *Managing the Risks of Organizational Accidents.* Ashgate.
