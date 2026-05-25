---
theme: default
background: '#0F0F10'
class: text-white
title: Caso 13 LRAC · Innovadores en Acción 2026
info: |
  Diagnóstico y Gobernanza del Sistema LRAC · Mina Juanita S.A.
  MMG Las Bambas · Innovadores en Acción 2026 · Talentos de Cobre.
  Postulante: Emanuel Edgar Ancco Guaygua.
mdc: true
fonts:
  sans: Inter
  serif: 'Source Serif Pro'
  mono: 'JetBrains Mono'
colorSchema: dark
download: true
exportFilename: emanuel-ancco-lrac-slides
transition: slide-left
---

<div class="absolute top-6 left-6 text-xs opacity-60">MMG Las Bambas · Innovadores en Acción 2026 · Caso 13 VP SHE</div>

<div class="h-full flex flex-col justify-center items-start px-16">

<div class="border-l-4 border-red-600 pl-6 mb-8">
  <div class="text-sm opacity-60 tracking-widest uppercase">Informe Técnico · 10 minutos</div>
</div>

# Diagnóstico y Gobernanza<br>del Sistema LRAC

<div class="text-xl opacity-80 mb-12">Mina Juanita S.A. · 4 500 trabajadores · 4 VPs · 12 gerencias</div>

<div class="text-base opacity-70">
  <div class="mb-2"><strong>Emanuel Edgar Ancco Guaygua</strong> · Bach. Ing. Civil UPC · AI Automation Engineer en gen+</div>
  <div>🏆 2.º AI Talent Demo Day 2026 con GAIATECH VIGÍA</div>
</div>

</div>

<div class="absolute bottom-6 right-6 text-xs opacity-50">21 de mayo de 2026</div>

---
layout: default
---

# El problema en 1 pantalla

<div class="grid grid-cols-3 gap-6 mt-8">

<div class="bg-red-900/30 border-l-4 border-red-600 p-5 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">Calidad de captura</div>
  <div class="text-5xl font-extrabold my-2">55.28<span class="text-2xl">%</span></div>
  <div class="text-xs opacity-70">cumplimiento global LRAC</div>
</div>

<div class="bg-orange-900/30 border-l-4 border-orange-500 p-5 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">LRAC-4P por VP</div>
  <div class="text-5xl font-extrabold my-2">69.2<span class="text-2xl">%</span></div>
  <div class="text-xs opacity-70">índice consolidado promedio anual</div>
</div>

<div class="bg-blue-900/30 border-l-4 border-blue-400 p-5 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">Trabajadores</div>
  <div class="text-5xl font-extrabold my-2">4 500</div>
  <div class="text-xs opacity-70">tajo abierto · sin sistema referente interno</div>
</div>

</div>

<div class="mt-10 text-lg">

**El reto:** los reportes preventivos caen al 55 %. Las 4 VPs convergen en una banda estrecha (68.57 % – 69.71 %) sin que ninguna lidere consistentemente. La pregunta es **dónde duele y cómo se arregla**.

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">2 / 14</div>

---
layout: default
---

# Estructura · 4 VPs · 12 gerencias · 4 meses

<div class="grid grid-cols-4 gap-4 mt-6 text-sm">

<div class="bg-red-900/20 p-4 rounded border-l-4 border-red-600">
  <div class="font-bold text-lg mb-2">OPERACIONES</div>
  <div class="opacity-80 leading-tight">
    DESARROLLO RECURSOS<br>
    MANTENIMIENTO<br>
    MINA<br>
    PLANTA<br>
    SERV. TÉCNICOS
  </div>
</div>

<div class="bg-orange-900/20 p-4 rounded border-l-4 border-orange-500">
  <div class="font-bold text-lg mb-2">PROYECTOS</div>
  <div class="opacity-80 leading-tight">
    PROYECTOS 1<br>
    PROYECTOS 2
  </div>
</div>

<div class="bg-green-900/20 p-4 rounded border-l-4 border-green-600">
  <div class="font-bold text-lg mb-2">SHE</div>
  <div class="opacity-80 leading-tight">
    MEDIO AMBIENTE<br>
    RELAVERAS<br>
    SSO
  </div>
</div>

<div class="bg-blue-900/20 p-4 rounded border-l-4 border-blue-400">
  <div class="font-bold text-lg mb-2">SUPPLY</div>
  <div class="opacity-80 leading-tight">
    ABASTECIMIENTO<br>
    LOGISTICA
  </div>
</div>

</div>

<div class="mt-8 grid grid-cols-2 gap-6 text-sm">

<div>

**4 pilares del LRAC-4P**

$$\text{LRAC{-}4P} = 0.3\,L + 0.2\,R + 0.2\,A + 0.3\,C$$

- L = 0.6 · FTO + 0.4 · 3Q
- R = 0.5 · CCV + 0.5 · ACC
- A = 0.6 · NMAP + 0.4 · VEA P1
- C = DESEMPEÑO contratistas

</div>

<div>

**Periodo y datos**

- Enero – Abril 2026
- 337 registros en BASE
- 48 filas gerencia × mes
- 16 filas VP × mes
- Diccionario formal del set entregado

</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">3 / 14</div>

---
layout: default
---

# Metodología

<div class="grid grid-cols-2 gap-8 mt-6">

<div>

## Análisis estadístico

- Descriptivos por VP y gerencia (μ, σ, CV)
- **Kruskal-Wallis** sobre las 4 VPs
- **Post-hoc Dunn** con corrección Bonferroni
- **Score compuesto** $S = \mu - \sigma$
- **Shewhart I-Chart** sobre 16 puntos VP × mes
- **Mann-Kendall** para tendencia mensual
- **Matriz de correlación 7×7** entre herramientas

</div>

<div>

## Marco conceptual

- ISO 45001:2018 § 5.1, 5.4, 10.2
- ICMM Critical Control Management (2024)
- Hudson Safety Culture Maturity Ladder
- DuPont Bradley Curve
- Just Culture (Reason 1997, Dekker 2012)
- Felt Leadership (DuPont / British Safety Council)
- DS 024-2016-EM + DS 023-2017-EM + DS 034-2023-EM

</div>

</div>

<div class="mt-8">

## Herramientas computacionales

<div class="text-sm opacity-90">
Python 3.12 · NumPy · SciPy · pandas · matplotlib · openpyxl<br>
LaTeX (Times New Roman 12 pt · interlineado 1.5)<br>
Streamlit + Plotly para el demo interactivo · Power BI Desktop para el .pbix anexo
</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">4 / 14</div>

---
layout: default
---

# Hallazgo 1 · Peores gerencias en enero 2026

<div class="grid grid-cols-2 gap-6 mt-4">

<div>

<table class="text-sm">
<thead>
<tr class="border-b border-red-600">
<th class="text-left py-2">Herramienta</th>
<th class="text-left py-2">Peor gerencia</th>
<th class="text-left py-2">VP</th>
<th class="text-right py-2">Valor</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-700">
<td class="py-2"><strong>FTO</strong></td>
<td>PLANTA</td>
<td><span class="text-red-400">OPERACIONES</span></td>
<td class="text-right font-bold">45.0 %</td>
</tr>
<tr class="border-b border-gray-700">
<td class="py-2"><strong>3Q</strong></td>
<td>MEDIO AMBIENTE</td>
<td><span class="text-green-400">SHE</span></td>
<td class="text-right font-bold">39.0 %</td>
</tr>
<tr class="border-b border-gray-700">
<td class="py-2"><strong>ACC</strong></td>
<td>MANTENIMIENTO</td>
<td><span class="text-red-400">OPERACIONES</span></td>
<td class="text-right font-bold">39.0 %</td>
</tr>
<tr>
<td class="py-2"><strong>NMAP</strong></td>
<td>SERV. TÉCNICOS</td>
<td><span class="text-red-400">OPERACIONES</span></td>
<td class="text-right font-bold">36.0 %</td>
</tr>
</tbody>
</table>

</div>

<div class="text-sm space-y-3">

<div class="bg-red-900/30 p-3 rounded border-l-4 border-red-600">
  <strong>3 de 4 peores</strong> pertenecen a la <strong>VP OPERACIONES</strong>.
</div>

<div class="bg-orange-900/30 p-3 rounded border-l-4 border-orange-500">
  El <strong>custodio del sistema</strong> (MEDIO AMBIENTE, VP SHE) es el <strong>peor en 3Q</strong> — la herramienta más simple del Pilar Liderazgo.
</div>

<div class="bg-blue-900/30 p-3 rounded border-l-4 border-blue-400">
  Dispersión en 3Q (σ = 13.34 pp) y ACC (σ = 14.61 pp): hay gerencias > 80 % y otras < 40 % en el mismo mes.
</div>

</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">5 / 14</div>

---
layout: default
---

# Hallazgo 2 · VP con LRAC-4P promedio más alto

<div class="text-sm mt-4">

<table>
<thead>
<tr class="border-b border-red-600">
<th class="text-left py-2">VP</th>
<th class="text-right py-2">μ anual</th>
<th class="text-right py-2">σ</th>
<th class="text-right py-2">CV%</th>
<th class="text-right py-2">Amplitud</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-700 bg-blue-900/20">
<td class="py-2 font-bold">SUPPLY</td>
<td class="text-right font-bold">69.71 %</td>
<td class="text-right">5.83 pp</td>
<td class="text-right">8.37</td>
<td class="text-right">14.23 pp</td>
</tr>
<tr class="border-b border-gray-700">
<td class="py-2">OPERACIONES</td>
<td class="text-right">69.70 %</td>
<td class="text-right">1.25 pp</td>
<td class="text-right">1.80</td>
<td class="text-right">2.92 pp</td>
</tr>
<tr class="border-b border-gray-700">
<td class="py-2">PROYECTOS</td>
<td class="text-right">68.72 %</td>
<td class="text-right">3.91 pp</td>
<td class="text-right">5.69</td>
<td class="text-right">8.22 pp</td>
</tr>
<tr>
<td class="py-2">SHE</td>
<td class="text-right">68.57 %</td>
<td class="text-right">0.96 pp</td>
<td class="text-right">1.40</td>
<td class="text-right">2.11 pp</td>
</tr>
</tbody>
</table>

</div>

<div class="mt-6 grid grid-cols-2 gap-4 text-sm">

<div class="bg-blue-900/30 p-3 rounded border-l-4 border-blue-400">
  <strong>SUPPLY lidera el promedio</strong> con 69.71 %. Su herramienta más alta: <strong>ACC = 78.12 %</strong>.
</div>

<div class="bg-red-900/30 p-3 rounded border-l-4 border-red-600">
  Pero su <strong>CV = 8.37 %</strong>, 4.6× mayor que <strong>OPERACIONES (CV = 1.80 %)</strong> que prácticamente empata en 69.70 %.
</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">6 / 14</div>

---
layout: default
---

# Hallazgo 3 · VP PROYECTOS

<div class="grid grid-cols-2 gap-8 mt-4">

<div>

<table class="text-sm">
<thead>
<tr class="border-b border-red-600">
<th class="text-left py-2">Indicador</th>
<th class="text-right py-2">μ</th>
<th class="text-right py-2">Mín</th>
<th class="text-right py-2">Máx</th>
</tr>
</thead>
<tbody>
<tr class="border-b border-gray-700"><td class="py-1">FTO</td><td class="text-right">76.12 %</td><td class="text-right">68.00 %</td><td class="text-right">86.50 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">CCV</td><td class="text-right">71.75 %</td><td class="text-right">63.00 %</td><td class="text-right">83.50 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">3Q</td><td class="text-right">71.50 %</td><td class="text-right">64.00 %</td><td class="text-right">79.00 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">NMAP</td><td class="text-right">67.75 %</td><td class="text-right">51.50 %</td><td class="text-right">78.00 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">VEA P1</td><td class="text-right">66.12 %</td><td class="text-right">54.50 %</td><td class="text-right">76.50 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">DESEMPEÑO</td><td class="text-right">65.75 %</td><td class="text-right">58.00 %</td><td class="text-right">72.50 %</td></tr>
<tr class="bg-red-900/30"><td class="py-1 font-bold">ACC</td><td class="text-right font-bold">61.12 %</td><td class="text-right font-bold">50.00 %</td><td class="text-right font-bold">70.00 %</td></tr>
</tbody>
</table>

</div>

<div class="space-y-3 text-sm">

<div class="bg-red-900/30 p-3 rounded border-l-4 border-red-600">
  <div class="text-xs opacity-60">Promedio general (7 indicadores × 4 meses)</div>
  <div class="text-3xl font-extrabold">68.59 %</div>
</div>

<div class="bg-orange-900/30 p-3 rounded border-l-4 border-orange-500">
  <div class="text-xs opacity-60">ACC PROYECTOS · valor anual</div>
  <div class="text-3xl font-extrabold">61.12 %</div>
  <div class="text-xs">Mes peor: marzo (50 %) — cierre fiscal Q1<br>Mes mejor: abril (70 %)</div>
</div>

<div class="bg-blue-900/30 p-3 rounded border-l-4 border-blue-400">
  <div class="text-xs opacity-70">39 % de acciones quedan abiertas mes a mes → caldo de cultivo para normalización de la desviación (Vaughan, 1996).</div>
</div>

</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">7 / 14</div>

---
layout: default
---

# Hallazgo 4 · LRAC-4P por VP

<div class="grid grid-cols-2 gap-8 mt-4 text-sm">

<div>

## Por promedio anual

<table class="mt-2">
<tr class="border-b border-gray-700"><td class="py-1">🥇 SUPPLY</td><td class="text-right font-bold">69.71 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥈 OPERACIONES</td><td class="text-right">69.70 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥉 PROYECTOS</td><td class="text-right">68.72 %</td></tr>
<tr><td class="py-1">⬇ SHE</td><td class="text-right">68.57 %</td></tr>
</table>

<div class="mt-3 bg-gray-800/50 p-3 rounded">Brecha entre extremos: <strong>1.14 pp</strong></div>

</div>

<div>

## Al cierre (abril 2026)

<table class="mt-2">
<tr class="border-b border-gray-700"><td class="py-1">🥇 PROYECTOS</td><td class="text-right font-bold">71.25 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥈 SHE</td><td class="text-right">69.39 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥉 OPERACIONES</td><td class="text-right">69.33 %</td></tr>
<tr><td class="py-1">⬇ SUPPLY</td><td class="text-right">68.98 %</td></tr>
</table>

<div class="mt-3 bg-red-900/30 p-3 rounded border-l-4 border-red-600">
  <strong>Rotación entre el promedio anual y el cierre.</strong> No existe un sistema dominante.
</div>

</div>

</div>

<div class="mt-6 text-xs opacity-80">

**Evolución mensual LRAC-4P:**

| VP | ENE | FEB | MAR | ABR | Δ Ene→Abr |
|---|---|---|---|---|---|
| OPERACIONES | 71.49 | 69.42 | 68.57 | 69.33 | **−2.16 pp** ↓ |
| PROYECTOS | 66.33 | 72.75 | 64.53 | 71.25 | +4.92 pp ↕ |
| SHE | 69.19 | 67.27 | 68.43 | 69.39 | +0.19 pp → |
| SUPPLY | 62.95 | 77.18 | 69.73 | 68.98 | +6.03 pp ↕ |

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">8 / 14</div>

---
layout: default
---

# Refuerzo estadístico inferencial

<div class="grid grid-cols-2 gap-8 mt-4 text-sm">

<div>

## Kruskal-Wallis (4 VPs · n = 48)

<div class="bg-gray-800/50 p-4 rounded font-mono text-base mt-2">
H = 1.32 · <strong class="text-red-400">p = 0.7237</strong>
</div>

<div class="mt-2 opacity-80 text-xs">
La convergencia entre VPs (68.57 % – 69.71 %) <strong>no es estadísticamente diferente de cero</strong>. Post-hoc Dunn confirma: 6 / 6 comparaciones no significativas (todas p<sub>bonf</sub> = 1.000).
</div>

</div>

<div>

## Score compuesto $S = \mu - \sigma$

<table class="mt-2">
<tr class="border-b border-gray-700"><td class="py-1">🥇 OPERACIONES</td><td class="text-right font-bold">68.45 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥈 SHE</td><td class="text-right">67.61 %</td></tr>
<tr class="border-b border-gray-700"><td class="py-1">🥉 PROYECTOS</td><td class="text-right">64.80 %</td></tr>
<tr><td class="py-1">⬇ SUPPLY</td><td class="text-right text-red-400 font-bold">63.88 %</td></tr>
</table>

<div class="mt-2 opacity-80 text-xs">Cuando se premia la estabilidad junto al promedio, <strong>el ranking se invierte</strong>: SUPPLY cae al último lugar; OPERACIONES emerge como el sistema más confiable.</div>

</div>

</div>

<div class="mt-6 grid grid-cols-3 gap-4 text-xs">

<div class="bg-orange-900/30 p-3 rounded border-l-4 border-orange-500">
  <strong>Shewhart I-Chart</strong> · sistema bajo control técnico (cero puntos fuera de ±3σ); pero centerline en 69.17 %.
</div>

<div class="bg-red-900/30 p-3 rounded border-l-4 border-red-600">
  <strong>Mann-Kendall OPERACIONES</strong> · τ = −0.667. Tendencia decreciente: alarma temprana.
</div>

<div class="bg-blue-900/30 p-3 rounded border-l-4 border-blue-400">
  <strong>Correlación 7×7</strong> · máx |r| = 0.30. Las herramientas son independientes; el índice 4P está bien diseñado.
</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">9 / 14</div>

---
layout: default
---

# Diagnóstico cultural · Hudson

<div class="mt-8">

<div class="grid grid-cols-5 gap-2 text-xs text-center">

<div class="bg-red-950 p-4 rounded">
  <div class="font-bold">PATOLÓGICA</div>
  <div class="opacity-60 mt-1">0–30 %</div>
  <div class="opacity-40 mt-1">¿quién se enteró?</div>
</div>

<div class="bg-red-900 p-4 rounded">
  <div class="font-bold">REACTIVA</div>
  <div class="opacity-60 mt-1">30–50 %</div>
  <div class="opacity-40 mt-1">tras el accidente</div>
</div>

<div class="bg-orange-700 p-4 rounded ring-4 ring-orange-300">
  <div class="font-bold">CALCULATIVA</div>
  <div class="opacity-60 mt-1">50–70 %</div>
  <div class="opacity-90 mt-1 font-bold">⬅ aquí estamos</div>
</div>

<div class="bg-yellow-700 p-4 rounded">
  <div class="font-bold">PROACTIVA</div>
  <div class="opacity-60 mt-1">70–85 %</div>
  <div class="opacity-40 mt-1">anticipación</div>
</div>

<div class="bg-green-700 p-4 rounded">
  <div class="font-bold">GENERATIVA</div>
  <div class="opacity-60 mt-1">85–100 %</div>
  <div class="opacity-40 mt-1">ADN organizacional</div>
</div>

</div>

</div>

<div class="mt-10 text-sm">

Las cuatro VPs de Mina Juanita S.A. se ubican en la frontera <strong>Calculativa → Proactiva</strong> de Hudson (Foster & Hoult, 2013), equivalente al estadio <strong>Dependiente</strong> de la curva de Bradley (Siuta et al., 2022).

Hay sistemas formales (formatos, comités, planes anuales). Pero el cumplimiento depende de la supervisión y el reporte se realiza por mandato, no por convicción interdependiente. **Migrar a Proactiva exige palancas culturales — no solo más sistemas.**

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">10 / 14</div>

---
layout: default
---

# 4 módulos GAIATECH M1.0 · habilitadores del plan

<div class="grid grid-cols-2 gap-4 mt-4 text-sm">

<div class="bg-red-900/30 border-l-4 border-red-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">M1.A · Visión EPP</div>
  <div class="font-bold text-base mb-1">Vision Pro PDK + ConstEdge</div>
  <div class="text-xs opacity-90">YOLOv8 sobre 14 055 imágenes peruanas · <strong>mAP@0.5 = 87.67 %</strong> · 38 FPS sostenidos · Jetson Orin Nano Super · 11 clases EPP</div>
  <div class="text-xs opacity-60 mt-2">Pilar R · L · <strong>en producción</strong></div>
</div>

<div class="bg-orange-900/30 border-l-4 border-orange-500 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">M1.B · Aecodito Minero</div>
  <div class="font-bold text-base mb-1">Bot WhatsApp + n8n + Gemini Pro</div>
  <div class="text-xs opacity-90"><strong>50 nodos n8n</strong> · 10 herramientas externas integradas · Postgres pgvector · procesa texto / audio / foto / PDF</div>
  <div class="text-xs opacity-60 mt-2">Pilar L · A · C · <strong>en producción</strong></div>
</div>

<div class="bg-green-900/30 border-l-4 border-green-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">M1.C · GAIATECH VIGÍA</div>
  <div class="font-bold text-base mb-1">FPGA Gowin + ESP32 + LSTM-AE</div>
  <div class="text-xs opacity-90">FFT en hardware + autoencoder PyTorch · <strong>F1 = 0.961</strong> · latencia alerta &lt; 2 s · 🏆 2.º AI Talent Demo Day 2026</div>
  <div class="text-xs opacity-60 mt-2">Pilar R · <strong>prototipo funcional</strong></div>
</div>

<div class="bg-blue-900/30 border-l-4 border-blue-400 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">M1.D · Dashboard ejecutivo</div>
  <div class="font-bold text-base mb-1">Next.js 16 + Postgres + Gemini Pro</div>
  <div class="text-xs opacity-90">Single Pane of Glass rol-based · alertas sintéticas · reportes ejecutivos Gemini Pro · login httpOnly</div>
  <div class="text-xs opacity-60 mt-2">Pilar L · R · A · C · <strong>en producción</strong></div>
</div>

</div>

<div class="mt-6 text-center text-xs opacity-70">
No son propuestas conceptuales. Son activos desplegables desde el día 1.
</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">11 / 14</div>

---
layout: default
---

# Plan de Acción · 31 acciones · 3 horizontes

<div class="grid grid-cols-3 gap-4 mt-4 text-sm">

<div class="bg-red-900/30 border-l-4 border-red-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">Horizonte 1 · 0–3 meses</div>
  <div class="text-3xl font-extrabold my-1">10 acciones</div>
  <div class="text-xs opacity-80">Quick wins · estabilizar y dar señales</div>
  <div class="mt-3 text-xs space-y-1 opacity-90">
    <div>• Pacto público 3Q del VP SHE</div>
    <div>• War-room ACC en MANTENIMIENTO</div>
    <div>• Plan NMAP+ con 5 capacitaciones</div>
    <div>• Cápsula semanal + quiz adaptativo</div>
  </div>
  <div class="mt-3 text-xs font-mono opacity-70">CAPEX S/ 63 k · OPEX 36.6 k</div>
</div>

<div class="bg-orange-900/30 border-l-4 border-orange-500 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">Horizonte 2 · 3–9 meses</div>
  <div class="text-3xl font-extrabold my-1">8 acciones</div>
  <div class="text-xs opacity-80">Digitalizar el bucle · Mina Inteligente 2030</div>
  <div class="mt-3 text-xs space-y-1 opacity-90">
    <div>• Plataforma RACS conversacional</div>
    <div>• Visión EPP en accesos + obra</div>
    <div>• Monitoreo estructural relaves</div>
    <div>• Dashboard ejecutivo Single Pane</div>
  </div>
  <div class="mt-3 text-xs font-mono opacity-70">CAPEX S/ 160 k · OPEX 91.6 k</div>
</div>

<div class="bg-green-900/30 border-l-4 border-green-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase tracking-wider">Horizonte 3 · 9–24 meses</div>
  <div class="text-3xl font-extrabold my-1">13 acciones</div>
  <div class="text-xs opacity-80">Madurar y blindar · Proactiva → Generativa</div>
  <div class="mt-3 text-xs space-y-1 opacity-90">
    <div>• Comité LRAC corporativo mensual</div>
    <div>• Gemelo digital + ML predictivo</div>
    <div>• Wearables fatiga + biométrico</div>
    <div>• Universidad LRAC interna + PSCI</div>
  </div>
  <div class="mt-3 text-xs font-mono opacity-70">CAPEX S/ 508 k · OPEX 359 k</div>
</div>

</div>

<div class="mt-6 bg-gray-800/50 p-4 rounded text-sm text-center">
Cada acción tiene <strong>KPI SMART · owner RACI · presupuesto · dependencias · horizonte</strong>. Hoja de ruta auditable, no lista de buenas intenciones.
</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">12 / 14</div>

---
layout: default
---

# Business case · 24 meses

<div class="grid grid-cols-4 gap-4 mt-4 text-sm">

<div class="bg-green-900/30 border-l-4 border-green-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase">NPV base</div>
  <div class="text-3xl font-extrabold">S/ 1.21 M</div>
  <div class="text-xs opacity-70">Tasa descuento 10 %</div>
</div>

<div class="bg-green-900/30 border-l-4 border-green-600 p-4 rounded">
  <div class="text-xs opacity-60 uppercase">NPV optimista</div>
  <div class="text-3xl font-extrabold">S/ 3.81 M</div>
  <div class="text-xs opacity-70">p = 0.3 × fatalidad evitada</div>
</div>

<div class="bg-blue-900/30 border-l-4 border-blue-400 p-4 rounded">
  <div class="text-xs opacity-60 uppercase">IRR anualizada</div>
  <div class="text-3xl font-extrabold">343 %</div>
  <div class="text-xs opacity-70">Modelo conservador</div>
</div>

<div class="bg-orange-900/30 border-l-4 border-orange-500 p-4 rounded">
  <div class="text-xs opacity-60 uppercase">Payback</div>
  <div class="text-3xl font-extrabold">Mes 11</div>
  <div class="text-xs opacity-70">Sin contar fatalidades evitadas</div>
</div>

</div>

<div class="grid grid-cols-2 gap-6 mt-6 text-sm">

<div>

## Inversión total

| Componente | Monto |
|---|---|
| CAPEX 24 meses | S/ 731 000 |
| OPEX acumulado | S/ 487 200 |
| **Total** | **S/ 1 218 200** |
| **Equivalente USD** | **~ USD 325 000** |

</div>

<div>

## Beneficios anuales (base)

| Línea | Estimado anual |
|---|---|
| Reducción multas SUNAFIL / OSINERGMIN | S/ 200 000 |
| Reducción paros operativos | S/ 1 500 000 |
| Eficiencia procesos SHE | S/ 500 000 |
| **Total anual** | **S/ 2 200 000** |

</div>

</div>

<div class="mt-4 text-xs opacity-70">
Una sola fatalidad evitada vale S/ 5–20 M (multas + indemnizaciones + paro + daño reputacional). El plan se autofinancia en el escenario base; multiplica por tres su retorno si previene siquiera el 30 % de probabilidad de un evento fatal.
</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">13 / 14</div>

---
layout: default
class: text-center
---

<div class="h-full flex flex-col justify-center items-center px-12">

<div class="border-l-4 border-red-600 pl-4 mb-8 text-left">
  <div class="text-xs opacity-60 tracking-widest uppercase">GAIATECH M1.0</div>
</div>

<div class="text-5xl font-extrabold mb-3">No es PowerPoint.</div>
<div class="text-3xl opacity-80 mb-12">Es producción.</div>

<div class="grid grid-cols-3 gap-12 text-sm mb-12">
  <div>
    <div class="text-4xl font-extrabold text-red-500">4</div>
    <div class="opacity-70">módulos en producción</div>
  </div>
  <div>
    <div class="text-4xl font-extrabold text-orange-400">12</div>
    <div class="opacity-70">workflows documentados</div>
  </div>
  <div>
    <div class="text-4xl font-extrabold text-green-400">31</div>
    <div class="opacity-70">acciones del plan</div>
  </div>
</div>

<div class="text-sm space-y-2 mb-8">
  <div>📂 <code>github.com/emanuelancco/lasbambas-lrac-2026</code></div>
  <div>🌐 <code>lasbambas-lrac-emanuel.streamlit.app</code></div>
  <div>📄 Informe PDF de 25 páginas · Times 12 pt · interlineado 1.5</div>
</div>

<div class="border-t border-gray-700 pt-6 mt-4 text-sm opacity-80">
  <div class="font-bold">Emanuel Edgar Ancco Guaygua</div>
  <div>Bach. Ing. Civil UPC · AI Automation Engineer en gen+ · Origen Puno</div>
  <div class="mt-2">🏆 2.º AI Talent Demo Day 2026 con GAIATECH VIGÍA</div>
  <div class="mt-1 opacity-70">Innovadores en Acción 2026 · Caso 13 LRAC · VP SHE</div>
</div>

</div>

<div class="absolute bottom-4 right-6 text-xs opacity-40">14 / 14</div>
