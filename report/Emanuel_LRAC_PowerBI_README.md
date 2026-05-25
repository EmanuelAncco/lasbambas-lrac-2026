# Emanuel_LRAC_Dashboard.pbix — guía de armado

> Anexo A5 del informe Innovadores en Acción 2026 · Caso 13 LRAC.
>
> Por ser un formato propietario (binario) que requiere Power BI Desktop, el archivo `.pbix` se arma en ~30 minutos siguiendo esta guía. Todo el modelo está pensado para que abrir el archivo y reproducir los hallazgos del informe sea instantáneo.

## Fuente de datos

`data/00_data_caso.xlsx` del repositorio.

Hojas a importar:
- `BASE` — 337 registros (long format)
- `LRACxGerencia` — 48 filas (gerencia × mes)
- `LRACxVP` — 16 filas (VP × mes)
- `LRAC_Global` — 4 filas (corporativo × mes)
- `Diccionario` — metadatos

## Modelo tabular sugerido

```
                ┌──────────────────────────┐
                │   Dim_Mes                 │
                │   ─ MES (texto)           │
                │   ─ MES_NUM (1-12)        │
                │   ─ FECHA                 │
                └────────────┬──────────────┘
                             │ 1
                             │
                             │ * (n)
            ┌────────────────┴────────────────┐
            │   Fact_LRACxGerencia            │
            │   ─ VICEPRESIDENCIA             │
            │   ─ GERENCIA                    │
            │   ─ MES_NUM (FK)                │
            │   ─ FTO, 3Q, CCV, ACC,          │
            │     NMAP, VEA P1, DESEMPEÑO     │
            │   ─ Pilar L, R, A, C            │
            │   ─ LRAC-4P                     │
            └─────────────────────────────────┘
                             │
                             │
            ┌────────────────┴────────────────┐
            │   Dim_VP                         │
            │   ─ VICEPRESIDENCIA              │
            │   ─ Color (paleta MMG)           │
            └──────────────────────────────────┘
```

## Medidas DAX clave

```dax
-- Pilar L = 0.6 * FTO + 0.4 * 3Q
Pilar L = 0.6 * AVERAGE('Fact_LRAC'[FTO]) + 0.4 * AVERAGE('Fact_LRAC'[3Q])

-- Pilar R = 0.5 * CCV + 0.5 * ACC
Pilar R = 0.5 * AVERAGE('Fact_LRAC'[CCV]) + 0.5 * AVERAGE('Fact_LRAC'[ACC])

-- Pilar A = 0.6 * NMAP + 0.4 * VEA P1
Pilar A = 0.6 * AVERAGE('Fact_LRAC'[NMAP]) + 0.4 * AVERAGE('Fact_LRAC'[VEA P1])

-- Pilar C = DESEMPEÑO
Pilar C = AVERAGE('Fact_LRAC'[DESEMPEÑO])

-- LRAC-4P consolidado
LRAC-4P =
    0.3 * [Pilar L] +
    0.2 * [Pilar R] +
    0.2 * [Pilar A] +
    0.3 * [Pilar C]

-- Score compuesto S = mu - sigma
LRAC_mu = AVERAGE('Fact_LRAC'[LRAC-4P])
LRAC_sigma = STDEV.S('Fact_LRAC'[LRAC-4P])
LRAC_Score = [LRAC_mu] - [LRAC_sigma]

-- Estado semáforo
LRAC_Estado =
    SWITCH(
        TRUE(),
        [LRAC-4P] >= 0.75, "Óptimo",
        [LRAC-4P] >= 0.60, "Esperado",
        "Debajo"
    )

-- Color semáforo (para campo Color en visuales)
LRAC_Color =
    SWITCH(
        [LRAC_Estado],
        "Óptimo", "#2E7D32",
        "Esperado", "#F9A825",
        "Debajo", "#C62828"
    )

-- Brecha vs meta 70%
LRAC_Brecha_Meta = [LRAC-4P] - 0.70

-- Indicador más débil por VP
Indicador_min =
    MIN('Fact_LRAC'[FTO], 'Fact_LRAC'[3Q], 'Fact_LRAC'[CCV], 'Fact_LRAC'[ACC],
        'Fact_LRAC'[NMAP], 'Fact_LRAC'[VEA P1], 'Fact_LRAC'[DESEMPEÑO])
```

## Visuales sugeridos (4 pestañas)

### Pestaña 1 · Resumen ejecutivo

- KPI cards: LRAC-4P corporativo · Pilar más débil · NMAP global · Estado actual.
- Tarjeta de "Top patrones" (texto con últimos hallazgos).

### Pestaña 2 · Dashboard interactivo

- Slicers: VP · Gerencia · Mes.
- Gráfico de líneas: evolución LRAC-4P por VP (Ene-Abr 2026).
- Matriz: VP × Mes con conditional formatting tipo heatmap.
- Tabla detalle con drill-down por gerencia.

### Pestaña 3 · Pilares y herramientas

- Heatmap (matriz) VP × Pilar.
- Radar (matriz personalizada) con las 7 herramientas por VP.
- Ranking horizontal de las 12 gerencias por LRAC-4P (con error bars σ).
- Indicador más débil corporativo (gráfico de barras horizontal).

### Pestaña 4 · Plan y simulador

- Texto + tabla con las 31 acciones del plan (importadas desde `analysis/plan_ejecutable.json`).
- "What-if" parameters por pilar: sliders que recalculan LRAC-4P proyectado.
- Tarjeta NPV / IRR / Payback.
- Gantt simple con `Sequence Visualization` o gráfico de barras tipo timeline.

## Paleta y formato

- Tema: Custom JSON con paleta MMG.
- Colores principales: `#C8102E` (rojo), `#FF7F0E` (naranja), `#2E7D32` (verde), `#1F77B4` (azul), `#4D4D4D` (gris), `#F2F2F2` (gris claro).
- Tipografía: Segoe UI Bold para títulos, Segoe UI Regular para tablas.

## Pasos para producir el .pbix (~30 min)

1. Abrir Power BI Desktop.
2. **Get Data → Excel** → seleccionar `data/00_data_caso.xlsx`.
3. Importar las 4 hojas (BASE, LRACxGerencia, LRACxVP, LRAC_Global) como tablas.
4. Renombrar: `Fact_LRAC`, `Fact_VP`, `Fact_Global`, `Dim_Diccionario`.
5. **Modeling → New Measure** → pegar las medidas DAX de arriba (una por una).
6. **Modeling → Manage Relationships** → conectar por `MES_NUM` (Dim_Mes 1:* Fact_LRAC).
7. Crear las 4 pestañas con los visuales sugeridos.
8. **Format → Page background → color #0F0F10** (modo oscuro opcional).
9. **File → Save As** → `Emanuel_LRAC_Dashboard.pbix`.
10. Adjuntar al envío y subir a Drive público.

## Alternativa rápida si no hay Power BI Desktop

- **Streamlit demo** (anexo A2) ya replica el dashboard. URL: `lasbambas-lrac-emanuel.streamlit.app`.
- **Excel pivot table** sobre `00_data_caso.xlsx` con tablas dinámicas + filtros.
- **Google Sheets + Looker Studio** (gratuito): importar el Excel, conectar a Looker Studio, replicar visuales.

> La plantilla DAX y la documentación están listas. El armado en Desktop es manual pero directo.
