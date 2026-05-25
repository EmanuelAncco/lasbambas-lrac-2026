# LRAC Governance Diagnosis · Mina Juanita S.A. (Las Bambas Case 13 · VP SHE)

[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-app-FF4B4B.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CI](https://github.com/emanuelancco/lasbambas-lrac-2026/actions/workflows/ci.yml/badge.svg)](https://github.com/emanuelancco/lasbambas-lrac-2026/actions)

> **Innovadores en Acción 2026 · MMG Las Bambas · Talentos de Cobre**
> Repositorio público con el análisis estadístico reproducible, el simulador interactivo y la documentación de los 12 *workflows* GAIATECH M1.0 que sustentan el Plan de Acción Estratégico LRAC.

---

## ES · Resumen

El sistema LRAC (Liderazgo, Riesgos, Aprendizaje, Contratistas) de **Mina Juanita S.A.** ---operación a tajo abierto con 4 500 trabajadores--- presenta un cumplimiento global de captura del **55.28 %** y un índice consolidado LRAC--4P por VP entre 68.57 % y 69.71 %. Este repositorio entrega:

1. **Análisis estadístico reproducible** del Excel del caso (337 registros, 4 VPs, 12 gerencias, 4 meses) con descriptivos, Kruskal-Wallis, Dunn (Bonferroni), Shewhart I-Chart, Mann-Kendall, score compuesto $S=\mu-\sigma$ y matriz de correlación 7×7.
2. **Plan de Acción Estratégico ejecutable** de 31 acciones × 3 horizontes × 5 frentes, con Gantt visual, RACI, KPIs SMART, *risk register* y *business case* (NPV S/ 1.21 M, IRR 343 %, payback mes 11).
3. **12 *workflows* GAIATECH M1.0** documentados (visión computacional EPP, agente conversacional TOKI, monitoreo estructural FPGA, dashboard ejecutivo y reportes Gemini Pro).
4. **Demo Streamlit interactivo** que replica el dashboard ejecutivo LRAC con los datos del caso, incluye simulador del plan y catálogo de los 12 *workflows*.

**Cumplimiento del instructivo:** PDF maestro de 25 páginas en Times New Roman 12 pt, interlineado 1.5, con bibliografía APA 7 (30 referencias, mayoría MDPI 2019-2026). Ver `report/Emanuel Edgar Ancco Guaygua.pdf`.

## EN · Summary

The LRAC management system (Leadership, Risks, Learning, Contractors) at **Mina Juanita S.A.** ---an open-pit operation with 4 500 workers--- shows a global compliance of **55.28 %** and a consolidated LRAC-4P index per Vice Presidency between 68.57 % and 69.71 %. This repository provides:

1. **Reproducible statistical analysis** of the case Excel (337 records, 4 VPs, 12 management units, 4 months) with descriptives, Kruskal-Wallis, Dunn (Bonferroni), Shewhart I-Chart, Mann-Kendall, composite score $S=\mu-\sigma$ and 7×7 correlation matrix.
2. **Executable Strategic Action Plan** with 31 actions × 3 horizons × 5 fronts, with visual Gantt, RACI, SMART KPIs, risk register, and business case (NPV S/ 1.21 M, IRR 343 %, payback at month 11).
3. **12 GAIATECH M1.0 workflows** documented (PPE computer vision, TOKI Mining conversational agent, FPGA structural monitoring, executive dashboard, and Gemini Pro automated reports).
4. **Interactive Streamlit demo** that mirrors the executive LRAC dashboard with the case data, with plan simulator and catalog of the 12 workflows.

**Brief compliance:** master PDF report (25 pages, Times New Roman 12 pt, 1.5 line spacing, APA-7 bibliography with 30 references, MDPI 2019-2026). See `report/Emanuel Edgar Ancco Guaygua.pdf`.

---

## Repository structure

```
lasbambas-lrac-2026/
├── README.md                ← este archivo
├── LICENSE                   ← MIT
├── requirements.txt          ← dependencias mínimas
├── data/
│   └── 00_data_caso.xlsx     ← datos del caso (ficticios)
├── analysis/                 ← scripts Python reproducibles
│   ├── 01_analisis_completo.py
│   ├── 02_figuras.py
│   ├── 03_estadistica_inferencial.py
│   └── 04_plan_ejecutable.py
├── figures/                  ← 14 figuras en PNG alta resolución
├── app/                      ← demo Streamlit
│   ├── main.py
│   ├── pages/
│   │   ├── 1_📊_Dashboard.py
│   │   ├── 2_🎯_Simulador.py
│   │   └── 3_🤖_Workflows.py
│   └── .streamlit/config.toml
├── docs/
│   ├── workflows/            ← 12 workflows GAIATECH M1.0 (.md)
│   ├── analisis-extra.md     ← apéndice A6: cross-indicator + estabilidad
│   └── comparativa-vs-comerciales.md ← TCO 5 años vs SAP/Intelex/Enablon
├── n8n-workflows/            ← 4 workflows n8n importables (JSON)
│   ├── LRAC-001-racs-guiado.json
│   ├── LRAC-003-cierre-bucle.json
│   ├── LRAC-004-capsula-quiz.json
│   └── LRAC-031-reporte-gemini.json
├── report/
│   └── Emanuel Edgar Ancco Guaygua.pdf
└── .github/workflows/ci.yml  ← GitHub Actions CI
```

## Quick start

### Reproducir el análisis estadístico

```bash
pip install -r requirements.txt
python analysis/01_analisis_completo.py        # análisis descriptivo
python analysis/02_figuras.py                  # genera 10 figuras
python analysis/03_estadistica_inferencial.py  # K-W, Dunn, SPC, Mann-Kendall
python analysis/04_plan_ejecutable.py          # Gantt + business case
```

Salidas: `analysis/resultados.json`, `analysis/resultados_inferencial.json`, `analysis/plan_ejecutable.json` y 16 figuras en `figures/`.

### Levantar el demo Streamlit

```bash
streamlit run app/main.py
```

Abre <http://localhost:8501>. Tres páginas: **Dashboard interactivo**, **Simulador del plan** y **Catálogo de 12 workflows GAIATECH M1.0**.

### Recompilar el informe LaTeX

```bash
cd report/
pdflatex "Emanuel Edgar Ancco Guaygua.tex"
pdflatex "Emanuel Edgar Ancco Guaygua.tex"   # segunda pasada para TOC/refs
```

Requiere TeX Live o MiKTeX.

## Resultados clave del análisis

| # | Hallazgo | Dato |
|---|---|---|
| 1 | Peores gerencias en enero | PLANTA (FTO 45 %), MEDIO AMBIENTE (3Q 39 %), MANTENIMIENTO (ACC 39 %), SERV. TÉCNICOS (NMAP 36 %) |
| 2 | VP con LRAC-4P más alto anual | SUPPLY 69.71 % (ACC 78.12 %), pero CV 8.37 % vs OPERACIONES CV 1.80 % |
| 3 | VP PROYECTOS — promedio general | 68.59 % · ACC 61.12 % (valle 50 % en marzo) |
| 4 | LRAC-4P por VP (anual) | SUPPLY > OPERACIONES > PROYECTOS > SHE |
| 5 | Indicador más débil corporativo | NMAP 65.71 % (Pilar A) |
| 6 | Diagnóstico cultural | Hudson Calculativa → Proactiva |
| 7 | Kruskal-Wallis (no parametrico) | H = 1.32, p = 0.724 (sin diferencia significativa entre VPs) |
| 8 | Score compuesto $S=\mu-\sigma$ | Inversion del ranking: OPERACIONES #1, SUPPLY #4 |

## Los 4 módulos GAIATECH M1.0

| Módulo | Componente | Métrica verificable | Pilares LRAC |
|---|---|---|---|
| M1.A | Visión computacional EPP (YOLOv8 + DeepFace) | 87.67 % mAP@0.5, 38 FPS Jetson Orin | R · L |
| M1.B | TOKI (n8n + Evolution API + Gemini) | 50 nodos, 10 tools, memoria persistente | L · A · C |
| M1.C | GAIATECH VIGÍA (FPGA Gowin + ESP32 + LSTM-AE) | F1 = 0.961, alerta < 2 s, 2.º AI Talent Demo Day | R |
| M1.D | Dashboard ejecutivo Vision Pro PDK | Single Pane of Glass rol-based, 11 clases EPP, login httpOnly | L · R · A · C |

## Bibliografía

30 referencias APA 7 con 22 papers MDPI (Safety, IJERPH, Sustainability, Sensors, Minerals, Mining). Marco normativo peruano (DS 024-2016-EM, DS 023-2017-EM, DS 034-2023-EM, Ley 29783, Resolución 122-2024-OS/CD), internacional (ISO 45001:2018, ICMM CCM 2024, GISTM 2020) y bibliográfico (Hudson 2007, Bradley/DuPont, Reason 1997, Dekker 2012, Weick & Sutcliffe 2007).

## Autor

**Emanuel Edgar Ancco Guaygua** · Bachiller en Ingeniería Civil UPC · AI Automation Engineer en gen+
[📧 coarp.eancco@gmail.com](mailto:coarp.eancco@gmail.com) ·
[🌐 emanuelancco.github.io/cv-portfolio](https://emanuelancco.github.io/cv-portfolio/) ·
[💼 LinkedIn](https://www.linkedin.com/in/emanuel-edgar-ancco-guaygua-a61210352)

2.º lugar AI Talent Demo Day 2026 (GAIATECH VIGÍA) · Origen Puno, Perú · Disponibilidad inmediata régimen 10×10 en Las Bambas.

## License

MIT — ver [LICENSE](LICENSE).

> Datos del caso (Mina Juanita S.A.) son ficticios y se entregan como parte del programa Innovadores en Acción 2026.
> Los activos GAIATECH M1.0 referenciados son propiedad intelectual del autor; este repositorio publica únicamente el análisis y la documentación arquitectónica, no su código de producción.
