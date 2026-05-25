"""
Página 1 — Dashboard LRAC interactivo
Filtros VP / Gerencia / Mes sobre los datos del caso Mina Juanita S.A.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(page_title="Dashboard LRAC", page_icon="📊", layout="wide")

# Paleta MMG
COLORES_VP = {
    "OPERACIONES": "#C8102E",
    "PROYECTOS":   "#FF7F0E",
    "SHE":         "#2E7D32",
    "SUPPLY":      "#1F77B4",
}

@st.cache_data(ttl=3600)
def load_data():
    here = Path(__file__).resolve()
    # repo root: .../lasbambas-lrac-2026/
    root = here.parents[2]
    xlsx = root / "data" / "00_data_caso.xlsx"
    base = pd.read_excel(xlsx, sheet_name="BASE")
    lrac_vp = pd.read_excel(xlsx, sheet_name="LRACxVP")
    lrac_ger = pd.read_excel(xlsx, sheet_name="LRACxGerencia")
    lrac_global = pd.read_excel(xlsx, sheet_name="LRAC_Global")
    # Normalizar encabezado AÑO (mojibake)
    for df in (base, lrac_vp, lrac_ger, lrac_global):
        df.columns = [c.replace("A�O", "ANIO") for c in df.columns]
    return base, lrac_vp, lrac_ger, lrac_global

base, lrac_vp, lrac_ger, lrac_global = load_data()

st.title("📊 Dashboard LRAC interactivo")
st.caption("Datos del caso Mina Juanita S.A. · Enero–Abril 2026 · 12 gerencias × 4 VPs")

# ---------- FILTROS ----------
with st.sidebar:
    st.markdown("### Filtros")
    meses_orden = ["ENERO", "FEBRERO", "MARZO", "ABRIL"]
    mes_sel = st.multiselect("Mes", meses_orden, default=meses_orden)
    vps_sorted = sorted(base["VICEPRESIDENCIA"].dropna().unique())
    vp_sel = st.multiselect("Vicepresidencia", vps_sorted, default=vps_sorted)
    gerencias = sorted(base[base["VICEPRESIDENCIA"].isin(vp_sel)]["GERENCIA"].dropna().unique())
    ger_sel = st.multiselect("Gerencia", gerencias, default=gerencias)

# Filtrar
filtro_ger = lrac_ger[
    (lrac_ger["MES"].isin(mes_sel))
    & (lrac_ger["VICEPRESIDENCIA"].isin(vp_sel))
    & (lrac_ger["GERENCIA"].isin(ger_sel))
]
filtro_vp = lrac_vp[
    (lrac_vp["MES"].isin(mes_sel)) & (lrac_vp["VICEPRESIDENCIA"].isin(vp_sel))
]

# ---------- KPIs ----------
c1, c2, c3, c4 = st.columns(4)
if len(filtro_ger):
    lrac_avg = filtro_ger["LRAC-4P"].mean() * 100
    optimo = (filtro_ger["LRAC-4P"] >= 0.75).sum()
    debajo = (filtro_ger["LRAC-4P"] < 0.60).sum()
    c1.metric("LRAC-4P promedio", f"{lrac_avg:.2f} %", delta=f"{lrac_avg - 70:.2f} pp vs meta 70 %")
    c2.metric("Observaciones", f"{len(filtro_ger)}", delta=f"de {len(lrac_ger)} totales")
    c3.metric("Óptimo (≥75 %)", f"{optimo}", delta=f"{optimo/len(filtro_ger)*100:.1f} %", delta_color="off")
    c4.metric("Debajo (<60 %)", f"{debajo}", delta=f"{debajo/len(filtro_ger)*100:.1f} %", delta_color="inverse")
else:
    st.warning("No hay datos con los filtros seleccionados")

st.divider()

# ---------- EVOLUCION ----------
st.markdown("### Evolución mensual del LRAC-4P por VP")
if len(filtro_vp):
    fig_ev = go.Figure()
    for vp in filtro_vp["VICEPRESIDENCIA"].unique():
        df_vp = filtro_vp[filtro_vp["VICEPRESIDENCIA"] == vp].sort_values("MES_NUM")
        fig_ev.add_trace(
            go.Scatter(
                x=df_vp["MES"],
                y=df_vp["LRAC-4P"] * 100,
                mode="lines+markers+text",
                name=vp,
                line=dict(color=COLORES_VP.get(vp, "#888"), width=3),
                marker=dict(size=10),
                text=[f"{v*100:.1f}%" for v in df_vp["LRAC-4P"]],
                textposition="top center",
                textfont=dict(size=10),
            )
        )
    fig_ev.add_hline(y=70, line_dash="dash", line_color="gray", annotation_text="Meta 70 %")
    fig_ev.update_layout(
        height=420,
        yaxis=dict(title="LRAC-4P (%)", range=[60, 80]),
        xaxis=dict(title="Mes"),
        hovermode="x unified",
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_ev, use_container_width=True)

# ---------- HEATMAP PILARES ----------
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### Heatmap por pilar y VP (promedio del filtro)")
    if len(filtro_vp):
        pivot = filtro_vp.groupby("VICEPRESIDENCIA")[["Pilar L", "Pilar R", "Pilar A", "Pilar C"]].mean() * 100
        pivot.columns = ["L (Liderazgo)", "R (Riesgos)", "A (Aprendizaje)", "C (Contratistas)"]
        fig_hm = px.imshow(
            pivot,
            text_auto=".1f",
            color_continuous_scale="RdYlGn",
            aspect="auto",
            zmin=60, zmax=80,
            labels=dict(color="%"),
        )
        fig_hm.update_layout(height=380, template="plotly_dark", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_hm, use_container_width=True)

with col_b:
    st.markdown("### Ranking de gerencias (LRAC-4P promedio)")
    if len(filtro_ger):
        ranking = (
            filtro_ger.groupby(["VICEPRESIDENCIA", "GERENCIA"])["LRAC-4P"]
            .mean()
            .reset_index()
            .sort_values("LRAC-4P", ascending=True)
        )
        ranking["color"] = ranking["VICEPRESIDENCIA"].map(COLORES_VP)
        fig_rk = go.Figure()
        fig_rk.add_trace(
            go.Bar(
                y=ranking["GERENCIA"] + " (" + ranking["VICEPRESIDENCIA"].str[:4] + ")",
                x=ranking["LRAC-4P"] * 100,
                orientation="h",
                marker_color=ranking["color"],
                text=[f"{v*100:.1f}%" for v in ranking["LRAC-4P"]],
                textposition="outside",
            )
        )
        fig_rk.add_vline(x=70, line_dash="dash", line_color="gray")
        fig_rk.update_layout(
            height=380,
            xaxis=dict(title="LRAC-4P (%)", range=[55, 85]),
            yaxis=dict(title=""),
            template="plotly_dark",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
        )
        st.plotly_chart(fig_rk, use_container_width=True)

# ---------- TABLA DETALLE ----------
st.markdown("### Detalle por gerencia-mes")
if len(filtro_ger):
    show = filtro_ger[
        ["VICEPRESIDENCIA", "GERENCIA", "MES", "3Q", "ACC", "CCV", "DESEMPE�O", "FTO", "NMAP", "VEA P1", "LRAC-4P"]
    ].copy()
    # rename mojibake
    show = show.rename(columns={"DESEMPE�O": "DESEMPEÑO"})
    for col in ["3Q", "ACC", "CCV", "DESEMPEÑO", "FTO", "NMAP", "VEA P1", "LRAC-4P"]:
        show[col] = (show[col] * 100).round(1)
    st.dataframe(
        show,
        use_container_width=True,
        hide_index=True,
        height=300,
    )
