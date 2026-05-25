---
titulo: Análisis adicional cross-indicator y estabilidad intra-gerencia
tipo: apéndice digital
fecha: 2026-05-21
script_fuente: analysis/05_analisis_extra.py
resultados_json: analysis/resultados_extra.json
---

# Análisis adicional · LRAC Mina Juanita S.A.

Profundiza tres ángulos no cubiertos explícitamente por las preguntas del reto:
1. Peor gerencia por herramienta para **CCV, VEA P1 y DESEMPEÑO** (las 3 que el reto no pidió).
2. Patrones **cross-indicator**: gerencias que están en el bottom-3 en múltiples herramientas simultáneamente.
3. **Estabilidad intra-gerencia** (CV mensual): qué gerencias son consistentes y cuáles son volátiles.
4. **Heatmap herramienta × VP** en enero: identificar el par más débil del sistema.

---

## 1 · Peores gerencias por las herramientas no exploradas (enero 2026)

| Herramienta | Peor gerencia | VP | Valor | Media | Observación |
|---|---|---|---|---|---|
| **CCV** | SSO | **SHE** | **35.0 %** | 50.07 % | Los 3 peores en CCV son TODOS de VP SHE: SSO (35), RELAVERAS (38), MEDIO AMBIENTE (40). |
| **VEA P1** | PROYECTOS 1 | PROYECTOS | 45.0 % | 57.67 % | Paradoja: PROYECTOS 1 lidera el LRAC-4P anual (75.12 %) pero es la peor en aprendizaje VEA P1 en enero. |
| **DESEMPEÑO** | LOGISTICA | **SUPPLY** | **36.0 %** | 49.75 % | Ironía: VP SUPPLY tiene el mejor LRAC-4P anual pero su LOGISTICA es la peor del sistema en gestión de contratistas. |

### Implicación crítica

El análisis del reto pedido (FTO, 3Q, ACC, NMAP) detectó que **MEDIO AMBIENTE** (VP SHE) era peor en 3Q. Este análisis adicional **agrava** ese hallazgo: la VP SHE en su conjunto es la peor del sistema en **CCV** (controles críticos verificados). El custodio del sistema está reprobando en el indicador más correlacionado por ICMM 2024 con fatalidades (83 % de muertes por falla de controles críticos).

---

## 2 · Patrones cross-indicator · gerencias críticas overall

Ranking promedio en enero (posición #1 = peor por herramienta, de 12 gerencias en total):

| VP | Gerencia | Pos media | % media | En bottom-3 |
|---|---|---|---|---|
| **SHE** | **RELAVERAS** | **5.14** | **50.43 %** | **5 / 7** |
| OPERACIONES | MINA | 5.29 | 50.14 % | 3 / 7 |
| SHE | MEDIO AMBIENTE | 5.71 | 53.14 % | 4 / 7 |
| SUPPLY | ABASTECIMIENTO | 5.71 | 52.43 % | 1 / 7 |
| PROYECTOS | PROYECTOS 2 | 6.14 | 53.57 % | 1 / 7 |
| OPERACIONES | MANTENIMIENTO | 6.29 | 51.57 % | 1 / 7 |

### El hallazgo más fuerte de todo el caso

**RELAVERAS (VP SHE)** está en el bottom-3 en **5 de 7 herramientas** en enero 2026:

| Herramienta | Posición (de 12) | Valor | Estado |
|---|---|---|---|
| 3Q | #3 | 42.0 % | bottom-3 |
| ACC | #2 | 39.0 % | bottom-3 |
| **CCV** | **#2** | **38.0 %** | bottom-3 |
| NMAP | #3 | 41.0 % | bottom-3 |
| VEA P1 | #3 | 49.0 % | bottom-3 |
| FTO | #11 | 69.0 % | medio |
| DESEMPEÑO | #12 | 75.0 % | bueno |

**Implicación operativa:** RELAVERAS debe ser la gerencia #1 de intervención de las acciones del Horizonte 1 del plan. Y dada su naturaleza (operación de depósitos de relave bajo DS 034-2023-EM art. 418-423), su debilidad en CCV es directamente correlacionada con riesgo de incumplimiento normativo y eventos catastróficos.

---

## 3 · Estabilidad intra-gerencia · CV mensual del LRAC-4P

### Top 5 más estables (proceso bajo control)

| VP | Gerencia | CV % | σ (pp) |
|---|---|---|---|
| OPERACIONES | MANTENIMIENTO | 2.72 | 1.91 |
| **SHE** | **RELAVERAS** | 3.48 | 2.29 |
| OPERACIONES | SERV. TÉCNICOS | 4.03 | 2.85 |
| PROYECTOS | PROYECTOS 2 | 4.48 | 2.79 |
| OPERACIONES | PLANTA | 6.70 | 5.01 |

### Top 5 más volátiles (oportunidad de estandarización)

| VP | Gerencia | CV % | σ (pp) |
|---|---|---|---|
| **PROYECTOS** | **PROYECTOS 1** | **11.75** | 8.83 |
| SHE | MEDIO AMBIENTE | 10.96 | 7.77 |
| SUPPLY | LOGISTICA | 8.81 | 6.08 |
| SUPPLY | ABASTECIMIENTO | 8.65 | 6.09 |
| OPERACIONES | MINA | 7.29 | 4.87 |

### Paradoja PROYECTOS 1 (resuelta)

PROYECTOS 1 es **la gerencia con mejor LRAC-4P anual (75.12 %)**, pero también **la más volátil (CV = 11.75 %)**. Sus mediciones mensuales oscilan entre 51.5 % y 86.5 %. Esto significa que su excelencia es **estacional o evento-dependiente**, no estructural. Si la siguiente medición coincide con un mes "bajo", caería al fondo de la tabla.

**Recomendación:** PROYECTOS 1 no es el modelo a replicar. Para benchmarking interno, **MANTENIMIENTO** (CV 2.72 % con μ 70 %) o **PLANTA** (CV 6.70 % con μ 74.78 %) son mejores candidatos.

### RELAVERAS revisada

RELAVERAS aparece simultáneamente como:
- **Gerencia más crítica overall** en enero (Análisis 2)
- **Segunda gerencia más estable** del año (Análisis 3, CV 3.48 %)

Esto sugiere que RELAVERAS está **establemente mal**: no fluctúa, sino que su nivel bajo es persistente. La intervención requerida es de naturaleza cultural y estructural, no episódica.

---

## 4 · Heatmap herramienta × VP · enero 2026

|  | OPERACIONES | PROYECTOS | SHE | SUPPLY |
|---|---|---|---|---|
| FTO | 59.2 % | 54.0 % | 59.7 % | 61.0 % |
| 3Q | 53.8 % | 63.0 % | 51.7 % | 61.0 % |
| **CCV** | 52.0 % | 59.0 % | **37.7 %** ⚠ | 51.5 % |
| ACC | 57.2 % | 56.0 % | 63.0 % | 46.5 % |
| NMAP | 52.8 % | 50.0 % | 52.3 % | 59.0 % |
| VEA P1 | 64.8 % | 48.0 % | 54.7 % | 54.0 % |
| DESEMPEÑO | 48.8 % | 50.5 % | 58.3 % | 38.5 % |

**Par más débil del sistema en enero:** **CCV × SHE = 37.67 %**.

El sistema de Verificación de Controles Críticos no funciona en la VP que es la dueña del proceso. Esto es estructural, no anecdótico: las tres gerencias de SHE (SSO, RELAVERAS, MEDIO AMBIENTE) ocupan posiciones 1 al 3 en el ranking de peor desempeño en CCV.

---

## Cómo conecta con el Plan de Acción

| Hallazgo extra | Acción del plan afectada |
|---|---|
| RELAVERAS bottom-3 en 5/7 herramientas | Refuerza A-13 (VIGÍA estructural en relaves) y A-04 (war-room ACC ampliado a RELAVERAS) |
| CCV × SHE = 37.67 % | A-05 (auditoría 2do nivel CCV) debe priorizar SHE; A-06 (tablero ICAM) debe segmentar por VP |
| PROYECTOS 1 volátil | A-19 (Comité LRAC) debe analizar la fuente de variación de PROYECTOS 1 |
| LOGISTICA peor en DESEMPEÑO | A-09 (bono solidario) y A-27 (plan de retiro) ganan urgencia para los contratistas de logística |
| VP SHE peor en CCV de toda la organización | Cambio de gobernanza: el custodio del sistema debe pasar primero por su propio sistema (auto-auditoría obligatoria) |

---

## Reproducibilidad

```bash
cd analysis
python 05_analisis_extra.py
# Salida estructurada en analysis/resultados_extra.json
```

Tiempo de ejecución: < 1 s.

---

## Notas

- Estos análisis NO están contenidos en el cuerpo de las 25 páginas del PDF maestro (cumplen el límite del instructivo).
- Quedan referenciados en el repo como **Anexo digital A6** (análisis adicional) y mencionados en la Sección 6 Discusión del PDF con la frase: "El análisis cross-indicator publicado en el anexo digital identifica a RELAVERAS como la gerencia más crítica overall (bottom-3 en 5 de 7 herramientas)".
- Si en la etapa de sustentación se pregunta "¿por qué priorizan PROYECTOS 2 en el plan si RELAVERAS está peor?", la respuesta está aquí.
