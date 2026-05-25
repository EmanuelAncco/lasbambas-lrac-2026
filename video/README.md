# Video GAIATECH M1.0 · 90 segundos

Demo audiovisual para sustentar la propuesta del informe Innovadores en Acción 2026 · Caso 13 LRAC.

## Contenido del directorio

```
video/
├── README.md                  ← este archivo
├── script.md                  ← script narrativo + plan de producción DaVinci
├── storyboard.md              ← storyboard frame por frame con mockups ASCII
├── voiceover.txt              ← texto exacto del voiceover (260 palabras · 90 s)
├── generate_voiceover.py      ← script Python para generar voz Kore con Gemini TTS
├── captures/                  ← capturas Playwright del Streamlit (5 PNG)
│   ├── 01-landing.png
│   ├── 02-dashboard.png
│   ├── 03-simulador.png
│   ├── 04-workflows.png
│   └── 05-dashboard-html.png
└── (a producir)
    ├── audio/voiceover.wav    ← generado con generate_voiceover.py
    ├── footage/               ← grabaciones reales del Vision Pro PDK y n8n
    ├── mockups/               ← mockups WhatsApp en Figma
    ├── music/                 ← música ambient royalty-free
    └── final.mp4              ← export final desde DaVinci Resolve
```

## Pasos para producir el video

### 1) Generar el voiceover (5 minutos)

```powershell
# Activar el venv del proyecto (o gaiatech)
conda activate gaiatech     # o tu venv preferido

# Instalar la SDK si aún no la tienes
pip install google-genai

# Exportar la API key
$env:GEMINI_API_KEY = "<tu-clave-google-ai-studio>"

# Generar
cd "c:\Users\Emanuel\.gemini\antigravity\scratch\n8n\lasbambas-lrac-2026\video"
python generate_voiceover.py
```

Salida: `voiceover.wav` (~2 MB, ~90 s, voz Kore femenina profunda).

> **Tip:** si la primera generación suena demasiado lenta o rápida, ajustar el espaciado/puntuación en `voiceover.txt` y regenerar. Gemini TTS interpreta puntos = pausa corta, dos puntos seguidos = pausa media.

### 2) Capturar el material faltante

| Asset | Cómo obtenerlo | Tiempo |
|---|---|---|
| Conversación WhatsApp Aecodito | Abrir un chat real en un grupo de prueba con el bot y grabar con OBS Studio | 10 min |
| n8n canvas animado | Abrir el workflow LRAC-001 en n8n self-hosted, grabar con OBS pasando el cursor por los nodos en orden | 10 min |
| Bounding boxes EPP | Cargar 10 fotos peruanas en Vision Pro PDK, grabar las detecciones | 15 min |
| Música ambient | YouTube Audio Library · categoría "Cinematic > Calm" | 5 min |

### 3) Ensamblar en DaVinci Resolve

1. Crear proyecto 1080 p 60 fps, espacio Rec.709.
2. Importar todos los assets a bins (Intro, M1.B, M1.A, M1.D, Outro).
3. Construir el timeline siguiendo `script.md` (timing exacto en cada escena).
4. Pista A1 = voiceover.wav; A2 = música -22 dB con ducking; A3 = SFX puntuales.
5. Aplicar transiciones suaves (cross-dissolve 200 ms entre escenas).
6. Color grading: Rec.709, contraste medio, saturación +5 %, paleta MMG.
7. Render H.264, 12 Mbps, formato MP4.

### 4) Subir a YouTube unlisted

1. youtube.com → Upload.
2. Visibilidad: **Unlisted** (no público, accesible por URL).
3. Título: "GAIATECH M1.0 · LRAC Mina Juanita · Innovadores en Acción 2026"
4. Descripción: copiar el resumen ejecutivo del informe + link al repo + link al Streamlit.
5. Capítulos en la descripción (YouTube los detecta):
   ```
   00:00 Diagnóstico
   00:05 Aecodito Minero (M1.B)
   00:35 Visión EPP (M1.A)
   01:00 Dashboard ejecutivo (M1.D)
   01:20 Cierre
   ```
6. Copiar la URL unlisted y pegarla en el PDF maestro (Sección 8 · Anexo A3).

## Tiempos estimados

| Tarea | Tiempo |
|---|---|
| Generar voiceover | 5 min |
| Capturar material faltante | 40 min |
| Ensamblar en DaVinci | 90 min |
| Render + subir YouTube | 15 min |
| **Total** | **~2.5 horas** |

## Backup

Si DaVinci Resolve no está disponible o el render falla, alternativas más rápidas:
- **CapCut Desktop** (gratuito, importa los PNG + audio, ensambla en 30 min).
- **OBS Studio + ScreenStudio**: para grabaciones de pantalla con zoom-pan automático.
- **Canva Pro Video Editor**: genera intro/outro con plantillas tipo Awwwards.

## Referencias

- Memoria del autor `project_gaiatech_video_recap.md` documenta el flujo DaVinci ya probado para el video del 2.º lugar AI Talent Demo Day 2026.
- Gemini TTS Kore: validada previamente en proyectos GAIATECH.
