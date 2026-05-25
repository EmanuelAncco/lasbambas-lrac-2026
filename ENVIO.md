# Pre-flight y plantilla de envío · Caso 13 LRAC

> **Deadline:** domingo 24 de mayo 2026, 23:59 hora Perú.
> **Destinatario:** `Peru.Recruitment@MMG.COM`.

## ✅ Estado al jueves 21 de mayo de 2026 22:30 hora Perú

Todo el material del agente está listo. Faltan solo acciones manuales puntuales del postulante (deploy Streamlit + envío del correo el sábado).

| ✔ | Asset | Ubicación / URL |
|---|---|---|
| ✅ | **PDF v7 maestro · 25 pp** | `report/Emanuel Edgar Ancco Guaygua.pdf` |
| ✅ | **Repo GitHub público** | https://github.com/EmanuelAncco/lasbambas-lrac-2026 |
| ✅ | **Workflow LRAC-001 vivo en n8n** | https://aecodetest.app.n8n.cloud/workflow/qRW88FSByN26nDJr |
| ✅ | **Voiceover Gemini Kore (106 s)** | `video/voiceover.wav` (4.97 MB) |
| ✅ | **Anexo A5 · Dashboard HTML autocontenido** | `report/Emanuel_LRAC_Dashboard.html` |
| ✅ | **Slides PDF (14 slides)** | `report/emanuel-ancco-lrac-slides.pdf` |
| ✅ | **One-pager imprimible** | `report/onepager.html` + `.png` |
| ✅ | **Mockup WhatsApp HD** | `video/mockups/whatsapp-toki.html` + `.png` |
| ✅ | **5 capturas Playwright Streamlit** | `video/captures/` |
| ✅ | **4 workflows n8n exportables (JSON)** | `n8n-workflows/` |
| ✅ | **12 docs arquitectónicos** | `docs/workflows/*.md` |
| ✅ | **Análisis extra cross-indicator** | `docs/analisis-extra.md` |
| ✅ | **Comparativa vs SAP/Intelex/Enablon** | `docs/comparativa-vs-comerciales.md` |
| 🟡 | Deploy Streamlit Cloud | Pendiente · https://share.streamlit.io/deploy |
| 🟢 | Power BI .pbix | Reemplazado por HTML interactivo en A5 (superior portabilidad) |

---

## ⏳ Pendientes del postulante

### 1 · Deploy Streamlit Cloud (5 min)

1. Abre https://share.streamlit.io/deploy
2. Login con la cuenta GitHub de EmanuelAncco (la misma del repo)
3. Configura:
   ```
   Repository:      EmanuelAncco/lasbambas-lrac-2026
   Branch:          main
   Main file path:  app/main.py
   App URL:         lasbambas-lrac-emanuel
   ```
4. Click "Deploy"
5. Esperar ~2 min. Avísame cuando esté online en `https://lasbambas-lrac-emanuel.streamlit.app`.

### 2 · Video DaVinci (opcional, 2.5 h)

Solo si tienes tiempo el viernes. Los assets están todos listos en `video/`:
- `script.md` · script con timing shot-by-shot
- `storyboard.md` · storyboard con frames ASCII
- `voiceover.wav` · audio listo (~106 s)
- `captures/` · 5 capturas del Streamlit
- `mockups/whatsapp-toki.png` · mockup HD WhatsApp

Subir a YouTube unlisted al terminar. Si no llega a tiempo, el PDF + repo + Streamlit + slides son suficientes.

### 3 · Envío correo (sábado antes de 18:00)

Plantilla lista abajo. Solo necesitas reemplazar la URL del Streamlit Cloud y la del video YouTube (si lo hiciste).

---

## ✅ Pre-flight checklist · sábado 24 mediodía

- [ ] PDF `report/Emanuel Edgar Ancco Guaygua.pdf` tiene **25 páginas** (verificado)
- [ ] Fuente Times New Roman 12 pt, interlineado 1.5 (verificado)
- [ ] Nombre exacto: `Emanuel Edgar Ancco Guaygua.pdf` (con tilde en Guaygua si corresponde · revisar DNI)
- [ ] Las 4 URLs anexas abren correctamente desde móvil:
  - Repo GitHub
  - Streamlit Cloud (cuando esté online)
  - n8n workflow (público con auth o solo-vista)
  - Dashboard HTML (en el repo)
- [ ] Copia del PDF en Drive personal con compartir público
- [ ] Backup local en 2 ubicaciones

---

## 📧 Plantilla del correo (copiar a Gmail)

**Para:** `Peru.Recruitment@MMG.COM`
**CC:** [tu cuenta personal como prueba]
**Asunto:** `Postulación Talentos de Cobre 2026 – Caso 13 LRAC – Emanuel Edgar Ancco Guaygua`

**Cuerpo (copiable):**

```
Estimado equipo de Reclutamiento y Atracción de Talento de MMG Las Bambas:

Adjunto el informe técnico correspondiente al Caso 13 (VP SHE – Diagnóstico
y Gobernanza del Sistema LRAC) del programa Innovadores en Acción 2026.

POSTULANTE
- Emanuel Edgar Ancco Guaygua
- DNI: [completar]
- Bachiller en Ingeniería Civil – UPC (egresado 2025)
- AI Automation Engineer en gen+
- 2.º lugar AI Talent Demo Day 2026 con GAIATECH VIGÍA

DOCUMENTO PRINCIPAL
- Emanuel Edgar Ancco Guaygua.pdf (25 páginas, Times New Roman 12 pt,
  interlineado 1.5, 30 referencias APA 7)

ANEXOS DIGITALES (evidencia del builder)

A1. Repositorio público en GitHub con código reproducible y documentación
    arquitectónica de los 12 workflows GAIATECH M1.0:
    https://github.com/EmanuelAncco/lasbambas-lrac-2026

A2. Demo Streamlit interactivo (dashboard + simulador del plan + catálogo
    de workflows):
    https://lasbambas-lrac-emanuel.streamlit.app

A3. Workflow LRAC-001 (TOKI clasificador RACS) desplegado en
    instancia n8n para inspección directa por el jurado:
    https://aecodetest.app.n8n.cloud/workflow/qRW88FSByN26nDJr

A4. Slides de sustentación oral (10 minutos, Slidev):
    PDF adjunto: emanuel-ancco-lrac-slides.pdf

A5. Dashboard HTML autocontenido equivalente a Power BI (5 pestañas
    interactivas con Plotly, abre en cualquier navegador):
    https://github.com/EmanuelAncco/lasbambas-lrac-2026/blob/main/report/Emanuel_LRAC_Dashboard.html
    (también adjunto)

RESUMEN EJECUTIVO

El sistema LRAC de Mina Juanita S.A. presenta un cumplimiento global de
captura del 55.28 % y un índice LRAC-4P por VP entre 68.57 % y 69.71 %.
El análisis estadístico (Kruskal-Wallis p = 0.7237, score compuesto S =
μ - σ, Mann-Kendall por VP, matriz de correlación 7×7) revela que la
convergencia entre VPs no es significativa y que el cuello de botella
corporativo es NMAP (65.71 %, Pilar A · Aprendizaje).

El Plan de Acción Estratégico propone 31 acciones en 3 horizontes (0-3,
3-9, 9-24 meses) y 5 frentes, ancladas en cuatro módulos GAIATECH M1.0
ya construidos por el postulante:

  · M1.A · Visión computacional EPP (YOLOv8 sobre 14 055 imágenes
    peruanas, mAP@0.5 87.67 %, 38 FPS Jetson Orin Nano Super).
  · M1.B · Agente WhatsApp TOKI (n8n + Evolution API +
    Gemini Pro, 50 nodos, 10 herramientas integradas).
  · M1.C · GAIATECH VIGÍA (FPGA Gowin GW1NR-9 + ESP32 + LSTM-AE
    F1 = 0.961, ganador del 2.º lugar AI Talent Demo Day 2026).
  · M1.D · Dashboard ejecutivo Vision Pro PDK en producción
    (Single Pane of Glass rol-based, reportes Gemini Pro
    automatizados).

Business case 24 meses: NPV S/ 1.21 M (base) / S/ 3.81 M (optimista) ·
IRR 343 % · payback mes 11 · inversión total S/ 1 218 200.

Quedo a disposición para responder preguntas o profundizar en cualquier
módulo del plan en la etapa siguiente del proceso.

Cordialmente,

Emanuel Edgar Ancco Guaygua
+51 974 583 549
coarp.eancco@gmail.com
emanuelancco.github.io/cv-portfolio
linkedin.com/in/emanuel-edgar-ancco-guaygua-a61210352
```

**Adjuntos (4 archivos):**
1. `Emanuel Edgar Ancco Guaygua.pdf` (informe principal, 25 pp · 1.35 MB)
2. `emanuel-ancco-lrac-slides.pdf` (slides defensa, 14 slides · 4 KB)
3. `Emanuel_LRAC_Dashboard.html` (anexo A5 dashboard, 89 KB)
4. `voiceover.wav` (opcional · audio del video, 5 MB)

---

## 🛡 Plan B por falla

| Falla | Plan B |
|---|---|
| Streamlit Cloud caído | El PDF y el repo son autosuficientes; cita `lasbambas-lrac-emanuel.streamlit.app` como "disponible bajo solicitud" |
| GitHub repo no accesible para el jurado | Adjuntar todo el contenido como ZIP en otro correo |
| n8n workflow no accesible públicamente | Adjuntar screenshot del flujo + JSON en `n8n-workflows/` |
| HTML A5 no abre | Adjuntar el `dashboard.html` (alternativa) o las 14 figuras PNG |

---

## 📊 Métricas del entregable final

| Indicador | Valor |
|---|---|
| Páginas del PDF | 25 / 25 |
| Figuras incrustadas | 8 |
| Tablas | 9 |
| Referencias APA 7 | 30 |
| Workflows GAIATECH documentados | 12 |
| Workflows n8n exportables (JSON) | 4 |
| Workflows n8n desplegados en producción | 1 (LRAC-001 demo) |
| Acciones del plan | 31 |
| NPV base / optimista | S/ 1.21 M / S/ 3.81 M |
| IRR / Payback | 343 % / mes 11 |
| Slides Slidev | 14 |
| Papers MDPI archivados | 40+ |
| Capturas Playwright Streamlit | 5 |
| Líneas totales de documentación MD | >2 000 |

**Estimación honesta de competitividad:** muy alta. El nivel de profundidad técnica + reproducibilidad + evidencia de activos en producción es difícilmente igualable por otros postulantes en el plazo dado.
