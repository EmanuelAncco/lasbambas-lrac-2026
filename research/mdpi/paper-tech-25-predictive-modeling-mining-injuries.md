---
titulo: "Predictive Modeling for Occupational Safety Outcomes and Days Away from Work Analysis in Mining Operations"
autores:
  - Anurag Yedla
  - Fatemeh Davoudi Kakhki
  - Ali Jannesari
revista: International Journal of Environmental Research and Public Health (MDPI)
year: 2020
volumen: 17
numero: 19
articulo: 7054
doi: 10.3390/ijerph17197054
url: https://www.mdpi.com/1660-4601/17/19/7054
tema: Machine learning, predicción de accidentes mineros, random forest, NLP de narrativas MSHA, días perdidos
citacion: "Yedla, A., Kakhki, F. D., & Jannesari, A. (2020). Predictive Modeling for Occupational Safety Outcomes and Days Away from Work Analysis in Mining Operations. International Journal of Environmental Research and Public Health, 17(19), 7054. https://doi.org/10.3390/ijerph17197054"
---

# Predictive Modeling de Lesiones Mineras (Yedla et al., 2020)

## Abstract resumido

Aplica machine learning (árboles de decisión, random forest, redes neuronales) a datos de Mine Safety and Health Administration (MSHA) usando tanto campos estructurados como narrativas de accidentes para predecir tipo de lesión, severidad y días alejados del trabajo. Demuestra que los modelos entrenados con narrativas superan a los basados solo en datos estructurados (93–94% de exactitud) y que los random forest sobresalen como predictores. Discute el rol del data augmentation y la complementariedad entre narrativas y datos tabulares.

## Hallazgos clave aplicables

- **Random Forest sobre narrativas alcanza 93–94% de exactitud** prediciendo tipo de lesión: viable como motor analítico para el módulo predictivo del dashboard M1.0.
- **Las narrativas (texto libre)** contienen información clave ausente en campos estructurados, lo cual valida el componente TOKI + Gemini (chatbot recolector de reportes en lenguaje natural por WhatsApp).
- **Importancia de variables**: naturaleza de la lesión > parte del cuerpo > ocupación. Útil para diseñar las dimensiones del dashboard rol-based (rol = ocupación; vista LRAC vs. operador).
- **Datos tabulares ganan en predicción de días perdidos** mientras narrativas ganan en severidad: justifica un híbrido tabular+NLP en el pipeline n8n + Gemini de M1.0.
- **Synthetic narrative generation** (word embeddings) mejora clases minoritarias: técnica replicable para casos de Las Bambas con pocos datos históricos en algunos tipos de accidente.

## Cómo apoya la propuesta GAIATECH M1.0

Sustenta científicamente que un pipeline narrativa-texto (WhatsApp → TOKI → Gemini → BD) sumado a datos estructurados (visión, sensores) puede predecir accidentes con alta precisión. Permite al informe LRAC argumentar que GAIATECH M1.0 no solo "detecta" EPP en tiempo real, sino que aprende y proyecta riesgos a partir de reportes históricos, dándole continuidad analítica al ciclo. Refuerza la propuesta de modelo Random Forest como baseline en el dashboard predictivo.

## Citación APA 7

Yedla, A., Kakhki, F. D., & Jannesari, A. (2020). Predictive Modeling for Occupational Safety Outcomes and Days Away from Work Analysis in Mining Operations. *International Journal of Environmental Research and Public Health*, *17*(19), 7054. https://doi.org/10.3390/ijerph17197054
