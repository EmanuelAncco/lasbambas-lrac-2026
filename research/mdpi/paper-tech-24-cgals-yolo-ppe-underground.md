---
titulo: "CGALS-YOLO: Vision-Based Sensing for Protective Equipment Wearing Compliance Detection in Underground Environments"
autores:
  - Chao Huang
  - Hongkang Huang
revista: Sensors (MDPI)
year: 2026
volumen: 26
numero: 5
articulo: 1646
doi: 10.3390/s26051646
url: https://www.mdpi.com/1424-8220/26/5/1646
tema: Visión computacional, cumplimiento EPP, YOLOv8 mejorado, atención CGAFusion, LSCD, edge underground
citacion: "Huang, C., & Huang, H. (2026). CGALS-YOLO: Vision-Based Sensing for Protective Equipment Wearing Compliance Detection in Underground Environments. Sensors, 26(5), 1646. https://doi.org/10.3390/s26051646"
---

# CGALS-YOLO para Cumplimiento EPP Subterráneo (Huang & Huang, 2026)

## Abstract resumido

Propone CGALS-YOLO, derivado de YOLOv8 con módulo de fusión guiado por contenido (CGAFusion) y cabezal de detección compartido y ligero (LSCD), pensado para detectar cumplimiento de EPP en ambientes subterráneos con baja luz e interferencia. Alcanza mAP@0.5 de 89.4%, mejorando ~4.6% en precisión y ~3.1% en recall sobre YOLOv8n base, mientras reduce parámetros en ~20% y se mantiene en tiempo real a 66.5 FPS con 2.52 M parámetros.

## Hallazgos clave aplicables

- **mAP@0.5 = 89.4% en EPP subterráneo**: respaldo cuantitativo directo para el componente YOLOv8 EPP del M1.0, que opera en condiciones equivalentes.
- **CGAFusion (canal + espacial + pixel attention)**: técnica adaptable al pipeline actual para subir el recall sin reentrenar desde cero.
- **Reducción de 20% de parámetros + 23.9% en costo computacional**: alineado con la restricción edge/FPGA del M1.0 y con corridas en GPU modestas (RTX 4060 del entorno GAIATECH).
- **Mejora en detección de targets pequeños** (AP small de 0.241→0.272): importante para detectar barbijos, gafas y guantes en cámaras alejadas de los trabajadores.
- **66.5 FPS con 2.52 M parámetros**: viabilidad real-time para flujos múltiples en el dashboard M1.0.

## Cómo apoya la propuesta GAIATECH M1.0

Es la justificación científica más reciente (2026) para el corazón visión-computacional del M1.0. Permite al informe LRAC argumentar: (a) el estado del arte en EPP subterráneo va por mejoras a YOLOv8 — exactamente el modelo base de GAIATECH —, (b) las técnicas de atención y cabezales ligeros son transferibles inmediatamente, y (c) los KPIs propuestos (mAP, FPS, latencia) están al nivel de lo publicado en MDPI Sensors 2026. Excelente para citar en la sección "elección tecnológica del modelo de detección".

## Citación APA 7

Huang, C., & Huang, H. (2026). CGALS-YOLO: Vision-Based Sensing for Protective Equipment Wearing Compliance Detection in Underground Environments. *Sensors*, *26*(5), 1646. https://doi.org/10.3390/s26051646
