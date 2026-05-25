---
titulo: "Real-Time Monitoring of Underground Miners' Status Based on Mine IoT System"
autores:
  - Yufeng Jiang
  - Wei Chen
  - Xue Zhang
  - Xuejun Zhang
  - Guowei Yang
revista: Sensors (MDPI)
year: 2024
volumen: 24
numero: 3
articulo: 739
doi: 10.3390/s24030739
url: https://www.mdpi.com/1424-8220/24/3/739
tema: IoT minero, wearable, monitoreo en tiempo real, fatiga, 5G + UWB, posicionamiento, dashboard de visualización
citacion: "Jiang, Y., Chen, W., Zhang, X., Zhang, X., & Yang, G. (2024). Real-Time Monitoring of Underground Miners' Status Based on Mine IoT System. Sensors, 24(3), 739. https://doi.org/10.3390/s24030739"
---

# IoT Real-Time Monitoring of Underground Miners (Jiang et al., 2024)

## Abstract resumido

Sistema IoT minero para vigilar en tiempo real la seguridad, salud y fatiga de mineros subterráneos. Concentra la captura en dos wearables ergonómicos: brazalete electrónico (signos vitales por Bluetooth) y casco minero (multi-gas + posicionamiento UWB + comunicación inalámbrica). Usa una red distribuida 5G + UWB MIMO con latencia ≤20 ms y precisión de posicionamiento <0.3 m. Estima fatiga mediante un modelo backpropagation que correlaciona signos vitales con pH salival, y consolida todo en una plataforma de visualización unificada para gestión de emergencias.

## Hallazgos clave aplicables

- **Arquitectura dual de wearables** (brazalete + casco inteligente) que reduce la carga al minero y centraliza signos vitales, gases y ubicación: plantilla directa para una capa fisiológica complementaria a la cámara EPP de VIGIA.
- **Posicionamiento UWB <0.3 m** con polling bidireccional: nivel de precisión adecuado para mapas tácticos en el dashboard rol-based del M1.0 (supervisor LRAC, mina, ESM).
- **5G + MIMO distribuido con latencia ≤20 ms**: respaldo técnico para que el bus de eventos n8n + WhatsApp opere en escala de segundos sin perder criticidad.
- **Estimación de fatiga vía BP NN** sobre signos vitales correlacionados con pH salival; abre la puerta a ampliar GAIATECH M1.0 con un módulo de fatiga predictiva alimentado por wearables.
- **Operación validada >6 meses en mina de carbón en Northwest China sin incidentes vinculados a estado físico**: caso de éxito empírico que se puede citar como benchmark.

## Cómo apoya la propuesta GAIATECH M1.0

Demuestra que la combinación dashboard + wearables + posicionamiento + ML para fatiga es viable industrialmente y reduce incidentes. Refuerza la pieza "dashboard rol-based" del M1.0 con evidencia de que las visualizaciones unificadas mejoran la respuesta de emergencia, y abre línea futura para sumar wearables TOKI-compatibles al stack n8n + WhatsApp. También respalda que el FPGA estructural y la cámara YOLOv8 conviven con sensores fisiológicos en una sola plataforma.

## Citación APA 7

Jiang, Y., Chen, W., Zhang, X., Zhang, X., & Yang, G. (2024). Real-Time Monitoring of Underground Miners' Status Based on Mine IoT System. *Sensors*, *24*(3), 739. https://doi.org/10.3390/s24030739
