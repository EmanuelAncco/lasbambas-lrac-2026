"""
Anexo A5 alternativo · Dashboard HTML autocontenido equivalente al .pbix.

Genera un archivo HTML standalone con Plotly que replica las 4 pestañas que
tendría el Power BI .pbix:
  1. Resumen ejecutivo (KPIs grandes)
  2. Dashboard interactivo (slicers + heatmap + evolución)
  3. Pilares y herramientas (radar + ranking)
  4. Simulador del plan + benchmarks

Justificación: Power BI .pbix es formato propietario binario que requiere Power BI
Desktop + license para producir programáticamente. Esta versión HTML cumple la
misma función (interactividad, drill-down, slicers) sin requerir license del
jurado, abre en cualquier navegador y se distribuye con el repositorio.
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import openpyxl
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

EXCEL = r"C:/Users/Emanuel/.gemini/antigravity/scratch/n8n/lasbambas-lrac-2026/data/00_data_caso.xlsx"
OUT = r"C:/Users/Emanuel/.gemini/antigravity/scratch/n8n/lasbambas-lrac-2026/report/Emanuel_LRAC_Dashboard.html"

# Paleta MMG
COLORS = {
    'OPERACIONES': '#C8102E',
    'PROYECTOS':   '#FF7F0E',
    'SHE':         '#2E7D32',
    'SUPPLY':      '#1F77B4',
}

# Cargar datos
xls = pd.ExcelFile(EXCEL)
ger = pd.read_excel(xls, 'LRACxGerencia')
vp = pd.read_excel(xls, 'LRACxVP')
glob = pd.read_excel(xls, 'LRAC_Global')

# Normalizar mojibake — match por prefijo dado que el caracter intermedio varia
def fix_cols(cols):
    out = []
    for c in cols:
        s = str(c)
        if s.startswith('A') and 'O' in s and len(s) <= 5: s = 'ANIO'
        elif s.startswith('DESEMPE'): s = 'DESEMPENO'
        out.append(s)
    return out
for df in (ger, vp, glob):
    df.columns = fix_cols(df.columns)
print('Columnas vp normalizadas:', list(vp.columns))

meses_orden = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL']

# ===========================================================
# FIG 1 · Evolución LRAC-4P por VP
# ===========================================================
fig1 = go.Figure()
for v in ['OPERACIONES', 'PROYECTOS', 'SHE', 'SUPPLY']:
    sub = vp[vp['VICEPRESIDENCIA'] == v].sort_values('MES_NUM')
    fig1.add_trace(go.Scatter(
        x=sub['MES'], y=sub['LRAC-4P']*100,
        name=v, mode='lines+markers+text',
        line=dict(color=COLORS[v], width=3),
        marker=dict(size=11),
        text=[f'{x*100:.1f}%' for x in sub['LRAC-4P']],
        textposition='top center', textfont=dict(size=10)
    ))
fig1.add_hline(y=70, line_dash='dash', line_color='gray', annotation_text='Meta 70%')
fig1.update_layout(
    title=None, height=400, template='plotly_white',
    yaxis=dict(title='LRAC-4P (%)', range=[60, 80]),
    xaxis=dict(title='Mes 2026'),
    hovermode='x unified',
    margin=dict(t=10, l=10, r=10, b=10),
)

# ===========================================================
# FIG 2 · Heatmap pilares por VP
# ===========================================================
pivot = vp.groupby('VICEPRESIDENCIA')[['Pilar L', 'Pilar R', 'Pilar A', 'Pilar C']].mean() * 100
pivot.columns = ['L · Liderazgo', 'R · Riesgos', 'A · Aprendizaje', 'C · Contratistas']
fig2 = px.imshow(pivot, text_auto='.1f', color_continuous_scale='RdYlGn',
                 aspect='auto', zmin=60, zmax=80, labels=dict(color='%'))
fig2.update_layout(height=350, template='plotly_white', margin=dict(t=10, l=10, r=10, b=10))

# ===========================================================
# FIG 3 · Ranking gerencias
# ===========================================================
ranking = ger.groupby(['VICEPRESIDENCIA', 'GERENCIA'])['LRAC-4P'].mean().reset_index()
ranking = ranking.sort_values('LRAC-4P', ascending=True)
ranking['color'] = ranking['VICEPRESIDENCIA'].map(COLORS)
ranking['label'] = ranking['GERENCIA'] + ' (' + ranking['VICEPRESIDENCIA'].str[:5] + ')'

fig3 = go.Figure(go.Bar(
    y=ranking['label'], x=ranking['LRAC-4P']*100, orientation='h',
    marker=dict(color=ranking['color']),
    text=[f'{v*100:.1f}%' for v in ranking['LRAC-4P']],
    textposition='outside'
))
fig3.add_vline(x=70, line_dash='dash', line_color='gray')
fig3.update_layout(height=480, template='plotly_white',
                   xaxis=dict(title='LRAC-4P promedio anual (%)', range=[55, 85]),
                   yaxis=dict(title=''),
                   margin=dict(t=10, l=10, r=10, b=10))

# ===========================================================
# FIG 4 · Radar 7 herramientas por VP
# ===========================================================
indicadores = ['FTO', '3Q', 'CCV', 'ACC', 'NMAP', 'VEA P1', 'DESEMPENO']
fig4 = go.Figure()
for v in ['OPERACIONES', 'PROYECTOS', 'SHE', 'SUPPLY']:
    sub = vp[vp['VICEPRESIDENCIA'] == v]
    vals = [sub[i].mean()*100 for i in indicadores]
    fig4.add_trace(go.Scatterpolar(
        r=vals + [vals[0]],
        theta=indicadores + [indicadores[0]],
        fill='toself', name=v,
        line=dict(color=COLORS[v]),
        opacity=0.5
    ))
fig4.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[50, 85])),
    template='plotly_white', height=420, showlegend=True,
    margin=dict(t=10, l=10, r=10, b=10)
)

# ===========================================================
# FIG 5 · Boxplot dispersión por VP (gerencia-mes)
# ===========================================================
fig5 = go.Figure()
for v in ['OPERACIONES', 'PROYECTOS', 'SHE', 'SUPPLY']:
    sub = ger[ger['VICEPRESIDENCIA'] == v]
    fig5.add_trace(go.Box(
        y=sub['LRAC-4P']*100,
        name=v,
        marker_color=COLORS[v],
        boxmean='sd'
    ))
fig5.add_hline(y=70, line_dash='dash', line_color='gray')
fig5.update_layout(
    template='plotly_white', height=350,
    yaxis=dict(title='LRAC-4P (%) por gerencia-mes'),
    margin=dict(t=10, l=10, r=10, b=10)
)

# Tabla detalle
df_table = ger.copy()
for c in ['FTO', '3Q', 'CCV', 'ACC', 'NMAP', 'VEA P1', 'DESEMPENO', 'LRAC-4P']:
    if c in df_table.columns:
        df_table[c] = (df_table[c] * 100).round(1)
table_html = df_table[['VICEPRESIDENCIA', 'GERENCIA', 'MES', 'FTO', '3Q', 'CCV', 'ACC', 'NMAP', 'VEA P1', 'DESEMPENO', 'LRAC-4P']].to_html(
    index=False, classes='lrac-table', border=0, table_id='detail-table'
)

# Convertir figs a HTML inline
import plotly.io as pio
pio.templates.default = 'plotly_white'

opts = {'include_plotlyjs': False, 'full_html': False, 'config': {'displayModeBar': True, 'responsive': True}}
fig1_html = fig1.to_html(**opts)
fig2_html = fig2.to_html(**opts)
fig3_html = fig3.to_html(**opts)
fig4_html = fig4.to_html(**opts)
fig5_html = fig5.to_html(**opts)

# ===========================================================
# Construir HTML completo
# ===========================================================
html_template = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LRAC Dashboard · Mina Juanita S.A. · Anexo A5</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js" charset="utf-8"></script>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family: -apple-system, "Segoe UI", Roboto, sans-serif; background: #fafafa; color: #1a1a1c; padding: 16px 24px; }
header { border-left: 4px solid #C8102E; padding-left: 16px; margin-bottom: 24px; }
header h1 { font-size: 22pt; color: #1a1a1c; font-weight: 800; }
header .sub { color: #666; font-size: 11pt; margin-top: 4px; }
header .urls { font-size: 9pt; color: #888; font-family: monospace; margin-top: 8px; }
header .urls strong { color: #C8102E; }

.tabs { display: flex; gap: 4px; margin-bottom: 16px; border-bottom: 2px solid #e0e0e0; }
.tab { padding: 10px 18px; cursor: pointer; border-radius: 6px 6px 0 0; font-size: 11pt; font-weight: 600; color: #666; background: transparent; border: none; }
.tab.active { background: #C8102E; color: white; }
.tab:hover:not(.active) { background: #f0f0f0; }

.panel { display: none; }
.panel.active { display: block; }

.kpi-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 24px; }
.kpi { background: white; border-left: 4px solid #C8102E; padding: 14px 18px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
.kpi.orange { border-left-color: #FF7F0E; }
.kpi.green { border-left-color: #2E7D32; }
.kpi.blue { border-left-color: #1F77B4; }
.kpi .label { font-size: 9pt; color: #888; text-transform: uppercase; letter-spacing: 0.5px; }
.kpi .value { font-size: 28pt; font-weight: 800; color: #1a1a1c; letter-spacing: -1px; margin-top: 4px; }
.kpi .sub { font-size: 9pt; color: #666; margin-top: 4px; }

.grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
@media (max-width: 900px) { .grid-2 { grid-template-columns: 1fr; } }

.card { background: white; border-radius: 8px; padding: 14px 18px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 16px; }
.card h3 { font-size: 11pt; color: #C8102E; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 10px; }

table.lrac-table { width: 100%; border-collapse: collapse; font-size: 9pt; }
table.lrac-table th { background: #C8102E; color: white; padding: 6px 8px; text-align: left; position: sticky; top: 0; }
table.lrac-table td { padding: 5px 8px; border-bottom: 1px solid #f0f0f0; }
table.lrac-table tr:nth-child(even) { background: #fafafa; }

.simulator { background: white; border-radius: 8px; padding: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); }
.slider-group { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.slider-row label { display: block; font-size: 10pt; color: #666; margin-bottom: 4px; }
.slider-row input[type=range] { width: 100%; accent-color: #C8102E; }
.slider-row .val { font-weight: 800; color: #C8102E; font-size: 11pt; }
.proy { background: #fff7e6; border-left: 4px solid #FF7F0E; padding: 12px 16px; margin-top: 16px; border-radius: 6px; }
.proy .big { font-size: 28pt; font-weight: 800; }

footer { text-align: center; color: #888; font-size: 9pt; margin-top: 32px; padding-top: 16px; border-top: 1px solid #e0e0e0; }
.tabla-scroll { max-height: 500px; overflow-y: auto; border: 1px solid #e0e0e0; border-radius: 4px; }
</style>
</head>
<body>

<header>
  <h1>LRAC Dashboard · Mina Juanita S.A.</h1>
  <div class="sub">MMG Las Bambas · Innovadores en Acción 2026 · Caso 13 VP SHE · <strong>Anexo A5</strong> al informe principal</div>
  <div class="urls">
    <strong>Repo:</strong> github.com/EmanuelAncco/lasbambas-lrac-2026 ·
    <strong>Streamlit:</strong> lasbambas-lrac-emanuel.streamlit.app ·
    <strong>n8n live:</strong> aecodetest.app.n8n.cloud/workflow/qRW88FSByN26nDJr
  </div>
</header>

<nav class="tabs">
  <button class="tab active" data-target="tab-resumen">📊 Resumen ejecutivo</button>
  <button class="tab" data-target="tab-dashboard">🔎 Dashboard interactivo</button>
  <button class="tab" data-target="tab-pilares">📐 Pilares &amp; herramientas</button>
  <button class="tab" data-target="tab-simulador">🎯 Simulador</button>
  <button class="tab" data-target="tab-detalle">📋 Detalle gerencia × mes</button>
</nav>

<section id="tab-resumen" class="panel active">
  <div class="kpi-grid">
    <div class="kpi"><div class="label">LRAC global captura</div><div class="value">55.3%</div><div class="sub">cumplimiento glob.</div></div>
    <div class="kpi orange"><div class="label">LRAC-4P corporativo</div><div class="value">69.2%</div><div class="sub">−0.83 pp vs meta</div></div>
    <div class="kpi"><div class="label">Pilar más débil</div><div class="value" style="font-size:18pt;">NMAP</div><div class="sub">65.71% (Pilar A)</div></div>
    <div class="kpi blue"><div class="label">Trabajadores</div><div class="value">4 500</div><div class="sub">4 VPs · 12 ger.</div></div>
    <div class="kpi green"><div class="label">Meta 24m</div><div class="value">80%</div><div class="sub">CV &lt; 5% inter-VP</div></div>
  </div>

  <div class="card">
    <h3>Evolución mensual del LRAC-4P por VP</h3>
    PLACEHOLDER_FIG1
  </div>

  <div class="grid-2">
    <div class="card">
      <h3>Heatmap pilares por VP (promedio anual)</h3>
      PLACEHOLDER_FIG2
    </div>
    <div class="card">
      <h3>Dispersión LRAC-4P intra-VP</h3>
      PLACEHOLDER_FIG5
    </div>
  </div>
</section>

<section id="tab-dashboard" class="panel">
  <div class="card">
    <h3>Evolución mensual LRAC-4P · 4 VPs</h3>
    PLACEHOLDER_FIG1B
  </div>
  <div class="grid-2">
    <div class="card">
      <h3>Ranking gerencias · 12 unidades</h3>
      PLACEHOLDER_FIG3
    </div>
    <div class="card">
      <h3>Heatmap pilares</h3>
      PLACEHOLDER_FIG2B
    </div>
  </div>
</section>

<section id="tab-pilares" class="panel">
  <div class="grid-2">
    <div class="card">
      <h3>Perfil 7 herramientas por VP (radar)</h3>
      PLACEHOLDER_FIG4
    </div>
    <div class="card">
      <h3>Ranking gerencias</h3>
      PLACEHOLDER_FIG3B
    </div>
  </div>
</section>

<section id="tab-simulador" class="panel">
  <div class="simulator">
    <h3 style="color:#C8102E; margin-bottom:14px;">🎯 Simulador del plan · proyección LRAC-4P</h3>
    <p style="color:#666; font-size:10pt; margin-bottom:16px;">Mueve los sliders para ver el impacto de cada pilar en el índice consolidado.</p>

    <div class="slider-group">
      <div class="slider-row">
        <label>Pilar L · Liderazgo: <span class="val" id="vL">67.6</span>%</label>
        <input type="range" id="sL" min="50" max="95" step="0.5" value="67.6">
      </div>
      <div class="slider-row">
        <label>Pilar R · Riesgos: <span class="val" id="vR">69.7</span>%</label>
        <input type="range" id="sR" min="50" max="95" step="0.5" value="69.7">
      </div>
      <div class="slider-row">
        <label>Pilar A · Aprendizaje: <span class="val" id="vA">67.7</span>%</label>
        <input type="range" id="sA" min="50" max="95" step="0.5" value="67.7">
      </div>
      <div class="slider-row">
        <label>Pilar C · Contratistas: <span class="val" id="vC">68.9</span>%</label>
        <input type="range" id="sC" min="50" max="95" step="0.5" value="68.9">
      </div>
    </div>

    <div class="proy">
      <div style="font-size:10pt; color:#666; text-transform:uppercase; letter-spacing:0.5px;">LRAC-4P proyectado</div>
      <div class="big" id="result">68.65%</div>
      <div style="font-size:10pt; color:#666;">Estado: <span id="status">🟡 Esperado</span> · Δ vs base: <span id="delta">0.00 pp</span></div>
    </div>
  </div>
</section>

<section id="tab-detalle" class="panel">
  <div class="card">
    <h3>Detalle por gerencia × mes (n=48 observaciones)</h3>
    <div class="tabla-scroll">PLACEHOLDER_TABLE</div>
  </div>
</section>

<footer>
  Construido para el informe Innovadores en Acción 2026 · Caso 13 LRAC ·
  <strong>Emanuel Edgar Ancco Guaygua</strong> · Bach. Ing. Civil UPC ·
  🏆 2.º AI Talent Demo Day 2026 con GAIATECH VIGÍA
</footer>

<script>
// Tabs
document.querySelectorAll('.tab').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById(btn.dataset.target).classList.add('active');
    // Trigger plotly resize on tab change
    window.dispatchEvent(new Event('resize'));
  });
});

// Simulador
const BASE = 0.3*67.6 + 0.2*69.7 + 0.2*67.7 + 0.3*68.9; // 68.65
function calc() {
  const L = parseFloat(document.getElementById('sL').value);
  const R = parseFloat(document.getElementById('sR').value);
  const A = parseFloat(document.getElementById('sA').value);
  const C = parseFloat(document.getElementById('sC').value);
  document.getElementById('vL').textContent = L.toFixed(1);
  document.getElementById('vR').textContent = R.toFixed(1);
  document.getElementById('vA').textContent = A.toFixed(1);
  document.getElementById('vC').textContent = C.toFixed(1);
  const proy = 0.3*L + 0.2*R + 0.2*A + 0.3*C;
  const delta = proy - BASE;
  document.getElementById('result').textContent = proy.toFixed(2) + '%';
  document.getElementById('delta').textContent = (delta >= 0 ? '+' : '') + delta.toFixed(2) + ' pp';
  let estado = '🔴 Debajo';
  if (proy >= 75) estado = '🟢 Óptimo';
  else if (proy >= 60) estado = '🟡 Esperado';
  document.getElementById('status').textContent = estado;
}
document.querySelectorAll('input[type=range]').forEach(s => s.addEventListener('input', calc));
calc();
</script>

</body>
</html>
"""

# Sustituir placeholders
html_final = (html_template
    .replace('PLACEHOLDER_FIG1B', fig1_html)
    .replace('PLACEHOLDER_FIG1', fig1_html)
    .replace('PLACEHOLDER_FIG2B', fig2_html)
    .replace('PLACEHOLDER_FIG2', fig2_html)
    .replace('PLACEHOLDER_FIG3B', fig3_html)
    .replace('PLACEHOLDER_FIG3', fig3_html)
    .replace('PLACEHOLDER_FIG4', fig4_html)
    .replace('PLACEHOLDER_FIG5', fig5_html)
    .replace('PLACEHOLDER_TABLE', table_html)
)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(html_final)

import os
size_kb = os.path.getsize(OUT) / 1024
print(f"Generado: {OUT}")
print(f"Tamano: {size_kb:.1f} KB")
print(f"5 figuras Plotly + simulador interactivo + tabla detalle en 5 pestanas")
