---
titulo: GAIATECH M1.0 — del diagnóstico al despliegue
duracion: 90 segundos
voz: Gemini TTS · Kore (femenina profunda)
formato_destino: 1920×1080 60 fps · YouTube unlisted
caso: Innovadores en Acción 2026 · MMG Las Bambas · Caso 13 LRAC
postulante: Emanuel Edgar Ancco Guaygua
fecha: 2026-05-21
---

# Script del video 90 s · GAIATECH M1.0

> **Mensaje único:** Mina Juanita S.A. tiene un LRAC al 55 %. El plan no se arregla con más formatos en papel — se arregla con cuatro módulos digitales que ya están construidos, en producción y miden por sí solos.

> **Estructura:** 5 escenas. Hook (5 s) · M1.B Aecodito (30 s) · M1.A Visión EPP (25 s) · M1.D Dashboard (20 s) · Cierre (10 s).

---

## Escena 1 · Hook ⏱ 0:00 – 0:05

**Voiceover (12 palabras, ~5 s):**
> "El sistema LRAC de Mina Juanita cayó al cincuenta y cinco por ciento. Más formatos no lo arreglan."

**Visual:**
- Fade desde negro.
- Texto en pantalla grande sobre fondo oscuro:
  ```
  LRAC global · 55.28 %
  4 500 trabajadores
  4 VPs · 12 gerencias
  ```
- Subraya el 55.28 % con un trazo rojo MMG `#C8102E`.
- Cierre: aparece el logo o ID del autor abajo a la izquierda en pequeño.

**Transición:** corte rápido a la captura del informe abierto (1 frame del PDF) → fade al Streamlit.

---

## Escena 2 · M1.B · Aecodito Minero captura un RACS ⏱ 0:05 – 0:35

**Voiceover (~30 s · 85 palabras):**
> "Workflow LRAC cero cero uno. Aecodito Minero es un bot de WhatsApp con cincuenta nodos en n8n. El operador escribe ‘RACS’ desde la planta. El bot pide una foto. Captura GPS automático. Recibe la descripción en texto o nota de voz. Gemini Pro clasifica acto o condición sub-estándar, severidad, y el fatal-risk asociado. En menos de quince segundos el reporte está en la base con embedding, el supervisor recibe la alerta, y el operador tiene número de ticket. La fricción del formato en papel desaparece."

**Visual (split-screen):**
- **Izquierda (60 %):** mockup animado de conversación WhatsApp con timestamps reales:
  ```
  Operador: RACS
  Bot:     Hola Juan, te ayudo. Mándame primero una foto.
  Operador: [📷 foto cinta transportadora]
  Bot:     Recibido. Confírmame la ubicación.
  Operador: [📍 envió ubicación en vivo]
  Bot:     Cuéntame qué viste (texto o voz).
  Operador: 🎤 [nota de voz 15 s]
  Bot:     ✓ Clasificado: Condición sub-estándar · Severidad ALTA
           Fatal-risk relacionado: Equipo móvil
           RACS #2026-04823 creado. Supervisor notificado.
  ```
- **Derecha (40 %):** vista del workflow n8n con nodos iluminándose en secuencia (trigger WhatsApp → router multimedia → Gemini Pro → Postgres → IEM push → confirmación).
- Texto inferior pequeño: "Stack: WhatsApp Business + Evolution API + n8n + Gemini Pro + Postgres pgvector"

**Transición:** zoom out, ambas mitades se contraen y dan paso a la pantalla de visión computacional.

---

## Escena 3 · M1.A · Visión computacional EPP ⏱ 0:35 – 1:00

**Voiceover (~25 s · 70 palabras):**
> "Workflow LRAC cero once. La verificación de controles críticos deja de ser un checklist humano. Cámaras IP en zonas críticas alimentan un YOLOv8 con ochenta y siete punto seis-siete por ciento de mAP, entrenado en catorce mil cincuenta y cinco imágenes peruanas. Treinta y ocho FPS sostenidos en Jetson Orin. Si detecta falta de EPP, el supervisor recibe la alerta con foto y ubicación en menos de treinta segundos. CCV continuo, no semanal."

**Visual:**
- Plano cuadrícula 2×2:
  - Cuadrante superior izquierdo: feed de cámara real con bounding boxes verdes/rojos detectando casco, chaleco, gafas. Una persona aparece sin casco → caja roja parpadea + sonido sutil de alerta.
  - Cuadrante superior derecho: terminal corriendo FastAPI mostrando logs de inferencia (`/infer/epp` 200 OK · 38 FPS · class: helmet missing · conf: 0.92`).
  - Cuadrante inferior izquierdo: WhatsApp del supervisor recibe la alerta con la foto.
  - Cuadrante inferior derecho: gráfico de barras con métrica `mAP@0.5 = 87.67 %` destacado en rojo MMG.
- Texto sobreimpreso: "Stack: FastAPI · YOLOv8 · Jetson Orin Nano Super · n8n"

**Transición:** los cuatro cuadrantes se fusionan en una sola pantalla → fade a dashboard.

---

## Escena 4 · M1.D · Dashboard ejecutivo Single Pane of Glass ⏱ 1:00 – 1:20

**Voiceover (~20 s · 55 palabras):**
> "Workflow LRAC cero treinta. Un solo dashboard rol-based muestra el LRAC Health Score, drill-down de Vicepresidencia a Gerencia, heatmap por pilar y ranking dinámico. El VP SHE abre el panel el lunes a las siete y entiende el estado en treinta segundos. Cada lunes a las seis, Gemini Pro genera el reporte ejecutivo automático."

**Visual:**
- Captura completa del Streamlit dashboard interactivo (file `02-dashboard.png` + `05-dashboard-html.png`).
- Movimiento de cámara: pan vertical lento, luego zoom suave al ranking de las 12 gerencias.
- Anotaciones flotantes:
  - "LRAC-4P 69.17 %" con flecha al KPI card
  - "12 gerencias · drill-down" con flecha al ranking horizontal
  - "PROYECTOS 1: 75.12 %" y "PROYECTOS 2: 62.31 %" subrayados (brecha intra-VP)
- Transición al simulador (3 s): muestra los sliders L/R/A/C moviéndose → línea de trayectoria de 24 meses crece hasta 80 %.

---

## Escena 5 · Cierre ⏱ 1:20 – 1:30

**Voiceover (~10 s · 28 palabras):**
> "Cuatro módulos. Doce workflows. Treinta y un acciones. NPV un punto dos millones de soles, payback mes once. No es PowerPoint: el repositorio está abierto."

**Visual:**
- Pantalla negra con texto blanco centrado:
  ```
  GAIATECH M1.0
  · 4 módulos · 12 workflows · 31 acciones
  ·
  NPV S/ 1.21 M  ·  IRR 343 %  ·  Payback mes 11
  ·
  github.com/emanuelancco/lasbambas-lrac-2026
  lasbambas-lrac-emanuel.streamlit.app
  ·
  Emanuel Edgar Ancco Guaygua
  Innovadores en Acción 2026 · MMG Las Bambas · Caso 13 LRAC
  ```
- Logo o ID inferior derecho: 🏆 2.º AI Talent Demo Day 2026.
- Fade a negro.

---

## Plan de producción en DaVinci Resolve

### Assets requeridos
| # | Asset | Tipo | Ruta |
|---|---|---|---|
| 1 | `01-landing.png` | Captura Streamlit landing | `video/captures/` |
| 2 | `02-dashboard.png` | Captura Dashboard interactivo | `video/captures/` |
| 3 | `03-simulador.png` | Captura Simulador | `video/captures/` |
| 4 | `04-workflows.png` | Captura Catálogo workflows | `video/captures/` |
| 5 | `05-dashboard-html.png` | Dashboard HTML standalone | `video/captures/` |
| 6 | `voiceover.wav` | Voz Kore Gemini TTS | `video/audio/` (a generar) |
| 7 | Mockup WhatsApp conversación | A diseñar (Figma o Canva) | `video/mockups/` |
| 8 | Loop de cámara EPP con bbox | Captura del Vision Pro PDK real | `video/footage/` |
| 9 | Música ambient minimal | Royalty-free de YouTube Audio Library | `video/music/` |
| 10 | Logo GAIATECH + branding MMG | PNG transparente | `video/branding/` |

### Timeline DaVinci (90 s a 60 fps = 5 400 frames)

```
00:00 – 00:05  Escena 1 · Hook                  Bin: Intro
00:05 – 00:35  Escena 2 · Aecodito Minero       Bin: M1.B
00:35 – 01:00  Escena 3 · Visión EPP             Bin: M1.A
01:00 – 01:20  Escena 4 · Dashboard ejecutivo    Bin: M1.D
01:20 – 01:30  Escena 5 · Cierre                 Bin: Outro
```

### Pista de audio
- **A1:** Voiceover Kore (mezcla -6 dB)
- **A2:** Música ambient (mezcla -22 dB, ducking durante voz)
- **A3:** SFX puntuales (alerta WhatsApp ~ -16 dB, "OK" check)

### Estilo visual
- Paleta: Negro `#0F0F10` · rojo MMG `#C8102E` · gris claro `#E8E8EA` · acento naranja `#FF7F0E`.
- Tipografía: Inter o Helvetica para texto en pantalla; tabular numbers para cifras.
- Transiciones: solo cortes secos o cross-dissolve corto (200 ms). Sin Star Wipe ni transiciones cliché.
- Bounding boxes EPP: stroke 4 px, esquinas redondeadas 2 px, color por clase.

### Música sugerida (royalty-free)
- "Document" — Aakash Gandhi (ambient minimal cinematic)
- "Slow Burn" — Kevin MacLeod (cinematic suspense → resolution)
- Buscar en YouTube Audio Library categoría "Cinematic > Calm" o "Inspirational > Slow".

---

## Métricas de éxito del video

| KPI | Meta |
|---|---|
| Duración | 90 s ± 2 s |
| Watch time medio | ≥ 80 % |
| Voz a ritmo de 175 ppm (palabras por minuto) | OK con script ~260 palabras |
| Legibilidad de texto en pantalla | mínimo 24 pt en 1080 p |
| URL del repo + Streamlit visible en cierre | ≥ 3 segundos |

---

## Voiceover completo para Gemini TTS Kore

Texto exacto que se enviará al TTS (260 palabras, 90 s a 175 ppm):

```
El sistema LRAC de Mina Juanita cayó al cincuenta y cinco por ciento. Más formatos no lo arreglan.

Workflow LRAC cero cero uno. Aecodito Minero es un bot de WhatsApp con cincuenta nodos en n ocho n. El operador escribe ‘RACS’ desde la planta. El bot pide una foto. Captura GPS automático. Recibe la descripción en texto o nota de voz. Gemini Pro clasifica acto o condición sub-estándar, severidad, y el fatal-risk asociado. En menos de quince segundos el reporte está en la base con embedding, el supervisor recibe la alerta, y el operador tiene número de ticket. La fricción del formato en papel desaparece.

Workflow LRAC cero once. La verificación de controles críticos deja de ser un checklist humano. Cámaras IP en zonas críticas alimentan un YOLO versión ocho con ochenta y siete punto seis-siete por ciento de mAP, entrenado en catorce mil cincuenta y cinco imágenes peruanas. Treinta y ocho FPS sostenidos en Jetson Orin. Si detecta falta de EPP, el supervisor recibe la alerta con foto y ubicación en menos de treinta segundos. CCV continuo, no semanal.

Workflow LRAC cero treinta. Un solo dashboard rol-based muestra el LRAC Health Score, drill-down de Vicepresidencia a Gerencia, heatmap por pilar y ranking dinámico. El VP SHE abre el panel el lunes a las siete y entiende el estado en treinta segundos. Cada lunes a las seis, Gemini Pro genera el reporte ejecutivo automático.

Cuatro módulos. Doce workflows. Treinta y un acciones. NPV un punto dos millones de soles, payback mes once. No es PowerPoint: el repositorio está abierto.
```
