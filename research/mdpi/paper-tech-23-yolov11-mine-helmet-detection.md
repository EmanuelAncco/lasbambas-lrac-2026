---
titulo: "Research on Mine-Personnel Helmet Detection Based on Multi-Strategy-Improved YOLOv11"
autores:
  - Lei Zhang
  - Zhipeng Sun
  - Hongjing Tao
  - Meng Wang
  - Weixun Yi
revista: Sensors (MDPI)
year: 2024
volumen: 25
numero: 1
articulo: 170
doi: 10.3390/s25010170
url: https://www.mdpi.com/1424-8220/25/1/170
tema: Visión computacional, YOLOv11 mejorado, detección de casco minero, edge deployment
citacion: "Zhang, L., Sun, Z., Tao, H., Wang, M., & Yi, W. (2024). Research on Mine-Personnel Helmet Detection Based on Multi-Strategy-Improved YOLOv11. Sensors, 25(1), 170. https://doi.org/10.3390/s25010170"
---

# Multi-Strategy YOLOv11 para Casco Minero (Zhang et al., 2024)

## Abstract resumido

Propone GCB-YOLOv11, una variante mejorada de YOLOv11n para detectar personal y cascos en entornos mineros con iluminación irregular y obstrucción por equipos. Incorpora tres mejoras: GSConv (reemplazo de convolución estándar), módulo C3K2_FE (Faster_block + atención ECA) y Bi-FPN para fusión multi-escala. Resultado: 93.6% mAP@0.5 y 90.3 FPS, superando a YOLOv11n base en 3.3% en mAP y 9.4% en FPS, con solo 1.6 M parámetros y 4.5 G FLOPs.

## Hallazgos clave aplicables

- **93.6% mAP@0.5** detectando personal y cascos en condiciones reales de mina: benchmark contra el cual GAIATECH M1.0 puede dimensionar su modelo YOLOv8 EPP.
- **Robustez ante iluminación reflejante y oclusión multi-objeto**, condiciones típicas del LRAC de Las Bambas (galerías, equipos pesados, polvo).
- **Modelo ultraligero** (1.6 M parámetros, 4.5 G FLOPs, 90.3 FPS): valida que la detección de EPP puede correr en edge devices, alineado con la visión FPGA-edge del M1.0.
- **Atención ECA + Faster_block**: bloque de atención eficiente que puede transferirse al modelo YOLOv8 actual para subir mAP sin inflar el cómputo.
- **Reducción de falsos negativos** en escenarios con reflejos y oclusión, lo cual reduce la fatiga de alertas y mejora la confianza del operador en el dashboard.

## Cómo apoya la propuesta GAIATECH M1.0

Aporta el techo técnico cuantitativo (93.6% mAP, 90 FPS) para que el módulo YOLOv8 EPP del M1.0 defienda su factibilidad ante el comité LRAC. Sirve como referencia directa para el roadmap "v2" (migración a YOLOv11 + atención ECA), y para justificar que el procesamiento puede ser local (edge) sin saturar la red ni comprometer privacidad. Además, valida la métrica clave para SLA de visión: tiempo de inferencia <15 ms.

## Citación APA 7

Zhang, L., Sun, Z., Tao, H., Wang, M., & Yi, W. (2024). Research on Mine-Personnel Helmet Detection Based on Multi-Strategy-Improved YOLOv11. *Sensors*, *25*(1), 170. https://doi.org/10.3390/s25010170
