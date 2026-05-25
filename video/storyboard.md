# Storyboard · GAIATECH M1.0 video 90 s

> Cada frame es un mockup ASCII de lo que el espectador ve en pantalla. La paleta es negro `#0F0F10` + rojo MMG `#C8102E` + grises. Las cifras grandes son siempre legibles a 1080 p.

---

## Frame 0:00 – 0:02 · Black hook

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│                                                        │
│                                                        │
│                                                        │
│          LRAC global · MINA JUANITA S.A.              │
│                                                        │
│              ████████████                              │
│              ██  55.28 %  ██   ← rojo MMG              │
│              ████████████                              │
│                                                        │
│        4 500 trabajadores · 4 VPs · 12 gerencias       │
│                                                        │
│                                                        │
│                                                        │
└────────────────────────────────────────────────────────┘
                  Voiceover en sync
```

## Frame 0:05 – 0:08 · Transición al workflow

```
┌────────────────────────────────────────────────────────┐
│  WORKFLOW LRAC-001 · RACS GUIADO         M1.B TOKI │
│  ─────────────────────────────────────────────────────│
│                                                        │
│         Bot conversacional WhatsApp + n8n             │
│                                                        │
│                  ▼                                     │
│         50 nodos · 10 herramientas                     │
│                                                        │
└────────────────────────────────────────────────────────┘
```

## Frame 0:10 – 0:30 · Split screen TOKI

```
┌────────────────────────┬────────────────────────────────┐
│                        │ Workflow n8n vista canvas      │
│ 🟢 WhatsApp Operador    │                                │
│ ───────────             │   [WhatsApp Trigger]           │
│ Operador: RACS          │        │                       │
│                         │        ▼                       │
│ Bot: Hola Juan, mándame │   [Router multimedia]          │
│      primero una foto.  │        │                       │
│                         │   ┌────┴────┐                  │
│ 📷 [foto cinta planta]  │   │         │                  │
│                         │   ▼         ▼                  │
│ Bot: Recibido.          │ [Gemini Pro] [STT Whisper]     │
│      Confírmame ubica   │      │           │             │
│ 📍 [GPS en vivo]        │      └─────┬─────┘             │
│                         │            ▼                   │
│ 🎤 [nota de voz 15 s]   │   [Postgres pgvector]          │
│                         │            │                   │
│ Bot:                    │            ▼                   │
│ ✓ Clasificado:          │   [Push IEM API]               │
│ Condición sub-estándar  │            │                   │
│ Severidad: ALTA         │            ▼                   │
│ Fatal-risk: Equipo móvil│   [WhatsApp Notify Supervisor] │
│ RACS #2026-04823 creado │                                │
│ Supervisor notificado   │                                │
└────────────────────────┴────────────────────────────────┘
        Voiceover sincronizado con el flujo
        Texto inferior: "Stack: WhatsApp + n8n + Gemini Pro"
```

## Frame 0:35 – 0:55 · Visión EPP cuadrícula

```
┌────────────────────────┬────────────────────────────────┐
│ CAM-01 · Acceso garita │ Terminal FastAPI               │
│                        │                                │
│  ┌──[CASCO]──┐         │ [2026-05-21 14:23:01]          │
│  │  worker   │ ✓       │ POST /infer/epp 200 OK         │
│  └───────────┘         │ class: helmet → detected ✓     │
│                        │ class: vest   → detected ✓     │
│  ┌─░░░░░░░░─┐          │ class: glasses → MISSING ⚠     │
│  │ worker-2 │ ⚠        │ confidence: 0.92               │
│  └──────────┘          │ inference time: 26 ms          │
│  ⚠ FALTA EPP            │ throughput: 38 FPS             │
│                        │                                │
├────────────────────────┼────────────────────────────────┤
│ WhatsApp Supervisor    │ Métrica del modelo             │
│                        │                                │
│ 🔔 LRAC-011 ALERTA      │      mAP@0.5                   │
│                        │  ████████████████              │
│ Falta de gafas         │       87.67 %                  │
│ Zona: Garita Acceso A  │  ████████████████              │
│ Hace: 12 segundos      │                                │
│ Foto: [imagen blureada]│  Dataset: 14 055 imgs · Perú   │
│                        │  Plataforma: Jetson Orin Nano  │
└────────────────────────┴────────────────────────────────┘
        Voiceover narra el detalle técnico
        Texto inferior: "Stack: FastAPI · YOLOv8 · Jetson"
```

## Frame 1:00 – 1:18 · Dashboard ejecutivo

```
┌────────────────────────────────────────────────────────┐
│ LRAC HEALTH SCORE                              72 / 100│
├────────────────────────────────────────────────────────┤
│ Liderazgo (L)     ████████░░  68 %     ↑ +3 %          │
│ Riesgos (R)       ███████░░░  69 %     ↑ +1 %          │
│ Aprendizaje (A)   ██████░░░░  66 %     → 0 %    ← rojo │
│ Contratistas (C)  ███████░░░  69 %     ↑ +2 %          │
├────────────────────────────────────────────────────────┤
│ Top 3 patrones detectados (Gemini Pro):                │
│ 1. Falta de gafas en Garita A (8 detecciones esta sem.)│
│ 2. ACC en PROYECTOS-2 cayó 4 pp                        │
│ 3. NMAP plana: aún 65.71 % corporativo                 │
├────────────────────────────────────────────────────────┤
│ Ranking · 12 gerencias                                 │
│ ★ PROYECTOS 1 ─────────────████  75.12 %               │
│ ☆ PLANTA ──────────────────████  74.78 %               │
│ ...                                                    │
│ ▼ PROYECTOS 2 ──██████              62.31 %  ← rojo    │
│                                                        │
│   [Botón Drill-down]   [Botón Reporte semanal Gemini]  │
└────────────────────────────────────────────────────────┘
        Cámara hace pan vertical lento + zoom al ranking
```

## Frame 1:18 – 1:20 · Transición al simulador

```
┌────────────────────────────────────────────────────────┐
│   SIMULADOR DEL PLAN · 24 MESES                        │
│                                                        │
│   L ─────●──── 75 %        Proyección LRAC-4P          │
│   R ──────●─── 78 %                                    │
│   A ─────●──── 75 %        80 ────────────/──── meta   │
│   C ─────●──── 76 %        70 ────/──────────         │
│                            60 ─/                       │
│   ⚡  LRAC-4P proyectado:   M0   M8   M16  M24          │
│       76.5 %  (+7.3 pp)    base→meta12→meta24          │
└────────────────────────────────────────────────────────┘
```

## Frame 1:20 – 1:30 · Cierre

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│                                                        │
│              GAIATECH M1.0                             │
│        ──────────────────────                          │
│      4 módulos · 12 workflows · 31 acciones            │
│                                                        │
│        NPV S/ 1.21 M   ·   IRR 343 %                   │
│        Payback mes 11   ·   24 meses                   │
│                                                        │
│   📂 github.com/emanuelancco/lasbambas-lrac-2026       │
│   🌐 lasbambas-lrac-emanuel.streamlit.app              │
│                                                        │
│        Emanuel Edgar Ancco Guaygua                     │
│        Bach. Ing. Civil UPC · AI Automation gen+       │
│        🏆 2.º AI Talent Demo Day 2026                  │
│                                                        │
│        Innovadores en Acción 2026 · Caso 13 LRAC       │
└────────────────────────────────────────────────────────┘
        Fade a negro lento (1.5 s)
```

---

## Tipografía y reglas

- **Cifras (KPIs grandes):** font weight 800, tabular numbers, ≥48 pt.
- **Texto narrativo en pantalla:** weight 500, ≥24 pt, line-height 1.4.
- **Colores semánticos:**
  - Crítico / abajo de umbral: rojo MMG `#C8102E`
  - Advertencia: naranja `#FF7F0E`
  - Logrado / verde: `#2E7D32`
  - Información: azul `#1F77B4`
- **Sin emojis en frame del informe**; sí en el sub-stitch del video para anclar visualmente cada workflow.

## Notas de producción

- El bounding-box demo en escena 3 puede ser una grabación real del Vision Pro PDK en producción (VPS 187.77.250.111:3020) o, si hay restricciones de acceso, una grabación local del modelo corriendo sobre 10-15 imágenes del dataset peruano.
- La animación n8n del canvas se puede grabar con OBS Studio abriendo el bot TOKI existente en n8n self-hosted.
- El mockup de WhatsApp puede generarse rápido con WhatsApp Web + Stencil de Figma, o capturando una conversación real en un grupo de prueba.
- Render final: H.264, 1080 p 60 fps, bitrate 12 Mbps. Subir a YouTube como unlisted; el procesado tarda ~5-10 min.
