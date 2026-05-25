---
id: LRAC-002
modulo: M1.B
nombre: Captura de voz a RACS estructurado
brecha: Operadores en altura / con guantes / EPP no pueden escribir
stack: Evolution API + Whisper o Gemini Multimodal + n8n + Postgres
metrica: Captura RACS en <90 s desde inicio del reporte
acciones: [A-02, A-11]
pilar: L · R
estado: produccion
---

# LRAC-002 · Captura de voz a RACS estructurado

## Brecha que ataca

En obra real, **escribir un RACS con guantes, casco bajo el sol o desde altura es inviable**. El subreporte no se debe siempre a falta de cultura; muchas veces es fricción operativa pura. La voz es el canal natural en campo.

## Stack técnico

- **WhatsApp Business + Evolution API** (recibe nota de voz como audio OGG).
- **Whisper-large-v3** (transcripción local en VPS) o **Gemini Multimodal** (transcripción + estructuración en una sola llamada).
- **n8n** orquesta: descarga audio → STT → Gemini estructura → confirma con el operador.
- **Postgres** con embedding del texto resultante.

## Flujo del workflow

```
1. Operador envía nota de voz al bot (5–60 s)
2. n8n descarga el OGG, lo pasa a Whisper o Gemini Multimodal
3. Gemini Pro estructura el RACS con el mismo schema de LRAC-001
4. Bot envía resumen estructurado al operador:
   "¿Confirmas?
    - Tipo: Condición subestándar
    - Severidad: Alta
    - Riesgo fatal asociado: Equipo móvil
    - Descripción: 'Faja transportadora con guarda suelta en zona molienda 2'"
5. Operador responde "sí" o corrige
6. Workflow guarda + notifica supervisor (igual que LRAC-001)
```

## KPIs y métricas

| KPI | Meta |
|---|---|
| Tiempo medio de captura por voz | 60 s |
| % reportes vía voz vs texto | 35 % H1 → 55 % H3 |
| Tasa de corrección por el operador | <15 % |
| WER (Word Error Rate) del STT en español andino | <8 % |

## Estado actual y dependencias

- **Estado:** **producción** (TOKI v3.0 ya procesa audio para otros dominios).
- **Dependencia crítica:** entrenamiento/fine-tuning de Whisper con audios reales de la mina si el español andino + ruido de planta degrada el WER (probable con vocabulario minero específico).

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Ruido ambiental degrada STT | Modelo voice-activity-detection + filtro previo |
| Costo de Gemini Multimodal alto | Cachear con Flash-Lite + escalar a Pro solo cuando confidence < umbral |
| Audios largos (>2 min) | Truncado a 90 s + segmentación |

## Referencias

- Salas et al. (2024). *Mindfulness-based program with virtual reality to increase safe behaviors in mining workers.* PMC11949912.
- Whisper paper (OpenAI, 2022).
