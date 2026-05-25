"""
LRAC Governance Dashboard — Mina Juanita S.A. (Las Bambas Case 13)
Demo Streamlit interactivo del informe Innovadores en Acción 2026.

Autor: Emanuel Edgar Ancco Guaygua
Repositorio: github.com/emanuelancco/lasbambas-lrac-2026
"""
import streamlit as st

st.set_page_config(
    page_title="LRAC · Mina Juanita · Innovadores en Acción 2026",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Demo interactivo del informe Innovadores en Acción 2026 · Caso 13 LRAC · MMG Las Bambas. Construido por Emanuel Edgar Ancco Guaygua.",
    },
)

# Header
st.markdown(
    """
    <div style='border-left: 4px solid #C8102E; padding-left: 20px; margin-bottom: 24px;'>
      <h1 style='margin:0; color:#fff;'>Diagnóstico y Gobernanza del Sistema LRAC</h1>
      <p style='color:#aaa; margin-top:4px;'>Mina Juanita S.A. · MMG Las Bambas · Innovadores en Acción 2026 · Caso 13 VP SHE</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# KPIs grandes
c1, c2, c3, c4 = st.columns(4)
c1.metric("LRAC global captura", "55.28 %", delta="-14.7 pp vs meta 70%", delta_color="inverse")
c2.metric("LRAC-4P corporativo", "69.17 %", delta="-0.83 pp vs meta 70%", delta_color="inverse")
c3.metric("Pilar más débil", "Aprendizaje (A)", delta="NMAP 65.71%")
c4.metric("NPV plan 24m", "S/ 1.21 M", delta="IRR 343 % · payback mes 11", delta_color="off")

st.divider()

col_a, col_b = st.columns([3, 2])

with col_a:
    st.markdown(
        """
        ### El reto

        Mina Juanita S.A. (caso del programa Innovadores en Acción 2026, MMG Las Bambas)
        es una operación a tajo abierto con **4 500 trabajadores** estructurada en
        **4 Vicepresidencias y 12 gerencias**. El sistema LRAC (Liderazgo, Riesgos,
        Aprendizaje, Contratistas) presenta un cumplimiento global de captura del
        **55.28 %** y un índice consolidado LRAC-4P por VP entre 68.57 % y 69.71 %.

        ### Qué muestra este demo

        Tres páginas accesibles desde la barra lateral:

        1. **📊 Dashboard interactivo** — filtros VP / Gerencia / Mes, evolución
           mensual del LRAC-4P, heatmap por pilar, ranking de las 12 gerencias y
           tabla detallada por indicador.
        2. **🎯 Simulador del plan** — sliders por pilar (L/R/A/C) que recalculan
           el LRAC-4P proyectado y muestran el impacto del Plan de Acción
           Estratégico a 24 meses.
        3. **🤖 Catálogo GAIATECH M1.0** — los 12 workflows de automatización
           (Aecodito Minero, Visión EPP, FPGA VIGÍA, Dashboard ejecutivo)
           que sustentan el plan, con stack, métricas y mapeo a las acciones.

        ### Hallazgos clave del análisis estadístico

        - **Kruskal-Wallis** sobre los 48 puntos VP × gerencia × mes: H = 1.32,
          p = 0.724. La convergencia entre VPs (68.57 % – 69.71 %) **no es
          estadísticamente significativa**.
        - **Score compuesto $S = \\mu - \\sigma$**: el ranking se **invierte**.
          OPERACIONES (S = 68.45 %) supera a SUPPLY (S = 63.88 %) cuando se
          premia la estabilidad junto al promedio.
        - **Mann-Kendall**: OPERACIONES con tendencia decreciente ($\\tau = -0.667$),
          alarma temprana de deterioro.
        - **NMAP = 65.71 %**: la herramienta más débil del sistema; el Pilar A
          (Aprendizaje) es el cuello de botella corporativo.
        """
    )

with col_b:
    st.markdown(
        """
        ### Los 4 módulos GAIATECH M1.0

        Habilitadores tecnológicos del Plan ya construidos por el autor:

        - **M1.A · Visión EPP**
          YOLOv8 87.67 % mAP, 38 FPS Jetson Orin
        - **M1.B · Aecodito Minero**
          n8n + Evolution API + Gemini Pro
          50 nodos, 10 herramientas
        - **M1.C · GAIATECH VIGÍA**
          FPGA Gowin + LSTM-AE, F1 = 0.961
          🏆 2.º AI Talent Demo Day 2026
        - **M1.D · Dashboard ejecutivo**
          Single Pane of Glass rol-based
          En producción · Vision Pro PDK

        ### Stack del repositorio

        Python 3.12 · NumPy · SciPy · pandas · Matplotlib · Streamlit · Plotly · LaTeX (Times 12 pt, 1.5).

        ### Recursos relacionados

        - 📄 [Informe PDF completo](https://github.com/emanuelancco/lasbambas-lrac-2026/blob/main/report/)
        - 📂 [Repo GitHub](https://github.com/emanuelancco/lasbambas-lrac-2026)
        - 🌐 [Portafolio técnico](https://emanuelancco.github.io/cv-portfolio/)
        """
    )

st.divider()

st.markdown(
    """
    <div style='text-align:center; color:#888; font-size:13px;'>
      Construido por <strong>Emanuel Edgar Ancco Guaygua</strong> · Bachiller en Ingeniería Civil UPC · AI Automation Engineer en gen+ · Puno, Perú · Mayo 2026<br>
      Caso simulado <em>Mina Juanita S.A.</em> entregado por el programa <em>Innovadores en Acción 2026</em>. Datos ficticios.
    </div>
    """,
    unsafe_allow_html=True,
)
