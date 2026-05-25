"""
Página 3 — Catálogo de los 12 workflows GAIATECH M1.0
"""
import streamlit as st

st.set_page_config(page_title="Workflows GAIATECH M1.0", page_icon="🤖", layout="wide")

st.title("🤖 Catálogo GAIATECH M1.0 — 12 automatizaciones LRAC")
st.caption("Los workflows que sustentan el Plan de Acción Estratégico. Detalle técnico, stack y mapeo a las acciones del plan.")

WORKFLOWS = [
    # Aecodito Minero
    {"id": "LRAC-001", "modulo": "M1.B", "nombre": "RACS guiado conversacional",
     "brecha": "Calidad del reporte preventivo (55 %), FTO PLANTA 45 %",
     "stack": "WhatsApp Business + Evolution API + n8n + Gemini Pro + Postgres pgvector",
     "metrica": "≥2 reportes/trabajador/mes con foto+GPS ≥90 %",
     "acciones": ["A-02", "A-11"],
     "pilar": "L · R",
     "descripcion": "Operador escribe 'RACS' al bot → bot guía: foto, GPS automático, audio o texto → Gemini clasifica (acto/condición/severidad, fatal-risk relacionado) → push a Postgres → ticket en IEM mock → confirmación con número de ticket.",
     "color": "#C8102E"},
    {"id": "LRAC-002", "modulo": "M1.B", "nombre": "Captura de voz a RACS",
     "brecha": "Trabajadores en altura/EPP no pueden escribir",
     "stack": "Evolution API + Whisper/Gemini transcribe + n8n",
     "metrica": "Captura RACS en <90 s desde el inicio",
     "acciones": ["A-02", "A-11"],
     "pilar": "L · R",
     "descripcion": "Trabajador envía nota de voz por WhatsApp → Gemini Flash transcribe + estructura el reporte → bot confirma → registra. Elimina la fricción del teclado en obra.",
     "color": "#C8102E"},
    {"id": "LRAC-003", "modulo": "M1.B", "nombre": "Cierre de bucle con verificación IA",
     "brecha": "ACC 61 % en PROYECTOS · acciones marcadas como cerradas sin verificación",
     "stack": "n8n + YOLOv8/Gemini Vision + Postgres",
     "metrica": "≥95 % cierres con foto validada por IA",
     "acciones": ["A-04", "A-11"],
     "pilar": "R",
     "descripcion": "Supervisor marca RACS como cerrado → bot pide foto de evidencia → IA (YOLO + Gemini Vision) verifica que la condición fue corregida → si no convince, reabre el ticket automáticamente. Eleva ACC del 61 % al objetivo del 85 %.",
     "color": "#C8102E"},
    {"id": "LRAC-004", "modulo": "M1.B", "nombre": "Cápsula semanal + quiz adaptativo",
     "brecha": "NMAP 65.71 % (cuello de botella corporativo)",
     "stack": "n8n cron + DaVinci video gen + Gemini quiz + WhatsApp + Postgres",
     "metrica": "Apertura ≥70 % · aprobación quizz ≥80 %",
     "acciones": ["A-08", "A-10", "A-28"],
     "pilar": "A · C",
     "descripcion": "Cada lunes 7 am el bot envía a TODOS los trabajadores un video 90 s + 3 preguntas. Quien falla recibe cápsula remedial 24 h después; si vuelve a fallar 3 veces, notifica al supervisor. Ranking semanal por gerencia.",
     "color": "#C8102E"},
    # Visión computacional
    {"id": "LRAC-010", "modulo": "M1.A", "nombre": "Detección EPP en accesos (garita)",
     "brecha": "Cumplimiento Reglas para la Vida en ingreso",
     "stack": "ConstEdge (DeepFace + YOLOv8) + Jetson Orin Nano + n8n",
     "metrica": "EPP ≥99 % en acceso · alerta <30 s",
     "acciones": ["A-12"],
     "pilar": "L · R",
     "descripcion": "Cámara en torniquete → DeepFace identifica trabajador → YOLO valida casco+gafas+chaleco+barbijo según rol → si falta EPP, alerta supervisor por WhatsApp + bloquea torniquete + log auditable.",
     "color": "#FF7F0E"},
    {"id": "LRAC-011", "modulo": "M1.A", "nombre": "Detección EPP continua en obra",
     "brecha": "CCV humano por checklist · cobertura limitada",
     "stack": "Cámaras Tapo/Reolink + FastAPI + YOLOv8 + n8n",
     "metrica": "Cobertura EPP en obra ≥97 % · 38 FPS sostenidos",
     "acciones": ["A-12", "A-05"],
     "pilar": "R",
     "descripcion": "Cámaras IP en zonas críticas → frame cada 5 s → FastAPI YOLOv8 inference (87.67 % mAP) → si detecta incumplimiento + persona identificada → push WhatsApp al supervisor con foto blureada + ubicación + clase faltante. CCV continuo, no semanal.",
     "color": "#FF7F0E"},
    {"id": "LRAC-012", "modulo": "M1.A", "nombre": "Verificación visual de cierre (2do nivel)",
     "brecha": "Auditoría CCV humana · 5 % muestreo",
     "stack": "FastAPI + YOLO + ViT crack detection + n8n",
     "metrica": "5 % muestra mensual auditada por IA",
     "acciones": ["A-05"],
     "pilar": "R",
     "descripcion": "Sistema selecciona aleatoriamente 5 % de los CCV cerrados cada mes → procesa la foto de cierre con modelos visuales adecuados (EPP/cracks/objeto-removido) → genera reporte de discrepancias para auditoría externa. Extensión natural de LRAC-003.",
     "color": "#FF7F0E"},
    # GAIATECH VIGÍA
    {"id": "LRAC-020", "modulo": "M1.C", "nombre": "Monitoreo de vibración en presa de relaves",
     "brecha": "Cumplimiento DS 034-2023-EM art. 418 · Resolución 122-2024-OS/CD",
     "stack": "FPGA Gowin GW1NR-9 + ESP32 + LoRa + LSTM-Autoencoder PyTorch + n8n",
     "metrica": "F1 = 0.961 · alerta <2 s · reporte mensual OSINERGMIN auto",
     "acciones": ["A-13"],
     "pilar": "R",
     "descripcion": "FFT en FPGA sobre sensor de vibración 1 s → ESP32 transmite features por LoRa → LSTM-AE detecta anomalía → si score > umbral → WhatsApp a geotecnia + ticket auto + reporte mensual Anexo 43 OSINERGMIN. Tecnología que ganó 2.º AI Talent Demo Day 2026.",
     "color": "#2E7D32"},
    {"id": "LRAC-021", "modulo": "M1.C", "nombre": "Geofence 6-4-2 de liderazgo visible",
     "brecha": "Regla 6-4-2 no se mide · 3Q MEDIO AMBIENTE 39 %",
     "stack": "App PWA + GPS + Postgres + n8n cron + dashboard",
     "metrica": "≥95 % gerentes ≥2 h/día en zonas operativas",
     "acciones": ["A-03"],
     "pilar": "L",
     "descripcion": "PWA en el celular del gerente/superintendente/supervisor → GPS counter cuenta minutos en geofences operativos definidos → reporte diario 17:00 con horas en campo por persona → ranking público mensual. Convierte la regla 6-4-2 en métrica auditable, no en buena intención.",
     "color": "#2E7D32"},
    # Dashboard + reportes
    {"id": "LRAC-030", "modulo": "M1.D", "nombre": "Dashboard SHE — Single Pane of Glass",
     "brecha": "Convergencia VPs sin sistema dominante · falta de visibilidad ejecutiva",
     "stack": "Next.js 16 + Tailwind + Postgres + VPS Gen+ · login httpOnly · rol-based",
     "metrica": "≥90 % supervisores usando dashboard semanal",
     "acciones": ["A-14"],
     "pilar": "L · R · A · C",
     "descripcion": "Login rol-based: operario/supervisor/gerente/auditor → LRAC Health Score corporativo + drill-down VP→Gerencia→Mes → heatmap pilares en vivo + ranking dinámico + alertas sintéticas + reporte ejecutivo Gemini Pro. Plataforma Vision Pro PDK adaptada al dominio LRAC.",
     "color": "#1F77B4"},
    {"id": "LRAC-031", "modulo": "M1.D", "nombre": "Reporte semanal ejecutivo Gemini Pro",
     "brecha": "Análisis manual ocupa horas del equipo SHE",
     "stack": "n8n cron + Postgres + Gemini Pro + Gmail/Drive",
     "metrica": "Reporte de 1 página automático cada lunes 6 am",
     "acciones": ["A-06", "A-19"],
     "pilar": "L · A",
     "descripcion": "Cada lunes 6 am Gemini consume últimos 7 días de data LRAC + eventos + cumplimientos → genera narrativa ejecutiva de 1 página con top 3 patrones, recomendaciones y riesgos emergentes → envía a VPs y junta directiva. Reemplaza horas de analista.",
     "color": "#1F77B4"},
    {"id": "LRAC-032", "modulo": "M1.D", "nombre": "Auto-cumplimiento legal OSINERGMIN",
     "brecha": "Cumplimiento Resolución 122-2024-OS/CD · 5 días hábiles mensuales",
     "stack": "n8n + Postgres + PDFkit + firma digital + Ventanilla Virtual VVO",
     "metrica": "100 % reportes enviados en plazo · 0 multas",
     "acciones": ["A-13", "A-20"],
     "pilar": "R",
     "descripcion": "Cada 5 días hábiles bot agrupa data de monitoreo geotécnico (proveniente de M1.C) → genera PDF formato Anexo 1 → notifica al ingeniero geotécnico para firma digital → sube a Ventanilla Virtual VVO. Quita 8 h/mes de trabajo manual y elimina riesgo de multa.",
     "color": "#1F77B4"},
]

# ---------- VISTA RESUMEN ----------
st.markdown("### Resumen por módulo")
import pandas as pd
df = pd.DataFrame([
    {"Módulo": w["modulo"], "ID": w["id"], "Workflow": w["nombre"],
     "Pilar(es)": w["pilar"], "Acciones del plan": ", ".join(w["acciones"])}
    for w in WORKFLOWS
])
st.dataframe(df, use_container_width=True, hide_index=True, height=460)

st.divider()

# ---------- DETALLE POR WORKFLOW ----------
st.markdown("### Detalle técnico por workflow")
filtro_modulo = st.selectbox(
    "Filtrar por módulo GAIATECH M1.0",
    ["Todos", "M1.A · Visión EPP", "M1.B · Aecodito Minero", "M1.C · GAIATECH VIGÍA", "M1.D · Dashboard ejecutivo"],
)

mod_map = {
    "M1.A · Visión EPP": "M1.A",
    "M1.B · Aecodito Minero": "M1.B",
    "M1.C · GAIATECH VIGÍA": "M1.C",
    "M1.D · Dashboard ejecutivo": "M1.D",
}

flt = WORKFLOWS if filtro_modulo == "Todos" else [w for w in WORKFLOWS if w["modulo"] == mod_map[filtro_modulo]]

for w in flt:
    with st.expander(f"**{w['id']} · {w['nombre']}** · Módulo {w['modulo']}  ·  Pilares {w['pilar']}", expanded=False):
        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown(f"**🔥 Brecha que ataca:** {w['brecha']}")
            st.markdown(f"**🛠 Stack técnico:** `{w['stack']}`")
            st.markdown(f"**📐 Descripción:**")
            st.write(w["descripcion"])
        with c2:
            st.markdown(f"**📊 Métrica objetivo:**")
            st.info(w["metrica"])
            st.markdown(f"**📋 Acciones del plan:**")
            for a in w["acciones"]:
                st.markdown(f"- `{a}`")

st.divider()
st.markdown(
    """
    ### Estado actual del stack

    | Módulo | Componente | Estado |
    |---|---|---|
    | M1.A | Visión computacional EPP | **en producción** (Vision Pro PDK puerto 8088 VPS Gen+) |
    | M1.B | Aecodito Minero (n8n) | **en producción** (Aecodito v3.0, 50 nodos, 10 herramientas) |
    | M1.C | GAIATECH VIGÍA | **prototipo funcional** (2.º AI Talent Demo Day 2026) |
    | M1.D | Dashboard ejecutivo | **en producción** (Vision Pro PDK Next.js 16) |

    Para piloto en Las Bambas se requiere principalmente **integración con IEM corporativo**
    (workflow LRAC-031) y **reentrenamiento del modelo EPP con dataset Las Bambas específico**,
    no construcción desde cero.

    El detalle arquitectónico de cada workflow está en `docs/workflows/` del repositorio.
    """
)
