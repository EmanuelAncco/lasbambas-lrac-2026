# Pre-flight checklist y plantilla del envío

> **Deadline:** domingo 24 de mayo 2026, 23:59 hora Perú.
> **Destinatario:** `Peru.Recruitment@MMG.COM`.
> **Asunto sugerido:** `Postulación Talentos de Cobre 2026 – Caso 13 LRAC – Emanuel Edgar Ancco Guaygua`.

## ✅ Pre-flight checklist (sábado 24 mediodía)

### Documento principal (obligatorio)
- [ ] PDF `Emanuel Edgar Ancco Guaygua.pdf` tiene **exactamente 25 páginas o menos**
- [ ] Fuente: **Times New Roman 12 pt** (verificado en propiedades del PDF)
- [ ] Interlineado: **1.5** (verificado visualmente)
- [ ] Nombre exacto del archivo: **`Emanuel Edgar Ancco Guaygua.pdf`** (con tilde en Guaygua si la tuviera el nombre legal · revisar DNI)
- [ ] PDF abre correctamente en Adobe Reader, Foxit y Microsoft Edge
- [ ] Bibliografía Sección 9 incluye 30 referencias en formato APA 7

### Anexos digitales (opcionales pero diferenciadores)
- [ ] **A1 · Repo GitHub** público y badge CI verde: <https://github.com/emanuelancco/lasbambas-lrac-2026>
- [ ] **A2 · Streamlit demo** responde HTTP 200 desde móvil y PC: <https://lasbambas-lrac-emanuel.streamlit.app>
- [ ] **A3 · Video YouTube** unlisted reproducible (cuenta diferente probó la URL)
- [ ] **A4 · Slides Slidev** HTML público + PDF descargable
- [ ] **A5 · Power BI .pbix** adjunto al correo + enlace Drive público

### Respaldo y verificación
- [ ] Copia del PDF en Google Drive personal (compartir público con enlace)
- [ ] Copia local en al menos 2 ubicaciones (PC + nube)
- [ ] Las 5 URLs probadas en navegador limpio sin cache (incógnito)
- [ ] BCC al envío incluye una cuenta personal del autor como prueba

### Estética y rigor
- [ ] Spell-check en español peruano completado (tildes, ñ, sin anglicismos forzados)
- [ ] Números cruzados entre cuerpo del informe y tablas (sin desfases)
- [ ] Citas APA 7 con DOI o URL verificable
- [ ] Sin emojis dentro del PDF (los emojis en pantalla del Streamlit no migran)

---

## Plantilla del correo (copiar y pegar a Gmail)

**Para:** `Peru.Recruitment@MMG.COM`
**CC:** [una cuenta personal del autor]
**Asunto:** `Postulación Talentos de Cobre 2026 – Caso 13 LRAC – Emanuel Edgar Ancco Guaygua`

```
Estimado equipo de Reclutamiento y Atracción de Talento de MMG Las Bambas:

Adjunto el informe técnico correspondiente al Caso 13 (VP SHE – Diagnóstico
y Gobernanza del Sistema LRAC) del programa Innovadores en Acción 2026.

POSTULANTE
- Emanuel Edgar Ancco Guaygua
- DNI: [completar]
- Bachiller en Ingeniería Civil – UPC
- AI Automation Engineer en gen+
- 2.º lugar AI Talent Demo Day 2026 con GAIATECH VIGÍA

DOCUMENTO PRINCIPAL
- Emanuel Edgar Ancco Guaygua.pdf  (25 páginas, Times New Roman 12 pt,
  interlineado 1.5, 30 referencias APA 7)

ANEXOS DIGITALES (evidencia del builder)
1. Repositorio GitHub público con código reproducible y documentación
   arquitectónica de los 12 workflows GAIATECH M1.0:
   https://github.com/emanuelancco/lasbambas-lrac-2026

2. Demo Streamlit interactivo (dashboard + simulador del plan + catálogo
   de workflows):
   https://lasbambas-lrac-emanuel.streamlit.app

3. Video 90 segundos GAIATECH M1.0 (YouTube unlisted):
   [URL]

4. Slides de sustentación oral (10 minutos · Slidev):
   [URL HTML] · PDF adjunto: emanuel-ancco-lrac-slides.pdf

5. Archivo Power BI con modelo tabular y medidas DAX:
   [adjunto: Emanuel_LRAC_Dashboard.pbix]

RESUMEN EJECUTIVO

El sistema LRAC de Mina Juanita S.A. presenta un cumplimiento global de
captura del 55.28 % y un índice LRAC-4P por VP entre 68.57 % y 69.71 %.
El análisis estadístico (Kruskal-Wallis p = 0.7237, score compuesto S =
mu - sigma, Mann-Kendall por VP, matriz de correlación 7×7) revela que
la convergencia entre VPs no es significativa y que el cuello de botella
corporativo es NMAP (65.71 %, Pilar A).

El Plan de Acción Estratégico propone 31 acciones en 3 horizontes (0–3,
3–9, 9–24 meses) y 5 frentes, ancladas en cuatro módulos GAIATECH M1.0
ya construidos por el postulante: visión computacional EPP (YOLOv8 sobre
14 055 imágenes peruanas, mAP 87.67 %), agente WhatsApp Aecodito Minero
(n8n + Gemini Pro, 50 nodos), monitoreo estructural con FPGA Gowin
(LSTM-AE F1 = 0.961) y dashboard ejecutivo Vision Pro PDK en producción.

Business case 24 meses: NPV S/ 1.21 M (base) / S/ 3.81 M (optimista) ·
IRR 343 % · payback mes 11 · inversión total S/ 1 218 200.

Quedo a disposición para responder preguntas o profundizar en cualquier
módulo del plan en la etapa siguiente del proceso.

Cordialmente,

Emanuel Edgar Ancco Guaygua
+51 974 583 549
coarp.eancco@gmail.com
emanuelancco.github.io/cv-portfolio
LinkedIn: linkedin.com/in/emanuel-edgar-ancco-guaygua-a61210352
```

---

## Verificación final pre-envío (ritual sábado 24 mayo)

**07:00** — Última revisión visual del PDF v4 (paginación, links activos).
**08:00** — Push final a GitHub (si quedó algo pendiente).
**09:00** — Confirmar Streamlit Cloud responde desde móvil (Android Chrome) y PC distinto.
**10:00** — Probar URLs anexas desde navegador en incógnito.
**11:00** — Redactar correo con la plantilla arriba.
**12:00** — Adjuntar PDF + .pbix + slides PDF.
**14:00** — Enviar correo a `Peru.Recruitment@MMG.COM` (con BCC a cuenta personal).
**14:01** — Verificar que llegó el BCC.
**14:30** — Captura del correo enviado como evidencia (archivar en Drive).

> **Margen:** 9.5 horas de buffer antes del cierre 23:59. Suficiente para resolver cualquier imprevisto.

---

## Si algo falla

| Falla | Plan B |
|---|---|
| Streamlit Cloud caído | Backup en VPS Gen+ (subdominio `lasbambas-lrac.187-77-250-111.nip.io`) |
| YouTube tarda en procesar video | Subir el viernes 23 a más tardar 22:00; fallback Vimeo |
| GitHub Actions rojo | Quitar referencia al badge CI del README; subir build artifacts manuales |
| Streamlit deploy falla | Mantener URL del backup VPS Gen+ en el PDF |
| PDF excede 25 páginas tras último cambio | Restaurar v3 desde git history; revertir cambio que pasó el límite |
| MMG bloquea links externos por seguridad | El PDF es 100 % autosuficiente; los anexos son refuerzo, no dependencia |

---

## Métricas del informe terminado

| Indicador | Valor |
|---|---|
| Páginas del PDF | 25 / 25 |
| Figuras incrustadas | 8 |
| Tablas | 9 |
| Referencias APA 7 | 30 |
| Workflows documentados (anexo arquitectónico) | 12 |
| Acciones del plan | 31 |
| Horizontes | 3 (0–3, 3–9, 9–24 meses) |
| Inversión total proyectada | S/ 1 218 200 |
| NPV base / optimista | S/ 1.21 M / S/ 3.81 M |
| IRR | 343 % |
| Payback (escenario base) | Mes 11 |
| Capturas Playwright del Streamlit | 5 |
| Slides Slidev | 14 |

Listo para entregar.
