---
tema: analitica-power-bi-mineria
fuentes: 30
actualizado: 2026-05-20
---
# Analítica, Power BI y plan de acción para LRAC

## 1. Repositorios GitHub relevantes

- **vishall29/PowerBI_SafetyDashboard** — plantilla DAX/medidas para incidentes, TRIFR, near-miss. Reutilizable cambiando dataset por FTO/3Q/CCV/ACC/NMAP/VEA-P1.
- **mining/mining** (BI en Python + OLAP) — backbone para procesar tablas largas antes de Power BI.
- **apsinghAnalytics/US_RecessionIndicatorsAndGoogleTrends** — patrón Python → Power BI con scripts custom.
- GitHub topics `power-bi-dashboard` y `safety-dashboard`.

## 2. Métricas estadísticas apropiadas

- **Coeficiente de Variación (CV = σ/μ)**: comparar dispersión entre indicadores con escalas distintas (FTO vs NMAP).
- **Control charts (Shewhart/CUSUM/EWMA)** sobre hazard reporting: paper *JEMIS — SPC as Early Warning Signal* aplica SPC sobre leading indicators mineros.
- **Índice de Cumplimiento Global (ICG)**: promedio ponderado normalizado `Σ(wᵢ · cumplimientoᵢ) / Σwᵢ`.
- Métricas complementarias: tasa per cápita, mediana + IQR (robusta), Kruskal-Wallis para comparar VPs.

## 3. Underreporting — comportamiento organizacional

- **Hopkins** (*Failure to Learn*): malas noticias no suben. Áreas con menos reportes ≠ más seguras — suelen tener miedo a reportar.
- **Reason — Swiss Cheese / Just Culture**: underreporting es agujero latente. Sin just culture no hay reportes sinceros.
- **Hudson (Parker et al., 2006)**: organizaciones Calculativas (donde está LRAC al 55%) reportan por sistema sin convicción.

## 4. Casos LRAC / benchmarks

- **Las Bambas**: ya tiene modelo de liderazgo visible + RAC + 6 horas supervisión en campo.
- **BHP Fatality Elimination Program (FEL, 2020-2025)**: estandariza controles críticos y HPIs.
- **Antofagasta Minerals**: 4 herramientas culturales (planned task risk assessment, shift change, role confirmation, process confirmation) + librería de 500 PTRA.

## 5. RACS peruano

DS 024-2016-EM Art. 7 + modificatoria DS 023-2017-EM y DS 034-2023-EM: obliga al titular minero a "controlar oportunamente los riesgos originados por condiciones o actos subestándar reportados". **Anexo 24** detalla formatos.

**Vacío regulatorio**: la calidad del reporte (no solo cantidad) — que un sistema LRAC moderno cubre.

## 6. Plan de acción — estructura recomendada

Marco **Corto (0-3 meses) / Mediano (3-9) / Largo (9-24)** con ownership por VP:

**Corto**:
- Estandarización criterios calidad reporte
- Capacitación express
- Kioskos móviles
- Refuerzo liderazgo visible (modelo Las Bambas)

**Mediano**:
- Plataforma digital RACS con app móvil
- Gamificación
- Feedback loop al reportante (Cascade/Speakup4Safety)

**Largo**:
- Integración con SPC en tiempo real
- Transición Hudson Calculativo → Proactivo
- Evaluación cultural anual

## 7. Aplicación Hudson al 55%

55% con alta varianza inter-VP = **Calculativo bajo, transitando desde Reactivo**. Plan:
- Reactivo → Calculativo: cerrar brechas SUPPLY/áreas rezagadas (capacitación + sistemas)
- Calculativo → Proactivo (meta 80%): just culture, feedback al reportante, reconocimiento positivo, métricas de **calidad**
- Proactivo → Generativo: el reporte es valor, no obligación; meta 95% sostenido + CV<15%

## 8. Casos 55% → 80%

- Anglo American (Elimination of Fatalities) y BHP FEL: aumentos de **30-50% en near-miss reporting** tras 24 meses.
- Metodología: capacitación + cambio cultural + tecnología + just culture + feedback visible.

## Fuentes

- vishall29/PowerBI_SafetyDashboard: https://github.com/vishall29/PowerBI_SafetyDashboard
- mining/mining: https://github.com/mining/mining
- GitHub power-bi-dashboard: https://github.com/topics/power-bi-dashboard
- JEMIS SPC Mining: https://jemis.ub.ac.id/index.php/jemis/article/view/374
- ResearchGate SPC Mining Safety Intervention: https://www.researchgate.net/publication/348484534
- ScienceDirect Monitoring CV: https://www.sciencedirect.com/science/article/abs/pii/S0360835221005040
- 911 Metallurgist UK Coal Mining maturity: https://www.911metallurgist.com/wp-content/uploads/2016/01/The-Safety-Journey-Using-a-Safety-Maturity-Model-for-Safety-Planning-and-Assurance-in-the-UK-Coal-Mining-Industry.pdf
- DS 024-2016-EM oficial: https://cdn.www.gob.pe/uploads/document/file/901782/DS-024-2016-EM.pdf
- DS 034-2023-EM modificatoria: https://busquedas.elperuano.pe/dispositivo/NL/2249422-2
- Anexo 24 DS 024-2016-EM: http://spij.minjus.gob.pe/Graficos/Peru/2016/Julio/28/DS-024-2016-EM-ANEXO-24.pdf
- Revista Seguridad Minera estrategia Las Bambas: https://revistaseguridadminera.com/minas/estrategia-de-seguridad-en-minera-las-bambas/
- Las Bambas Minería de altura cap. 3: https://www.lasbambas.com/userfiles/cms/publicacion/documento/libro-las-bambas-capitulo3.pdf
- ICMM Critical Control Management: https://www.icmm.com/en-gb/our-work/health-and-safety/critical-control-management
- ICMM Leading Indicators OHS Mining: https://pimcore.icmm.com/website/publications/pdfs/health-and-safety/2012/guidance_indicators-ohs.pdf
- BHP Safety: https://www.bhp.com/sustainability/safety-health/safety
- Antofagasta PLC: https://www.antofagasta.co.uk/sustainability/health-and-safety/
- Cascade Safety Corrective Action: https://www.cascade.app/google-sheet-templates/safety-corrective-action-plan-template
- Cascade Safety KPIs: https://www.cascade.app/blog/kpis-health-and-safety
- BSC Designer Safety Scorecard: https://bscdesigner.com/safety-kpis.htm
- Opsima Mining KPIs: https://opsima.com/blog/kpis/mining-industry-kpis/
- Vector Solutions Safety KPI: https://www.vectorsolutions.com/resources/blogs/resources-blogs-safety-kpi-examples/
- Flevy Workplace Safety case mining: https://flevy.com/topic/workplace-safety/case-workplace-safety-international-mining-corp
- Springer Safety Climate MT Mining: https://link.springer.com/article/10.1007/s42461-021-00472-1
- Swiss Cheese Model Wikipedia: https://en.wikipedia.org/wiki/Swiss_cheese_model
- SmartQHSE Swiss Cheese 2026: https://www.smartqhse.com/safety-blog/swiss-cheese-model-incident-prevention-2026
- PMC Just culture near-miss: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12616966/
- Buenaventura RACS procedimiento: https://buenaventura.com/wp-content/uploads/2024/10/p_cor_sib_2019_P-COR-09.02-Reporte-de-Actos-y-Condiciones.pdf
- Tesis UNAP RACS: https://repositorio.unap.edu.pe/bitstream/handle/20.500.14082/12256/Chavez_Ruiz_Diego_Fernando.pdf
- SciELO modelo gestión contratistas: http://www.scielo.org.pe/scielo.php?script=sci_arttext&pid=S1810-99932021000200149
- Alicia Concytec supervisión: https://alicia.concytec.gob.pe/vufind/Record/UUNI_3b1a8a667dc344c05f5dfb12658bb194/Details
