"""
Página 2 — Simulador del Plan de Acción Estratégico LRAC
Sliders por pilar recalculan el LRAC-4P proyectado y muestran impacto del plan.
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Simulador del Plan", page_icon="🎯", layout="wide")

st.title("🎯 Simulador del Plan de Acción Estratégico")
st.caption("Mueve los sliders por pilar para visualizar el impacto de cada palanca sobre el LRAC-4P proyectado")

st.markdown(
    """
    El índice consolidado se calcula con la fórmula:
    $$
    \\text{LRAC--4P} = 0.3 \\cdot L + 0.2 \\cdot R + 0.2 \\cdot A + 0.3 \\cdot C
    $$
    Los valores base corresponden al promedio corporativo abril 2026.
    Las metas a 24 meses provienen del Plan de Acción Estratégico (Sección 7 del informe).
    """
)

# Baseline abril 2026
BASE = {"L": 67.6, "R": 69.7, "A": 67.7, "C": 68.9}
META_24M = {"L": 85.0, "R": 85.0, "A": 85.0, "C": 85.0}
META_12M = {"L": 75.0, "R": 76.0, "A": 76.0, "C": 75.0}

st.divider()

c1, c2 = st.columns([3, 2])

with c1:
    st.markdown("### Palancas por pilar")
    st.caption("Ajusta el nivel proyectado de cada pilar")

    cl1, cl2 = st.columns(2)
    cl3, cl4 = st.columns(2)

    with cl1:
        L = st.slider("**Pilar L — Liderazgo**", 50.0, 95.0, BASE["L"], 0.5, key="L",
                       help="FTO + 3Q. Habilitadores: workflows LRAC-001/002 (Aecodito) + LRAC-021 (geofence 6-4-2)")
    with cl2:
        R = st.slider("**Pilar R — Riesgos**", 50.0, 95.0, BASE["R"], 0.5, key="R",
                       help="CCV + ACC. Habilitadores: workflows LRAC-010/011 (visión EPP) + LRAC-012 (cierre con IA) + LRAC-020 (VIGÍA estructural)")
    with cl3:
        A = st.slider("**Pilar A — Aprendizaje**", 50.0, 95.0, BASE["A"], 0.5, key="A",
                       help="NMAP + VEA P1. Habilitadores: workflow LRAC-004 (cápsulas + quiz adaptativo)")
    with cl4:
        C = st.slider("**Pilar C — Contratistas**", 50.0, 95.0, BASE["C"], 0.5, key="C",
                       help="Desempeño SHE. Habilitadores: workflow LRAC-004 onboarding + dashboard rol-based M1.D")

    lrac_proy = 0.3 * L + 0.2 * R + 0.2 * A + 0.3 * C
    lrac_base = 0.3 * BASE["L"] + 0.2 * BASE["R"] + 0.2 * BASE["A"] + 0.3 * BASE["C"]
    delta = lrac_proy - lrac_base

    st.divider()
    st.markdown("### Resultado proyectado")
    m1, m2, m3 = st.columns(3)
    m1.metric("LRAC-4P base (abr 2026)", f"{lrac_base:.2f} %")
    m2.metric("LRAC-4P proyectado", f"{lrac_proy:.2f} %", delta=f"{delta:+.2f} pp")
    estado = "🟢 Óptimo" if lrac_proy >= 75 else ("🟡 Esperado" if lrac_proy >= 60 else "🔴 Debajo")
    m3.metric("Estado", estado)

with c2:
    st.markdown("### Comparativa")
    fig = go.Figure()
    cats = ["L", "R", "A", "C"]
    fig.add_trace(go.Bar(name="Base abr 2026", x=cats, y=[BASE[c] for c in cats], marker_color="#666"))
    fig.add_trace(go.Bar(name="Proyectado (slider)", x=cats, y=[L, R, A, C],
                         marker_color=["#C8102E", "#FF7F0E", "#2E7D32", "#1F77B4"]))
    fig.add_trace(go.Scatter(name="Meta 12 m", x=cats, y=[META_12M[c] for c in cats],
                              mode="markers", marker=dict(symbol="line-ew", size=20, color="gold")))
    fig.add_trace(go.Scatter(name="Meta 24 m", x=cats, y=[META_24M[c] for c in cats],
                              mode="markers", marker=dict(symbol="line-ew", size=20, color="lightgreen")))
    fig.update_layout(
        barmode="group",
        height=380,
        yaxis=dict(title="%", range=[50, 100]),
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ---------- TRAYECTORIA ----------
st.markdown("### Trayectoria proyectada del LRAC-4P corporativo (24 meses)")

# Asumimos rampa lineal: base → meta 12m → meta 24m
import numpy as np
meses = list(range(0, 25))
trayectoria = []
for m in meses:
    if m == 0:
        trayectoria.append(lrac_base)
    elif m <= 8:
        # base -> meta 12m via slider
        prog = m / 8
        valor = lrac_base + (lrac_proy - lrac_base) * prog
        trayectoria.append(valor)
    elif m <= 24:
        # slider proy -> meta 24m
        prog = (m - 8) / 16
        meta24p = 0.3 * META_24M["L"] + 0.2 * META_24M["R"] + 0.2 * META_24M["A"] + 0.3 * META_24M["C"]
        valor = lrac_proy + (meta24p - lrac_proy) * prog
        trayectoria.append(valor)

fig_traj = go.Figure()
fig_traj.add_trace(go.Scatter(
    x=meses, y=trayectoria,
    mode="lines+markers",
    fill="tozeroy",
    line=dict(color="#C8102E", width=3),
    marker=dict(size=6),
    name="LRAC-4P proyectado",
))
fig_traj.add_hline(y=70, line_dash="dash", line_color="gray", annotation_text="Meta corporativa 70 %")
fig_traj.add_hline(y=80, line_dash="dash", line_color="lightgreen", annotation_text="Meta 24 m: 80 %")
fig_traj.update_layout(
    height=380,
    xaxis=dict(title="Meses desde inicio del plan"),
    yaxis=dict(title="LRAC-4P (%)", range=[55, 90]),
    template="plotly_dark",
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
)
st.plotly_chart(fig_traj, use_container_width=True)

# ---------- TABLA DE ACCIONES PRIORIZADAS ----------
st.divider()
st.markdown("### Acciones recomendadas según los sliders")

acciones = []
if L < 75:
    acciones.append({"Pilar": "L", "Acción": "A-01 Pacto público 3Q VP SHE + A-03 Rondas 6-4-2 con geofence", "Workflow": "LRAC-001 + LRAC-021"})
if R < 75:
    acciones.append({"Pilar": "R", "Acción": "A-12 Visión EPP en accesos y obra + A-05 Auditoría externa CCV", "Workflow": "LRAC-010/011 + LRAC-012"})
if A < 75:
    acciones.append({"Pilar": "A", "Acción": "A-07 Plan NMAP+ + A-08 Cápsula semanal multimedia", "Workflow": "LRAC-004"})
if C < 75:
    acciones.append({"Pilar": "C", "Acción": "A-09 Bono solidario contratista + A-10 Onboarding asistido", "Workflow": "LRAC-004 (onboarding)"})
if not acciones:
    st.success("✅ Todos los pilares ≥75 %. El sistema está en estado óptimo. Foco: sostener y migrar de Proactivo a Generativo.")
else:
    import pandas as pd
    st.dataframe(pd.DataFrame(acciones), use_container_width=True, hide_index=True)

st.info("💡 El plan completo de 31 acciones × 3 horizontes × 5 frentes está en el informe PDF (Sección 7). Ver también la página **🤖 Workflows** para el detalle técnico.")
