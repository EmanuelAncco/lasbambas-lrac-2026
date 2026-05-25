# Catálogo GAIATECH M1.0 · 12 workflows de automatización LRAC

> Cada workflow ataca una brecha concreta del sistema LRAC de Mina Juanita S.A. y mapea a una acción específica del Plan de Acción Estratégico (Sección 7 del informe).

## Resumen por módulo

| Módulo | ID | Workflow | Pilar | Acción |
|---|---|---|---|---|
| **M1.B TOKI** | [LRAC-001](LRAC-001-racs-guiado.md) | RACS guiado conversacional | L · R | A-02 · A-11 |
| | [LRAC-002](LRAC-002-captura-voz.md) | Captura de voz a RACS | L · R | A-02 · A-11 |
| | [LRAC-003](LRAC-003-cierre-bucle.md) | Cierre de bucle con verificación IA | R | A-04 · A-11 |
| | [LRAC-004](LRAC-004-capsula-quiz.md) | Cápsula semanal + quiz adaptativo | A · C | A-08 · A-10 · A-28 |
| **M1.A Visión EPP** | [LRAC-010](LRAC-010-epp-accesos.md) | Detección EPP en accesos | L · R | A-12 |
| | [LRAC-011](LRAC-011-epp-continuo.md) | Detección EPP continua en obra | R | A-05 · A-12 |
| | [LRAC-012](LRAC-012-verif-cierre.md) | Verificación visual de cierre 2do nivel | R | A-05 |
| **M1.C GAIATECH VIGÍA** | [LRAC-020](LRAC-020-vibracion-presa.md) | Monitoreo vibración presa de relaves | R | A-13 |
| | [LRAC-021](LRAC-021-geofence-642.md) | Geofence 6-4-2 liderazgo visible | L | A-03 |
| **M1.D Dashboard** | [LRAC-030](LRAC-030-dashboard-she.md) | Dashboard SHE Single Pane of Glass | L·R·A·C | A-14 |
| | [LRAC-031](LRAC-031-reporte-gemini.md) | Reporte semanal Gemini Pro | L · A | A-06 · A-19 |
| | [LRAC-032](LRAC-032-osinergmin-vvo.md) | Auto-cumplimiento OSINERGMIN | R | A-13 · A-20 |

## Plantilla de documentación

Cada archivo `LRAC-NNN-*.md` sigue la estructura:

```yaml
---
id: LRAC-NNN
modulo: M1.X
nombre: Nombre del workflow
brecha: Brecha del sistema LRAC que ataca
stack: Tecnologías involucradas
metrica: KPI objetivo
acciones: [A-XX, A-YY]
pilar: L | R | A | C (uno o varios)
estado: produccion | prototipo | diseno
---
```

Secciones del contenido:
1. **Brecha que ataca** (con dato del Excel cuando aplica)
2. **Stack técnico** (componentes específicos)
3. **Flujo del workflow** (paso a paso)
4. **KPIs y métricas**
5. **Estado actual y dependencias**
6. **Riesgos y mitigaciones**

## Mapeo workflow ↔ módulo GAIATECH M1.0

```
                    ┌─────────────────────────────────────┐
                    │   M1.D · Dashboard ejecutivo         │
                    │   LRAC-030/031/032                   │
                    └──────────────▲──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────┐  ┌──────────────▼──────────┐  ┌────────────▼────────┐
│ M1.A · Visión  │  │  M1.B · TOKI  │  │ M1.C · GAIATECH      │
│ LRAC-010/011/  │  │  LRAC-001/002/003/004    │  │ VIGÍA                 │
│       012      │  │                          │  │ LRAC-020/021          │
└────────────────┘  └──────────────────────────┘  └──────────────────────┘
```
