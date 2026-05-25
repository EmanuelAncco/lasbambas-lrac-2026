---
id: LRAC-003
modulo: M1.B
nombre: Cierre de bucle con verificación IA
brecha: ACC en PROYECTOS 61.12% · acciones marcadas cerradas sin verificación real
stack: n8n + YOLOv8 + Gemini Vision + Postgres + WhatsApp
metrica: ≥95% cierres con foto validada por IA
acciones: [A-04, A-11]
pilar: R
estado: produccion (componentes existentes; integracion pendiente)
---

# LRAC-003 · Cierre de bucle con verificación IA

## Brecha que ataca

Del análisis del Excel: **ACC en PROYECTOS está en 61.12 %** con valle de 50.00 % en marzo 2026. ACC = Acciones Correctivas Cerradas: refleja la disciplina con la que la organización **cierra el bucle entre identificación y rectificación**. Un 39 % de acciones quedan abiertas mes a mes. Esto es el caldo de cultivo para "normalización de la desviación" (Vaughan, 1996) y para eventos de alto potencial.

El problema típico: el supervisor marca el RACS como "cerrado" sin verificación física, simplemente para cumplir el indicador. **La IA visual cierra ese flanco.**

## Stack técnico

- **YOLOv8** para verificación EPP (87.67 % mAP) cuando aplica.
- **ViT crack detection** (Vision Transformer entrenado en grietas) cuando la condición original era estructural.
- **Gemini Vision Pro** como modelo generalista para casos no cubiertos (objeto removido, derrame limpiado, señalética instalada).
- **n8n** orquesta: pide foto → enruta al modelo adecuado según el tipo de RACS original → decide si aprueba o reabre.

## Flujo del workflow

```
1. Supervisor abre el RACS #2026-04823 en el bot y escribe "cerrar"
2. Bot: "Envíame la foto de evidencia"
3. n8n descarga la foto + recupera el RACS original de Postgres
4. Router por tipo:
   - Si RACS era "falta EPP" → YOLOv8 valida que la persona tiene EPP completo
   - Si era "grieta" → ViT clasifica: reparada / atenuada / persiste
   - Si era genérico → Gemini Vision compara foto antes/después
5. IA devuelve {aprobado: bool, confidence: float, observacion: str}
6. Si aprobado y confidence >= 0.75:
   - RACS marcado "Cerrado verificado"
   - Bot agradece al supervisor + felicita al reportador original
7. Si rechazado o confidence < 0.75:
   - RACS reabierto con observación de la IA
   - Bot notifica al supervisor: "Necesito otra foto. La IA observa que [...]"
8. Toda decisión queda auditada en Postgres con la foto + score
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| ACC corporativo | 70.4 % | 78 % | 85 % |
| ACC en PROYECTOS (gerencia peor) | 61.12 % | 70 % | 80 % |
| % cierres verificados por IA | 0 % | 70 % | 95 % |
| Tasa de reapertura post IA | n/d | <15 % | <8 % |

## Estado actual y dependencias

- **Estado:** los componentes (YOLOv8, ViT, Gemini Vision) están en producción separados. La **integración como un workflow de cierre** es nueva — estimo 1 semana de implementación.
- **Dependencias:**
  - Workflow LRAC-001 operativo (para tener RACS estructurados con tipo).
  - Threshold tunning con un set de 100–200 fotos antes/después reales.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Falsos positivos (IA aprueba un cierre malo) | Auditoría aleatoria 5 % por humanos durante los primeros 90 días |
| Falsos negativos (IA rechaza un cierre correcto) | Botón de override del supervisor que dispara revisión humana |
| Costos de inferencia | YOLOv8 corre local en Jetson Orin; Gemini Vision solo cuando es necesario |

## Referencias

- Selleck, R., Hassall, M. E., Cattani, M. (2022). *Determining the reliability of critical controls in mining.* Safety, 8(3), 64. **Dato clave: confiabilidad real de controles críticos = 42 %** después de implementación documental → necesidad imperiosa de verificación de segundo nivel.
- Vaughan, D. (1996). *The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA.*
