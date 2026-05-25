---
titulo: "A Robust End-to-End IoT System for Supporting Workers in Mining Industries"
autores:
  - Marios Vlachos
  - Lampros Pavlopoulos
  - Anastasios Georgakopoulos
  - Georgios Tsimiklis
  - Angelos Amditis
revista: Sensors (MDPI)
year: 2024
volumen: 24
numero: 11
articulo: 3317
doi: 10.3390/s24113317
url: https://www.mdpi.com/1424-8220/24/11/3317
tema: IoT end-to-end, smart garment, cloud, edge, GDPR, mineros, monitoreo biométrico y ambiental
citacion: "Vlachos, M., Pavlopoulos, L., Georgakopoulos, A., Tsimiklis, G., & Amditis, A. (2024). A Robust End-to-End IoT System for Supporting Workers in Mining Industries. Sensors, 24(11), 3317. https://doi.org/10.3390/s24113317"
---

# End-to-End IoT for Mining Workers (Vlachos et al., 2024)

## Abstract resumido

Solución IoT completa para entornos mineros que combina dispositivos edge vestibles (chaleco-hub + brazalete + tapones) con una plataforma cloud que almacena y comparte datos conforme a regulaciones, ética y GDPR. La arquitectura mide signos biométricos, gases y posición UWB, y entrega alertas en tiempo real a los mineros. Validación en laboratorio y en tres minas reales (Marini-Marmi, Kemi, Titania) confirma la eficacia operativa del sistema.

## Hallazgos clave aplicables

- **Arquitectura edge-to-cloud jerárquica** (chaleco hub + BLE wristband + earplugs + Wi-Fi a infraestructura): plantilla directa para un eventual edge gateway que conecte la cámara YOLOv8 de VIGIA con el dashboard M1.0.
- **Métricas biométricas validadas** contra dispositivos comerciales: 4.52 bpm de error en frecuencia cardíaca, 0.084 µS en conductancia de piel, 0.48 °C en temperatura. Línea base creíble para si M1.0 incorpora wearables.
- **Posicionamiento UWB con ~60 cm de error medio** en interiores: precisión suficiente para alertas geo-contextualizadas en el dashboard rol-based.
- **Cumplimiento GDPR** explícito en el diseño cloud: insumo clave para que el informe LRAC defienda el manejo de datos personales en GAIATECH M1.0 frente a auditoría legal en Las Bambas.
- **Pruebas de campo en tres minas activas**: evidencia industrial de que la pila wearable-edge-cloud opera en ambientes equivalentes al peruano subterráneo y a cielo abierto.

## Cómo apoya la propuesta GAIATECH M1.0

Aporta el patrón "edge-cloud con cumplimiento normativo" que la propuesta M1.0 debe replicar para encajar en las exigencias de MMG Las Bambas: privacidad del personal, GDPR/Ley 29733 peruana y trazabilidad. Refuerza que YOLOv8 EPP + n8n + WhatsApp + dashboard pueden convivir con una capa biométrica adicional sin saltarse buenas prácticas, y aporta números concretos (latencias, errores) para los KPIs de la propuesta.

## Citación APA 7

Vlachos, M., Pavlopoulos, L., Georgakopoulos, A., Tsimiklis, G., & Amditis, A. (2024). A Robust End-to-End IoT System for Supporting Workers in Mining Industries. *Sensors*, *24*(11), 3317. https://doi.org/10.3390/s24113317
