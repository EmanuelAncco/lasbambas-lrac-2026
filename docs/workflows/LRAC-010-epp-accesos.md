---
id: LRAC-010
modulo: M1.A
nombre: Detección EPP en accesos (garita)
brecha: Cumplimiento de Reglas para la Vida en el punto de ingreso · 100% trabajadores
stack: ConstEdge (DeepFace + YOLOv8) + Jetson Orin Nano Super + n8n + Postgres
metrica: EPP ≥99% en acceso · alerta <30 s · 38 FPS sostenidos
acciones: [A-12]
pilar: L · R
estado: produccion
---

# LRAC-010 · Detección EPP en accesos

## Brecha que ataca

Cada trabajador debe ingresar a la operación con su EPP completo según su rol. La verificación visual humana en la garita es **inconsistente, sensible a fatiga del guardia y no auditable**. En operaciones de 4 500 trabajadores con turnos rotativos, este es un punto natural de control crítico que debe convertirse en métrica continua y auditable.

## Stack técnico

- **ConstEdge** (sistema construido por el autor): combina **DeepFace** (identificación facial) + **YOLOv8** (11 clases EPP).
- **Jetson Orin Nano Super** (entorno provisionado 2026-05-13 con `torch+cuSPARSELt+torchvision` compiled).
- **Cámara IP** en la garita (Tapo C320WS o equivalente).
- **n8n** orquesta: detección → notificación → registro.
- **Postgres** para audit log + base biométrica con consentimiento.

## Flujo del workflow

```
1. Trabajador se acerca al torniquete
2. Cámara captura frame (1 cada 200 ms)
3. DeepFace identifica al trabajador (vs base biométrica con consentimiento)
4. YOLOv8 analiza el mismo frame y detecta clases EPP:
   - casco, gafas, chaleco reflectante, barbijo, guantes, botas, arnés (si aplica),
     audífonos, mascarilla, careta soldador, protección facial completa
5. Sistema valida EPP requerido según rol del trabajador
6. Decisión:
   - Si EPP completo → torniquete abre + log verde
   - Si falta EPP → torniquete bloqueado + sonido + mensaje en pantalla
                    + bot envía mensaje al trabajador con detalle del faltante
                    + supervisor del área es notificado en <30 s
7. Reintento: trabajador corrige + vuelve a presentarse
8. Todo el evento queda en Postgres con foto + frame + timestamp + decisión
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| Cobertura EPP en acceso | <80 % (estimado) | 99 % | 99.9 % |
| FPS sostenidos | 38 FPS (medido) | mantener | mantener |
| Latencia identificación → decisión | <800 ms | <500 ms | <300 ms |
| Falsos positivos (bloqueo erróneo) | n/d | <1 % | <0.5 % |
| % accesos con foto auditable | 0 % | 100 % | 100 % |

## Estado actual y dependencias

- **Estado:** **producción** en Vision Pro PDK (VPS Gen+ + Jetson Orin Nano Super).
- **Métricas reales medidas:** 87.67 % mAP@0.5 sobre dataset peruano de 14 055 imágenes, 38 FPS sostenidos.
- **Dependencias:**
  - Base biométrica de trabajadores con consentimiento (Ley 29733).
  - Cámara IP + cableado garita.
  - Licencia YOLOv8 AGPL-3.0 → **plan: migrar a RF-DETR o YOLOX (Apache 2.0)** antes del piloto Las Bambas.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| AGPL de YOLOv8 contamina código corporativo | Migración a RF-DETR / YOLOX (Apache 2.0) en H1 |
| Privacidad biométrica (Ley 29733) | Consentimiento informado + DPO designado + retención limitada |
| Iluminación variable madrugada/atardecer | Modelo entrenado con augmentation lumínica + cámara con IR |
| Cambio de EPP requerido por área | Configuración por rol y zona, no globalizada |

## Referencias

- Huang & Huang (2026). *CGALS-YOLO: Vision-Based Sensing for Protective Equipment Wearing Compliance Detection in Underground Environments.* Sensors, 26(5), 1646. — Estado del arte: mAP@0.5 = 89.4 % con CGALS-YOLO (mejora 4.6 % vs YOLOv8 baseline).
- Costin, A. M., Wehle, A., Adibfar, A. (2019). *Leading indicators — A conceptual IoT-based framework.* Safety, 5(4), 86.
