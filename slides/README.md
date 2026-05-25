# Slides defensa oral · 10 minutos

Slidev deck (markdown + Vue) para sustentación oral si el caso avanza a etapa 2.

## Contenido

- `slides.md` — 14 slides con narrativa de 10 min.
- Stack: [Slidev](https://sli.dev) (markdown + Vue + Tailwind + UnoCSS).
- Tema oscuro paleta MMG (`#0F0F10` + rojo `#C8102E`).
- Export a PDF + HTML público.

## Cómo usarlo

### Local (desarrollo y presentación)

```bash
# Requiere Node 18+
cd "c:\Users\Emanuel\.gemini\antigravity\scratch\n8n\lasbambas-lrac-2026\slides"
npx -y slidev@latest slides.md
# Abre http://localhost:3030
```

Atajos durante la presentación:
- **F** → fullscreen
- **D** → modo presentador (dual screen)
- **O** → vista general
- **←/→** → navegar
- **G** → ir a slide específica

### Export a PDF

```bash
# instala playwright deps (primera vez)
npx -y slidev@latest export slides.md --output emanuel-ancco-lrac-slides.pdf
```

Genera `emanuel-ancco-lrac-slides.pdf` listo para adjuntar al envío.

### Export a HTML público

```bash
npx -y slidev@latest build slides.md
# Genera carpeta dist/ con sitio estático
```

Subir `dist/` a:
- **GitHub Pages** del propio repo `lasbambas-lrac-2026` (carpeta `/docs/slides/`).
- **Vercel** o **Netlify** drag-and-drop.
- **VPS Gen+** detrás de nginx.

URL final esperada: `https://emanuelancco.github.io/lasbambas-lrac-2026/slides/` o similar.

## Estructura de las 14 slides

| # | Slide | Tiempo objetivo | Mensaje clave |
|---|---|---|---|
| 1 | Portada | 30 s | Identificación + autoridad (2.º AI Talent) |
| 2 | El problema en 1 pantalla | 45 s | 55 % global · 69.2 % LRAC-4P · 4 500 trabajadores |
| 3 | Estructura organizacional | 30 s | 4 VPs, 12 gerencias, fórmula 4P |
| 4 | Metodología | 40 s | Análisis estadístico + marco conceptual |
| 5 | Hallazgo 1 · peores gerencias enero | 50 s | 3 de 4 peores en OPERACIONES; SHE peor en 3Q |
| 6 | Hallazgo 2 · VP top anual | 50 s | SUPPLY lidera pero inestable; OPERACIONES más estable |
| 7 | Hallazgo 3 · PROYECTOS | 50 s | 68.59 % + ACC 61.12 % · valle marzo 50 % |
| 8 | Hallazgo 4 · LRAC por VP | 50 s | Rotación de líderes entre anual y cierre |
| 9 | Refuerzo estadístico inferencial | 60 s | K-W p=0.724 + score compuesto inverso |
| 10 | Diagnóstico Hudson | 40 s | Calculativa → Proactiva |
| 11 | 4 módulos GAIATECH M1.0 | 75 s | Activos en producción · métricas verificables |
| 12 | Plan · 31 acciones · 3 horizontes | 60 s | Hoja de ruta auditable |
| 13 | Business case 24 meses | 50 s | NPV S/ 1.21 M · IRR 343 % · payback mes 11 |
| 14 | Cierre · no es PowerPoint, es producción | 30 s | URLs anexas + identificación |

**Total: ~10:00 minutos.**

## Tips para la sustentación

- Practicar dos veces en voz alta cronometrando.
- Slide 11 (4 módulos GAIATECH) es **el ancla diferencial**: dedicar 75 s y abrir conversación con el jurado sobre el módulo que más les interese.
- Tener el Streamlit listo en otra pestaña para mostrar en vivo si el jurado pregunta.
- Cerrar con la frase "no es PowerPoint, es producción" haciendo gesto firme.

## Slides skeleton

Si Slidev no está disponible, el mismo deck se puede reproducir en:
- **PowerPoint / Google Slides:** copiar el contenido de cada bloque `## Slide N` a una diapositiva.
- **Canva Pro:** importar `slides.pdf` exportado y editar.
- **Keynote:** import desde PDF y refinar visualmente.

## Referencias usadas en las slides

Las mismas 30 referencias APA 7 del informe PDF (mayoría MDPI). Las más citadas:

- Foster & Hoult (2013) — Safety Maturity Model UK Coal Mining.
- Siuta et al. (2022) — Process Safety Culture Index + Bradley exponencial.
- Selleck et al. (2022) — Confiabilidad real de controles críticos 42 %.
- Zhang et al. (2022) — Pesos causales de liderazgo en mineros chinos.
- Tu et al. (2023) — Diseño de contratos con incentivos verificables.
- Huang & Huang (2026) — CGALS-YOLO mAP 89.4 % en EPP subterráneo.
- ICMM (2024) — Benchmarking Safety Data.

Detalle completo en `report/Emanuel Edgar Ancco Guaygua.pdf` (Sección 9 · Bibliografía).
