---
titulo: "Data-Driven Cognitive Early Warning for Goaf Spontaneous Combustion: An Edge-Deployed RBF Network with Real-Time Multisensor Analytics"
autores:
  - G. Cheng
  - H. Pei
  - X. Chen
  - X. Pang
  - R. Sun
revista: Big Data and Cognitive Computing (MDPI)
year: 2026
volumen: 10
numero: 3
articulo: 91
doi: 10.3390/bdcc10030091
url: https://www.mdpi.com/2504-2289/10/3/91
tema: Big Data, cognitive computing, edge AI, alerta temprana, multi-sensor, RBF, riesgo minero
citacion: "Cheng, G., Pei, H., Chen, X., Pang, X., & Sun, R. (2026). Data-Driven Cognitive Early Warning for Goaf Spontaneous Combustion: An Edge-Deployed RBF Network with Real-Time Multisensor Analytics. Big Data and Cognitive Computing, 10(3), 91. https://doi.org/10.3390/bdcc10030091"
---

# Cognitive Early Warning Goaf Edge-AI (Cheng et al., 2026)

## Abstract resumido

Framework cognitivo basado en big data para predicción dinámica de riesgo de combustión espontánea en goaf minero, con arquitectura colaborativa "Cloud-Edge-End". Combina streams multi-sensor (CO, C2H4, O2, etc.) y despliega una red neuronal RBF ligera en nodos edge (STM32) subterráneos para analítica en tiempo real. Logra PR-AUC = 0.910 y recall = 99.7% en datasets desbalanceados, con inferencia única de 0.62 ms — habilitando un mapeo cognitivo de riesgo en tiempo real.

## Hallazgos clave aplicables

- **Arquitectura Cloud-Edge-End**: patrón directamente aplicable al M1.0 (FPGA edge → n8n cloud → WhatsApp end-user) y al despliegue en Las Bambas con conectividad mixta.
- **Inferencia 0.62 ms en edge**: la combustión goaf no es el caso del M1.0, pero el principio (modelo ligero en hardware embebido) valida la elección FPGA para procesamiento estructural local.
- **Recall 99.7% en datos imbalanced**: clave porque los datasets de accidentes mineros son típicamente desbalanceados; la lección RBF + features ingeniería es transferible al pipeline EPP.
- **Multi-sensor real-time analytics** como núcleo cognitivo: el M1.0 también ingiere múltiples streams (visión, sensores estructurales, reportes humanos) y se beneficia del mismo paradigma.
- **Publicación 2026 en MDPI BDCC**: respaldo de actualidad para citar en el informe LRAC como "estado del arte vigente".

## Cómo apoya la propuesta GAIATECH M1.0

Provee la legitimidad arquitectónica "Cloud-Edge-End" que necesita el M1.0 para defender su despliegue: FPGA (edge) + n8n/VPS (cloud) + WhatsApp/dashboard (end). Justifica que un modelo ligero embebido (no necesariamente RBF, podría ser YOLOv8 cuantizado) puede operar en tiempo real bajo restricciones de hardware. Aporta KPIs de referencia (recall 99.7%, latencia sub-milisegundo) para fijar SLAs ambiciosos pero verosímiles en la propuesta.

## Citación APA 7

Cheng, G., Pei, H., Chen, X., Pang, X., & Sun, R. (2026). Data-Driven Cognitive Early Warning for Goaf Spontaneous Combustion: An Edge-Deployed RBF Network with Real-Time Multisensor Analytics. *Big Data and Cognitive Computing*, *10*(3), 91. https://doi.org/10.3390/bdcc10030091
