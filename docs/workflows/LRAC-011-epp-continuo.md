---
id: LRAC-011
modulo: M1.A
nombre: Detección EPP continua en obra
brecha: CCV humano por checklist · cobertura limitada
stack: Cámaras Tapo/Reolink + FastAPI + YOLOv8 + n8n + WhatsApp
metrica: Cobertura EPP en obra ≥97% · alerta <30 s
acciones: [A-05, A-12]
pilar: R
estado: produccion
---

# LRAC-011 · Detección EPP continua en obra

## Brecha que ataca

Las verificaciones de Controles Críticos (CCV) en Las Bambas se realizan hoy por checklist humano. Selleck, Hassall y Cattani (2022, *Safety*) auditaron 10 años de incidentes mineros y demostraron que **la confiabilidad real de los controles críticos es solo 42 %**, aún cuando los CCV documentados pasan las verificaciones. La pieza faltante es **verificación continua y automatizada**, no más verificaciones humanas.

## Stack técnico

- **Cámaras IP** en zonas críticas: Tapo C320WS (interior, accesible) y Reolink Argus PT Ultra (exterior, energía solar).
- **FastAPI inference server** corriendo en VPS Gen+ (puerto 8088) con modelos cargados en memoria.
- **YOLOv8** sobre frames cada 5 s para no saturar GPU.
- **n8n** consume el endpoint, evalúa severidad, decide canal de notificación.
- **Postgres** archiva detecciones con foto blureada.

## Flujo del workflow

```
1. Cámara IP transmite RTSP continuamente
2. Worker Python extrae 1 frame cada 5 s
3. POST a FastAPI /infer/epp con el frame
4. YOLOv8 devuelve: detections = [{class, confidence, bbox}]
5. Lógica de decisión:
   - Si detecta persona sin casco/chaleco con confidence > 0.65
     + persona se queda >30 s en la zona (no es un transeúnte)
     → ALERTA
6. n8n recibe el evento y:
   - Identifica al supervisor del área (por geolocalización de la cámara)
   - Envía WhatsApp con foto blureada (rostro pixelado) + clase faltante + ubicación
   - Crea ticket auto en IEM
   - Si la persona se identifica visualmente (uniforme, número), tracking del incidente
7. Supervisor responde "atendido" → cierra el flujo
8. Detección queda en Postgres para reportes ejecutivos semanales
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| Cobertura EPP en obra (medida continua) | n/d | 95 % | 99 % |
| Tiempo detección → notificación supervisor | n/d | <30 s | <15 s |
| Falsos positivos en producción | n/d | <5 % | <2 % |
| Cámaras activas | 8 inicial | 16 | 24+ |

## Estado actual y dependencias

- **Estado:** **producción** en Vision Pro PDK (VPS Gen+ puerto 8088, login `vision-pro-2026`).
- **Métricas reales:** 87.67 % mAP@0.5 sobre 14 055 imágenes peruanas, 38 FPS sostenidos en Jetson Orin Nano Super.
- **Dependencias:** cámaras instaladas con buena vista al área crítica, red Ethernet o 4G, plan de migración YOLOv8 → RF-DETR.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Falsos positivos saturan al supervisor | Throttle: máx 1 alerta/persona/15 min + agregación por área |
| Cámara fuera de servicio sin alerta | Heartbeat cada 60 s + dashboard de salud de cámaras |
| Privacidad (rostros visibles) | Blureado automático en cualquier foto enviada |

## Referencias

- Selleck, R., Hassall, M. E., Cattani, M. (2022). *Determining the reliability of critical controls in mining.* Safety, 8(3), 64.
- Huang & Huang (2026). *CGALS-YOLO.* Sensors, 26(5), 1646.
- ICMM (2024). *Benchmarking 2024 Safety Data.* — Dato crítico: 83 % de fatalidades 2024 vinculadas a fallas en controles críticos.
