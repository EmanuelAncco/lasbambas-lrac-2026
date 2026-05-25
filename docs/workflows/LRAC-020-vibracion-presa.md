---
id: LRAC-020
modulo: M1.C
nombre: Monitoreo de vibración en presa de relaves
brecha: Cumplimiento DS 034-2023-EM art. 418 · Resolución 122-2024-OS/CD
stack: FPGA Gowin GW1NR-9 + ESP32 + LoRa + LSTM-Autoencoder PyTorch + n8n
metrica: F1 = 0.961 · alerta <2 s · reporte mensual OSINERGMIN automatico
acciones: [A-13]
pilar: R
estado: prototipo (2do AI Talent Demo Day 2026)
---

# LRAC-020 · Monitoreo de vibración en presa de relaves

## Brecha que ataca

El DS 034-2023-EM Capítulo XII (vigente desde diciembre 2023) introduce los artículos 418–423 sobre relaves, con énfasis en:
- **Art. 418:** programa de monitoreo geotécnico continuo, interpretación máxima cada 2 meses, firma de ingeniero geotecnia, Anexo 43.
- **Art. 419:** PPRE (Plan de Preparación y Respuesta a Emergencias) incluye falla/colapso.
- **Art. 423:** **sistema de suspensión automática de bombeo ante fugas**.

La Resolución 122-2024-OS/CD OSINERGMIN (junio 2024) reglamenta operativamente: reportes mensuales (5 días hábiles), reportes semestrales firmados por ingeniero geotécnico vía Ventanilla Virtual VVO. **Sin monitoreo automatizado, el cumplimiento es manual, lento y propenso a fallar.**

## Stack técnico

- **FPGA Gowin GW1NR-9** (Explorer Edge-9K o Tang Nano 9K): ejecuta FFT en hardware sobre la señal del sensor de vibración.
- **ESP32** como bridge: lee features pre-procesadas del FPGA, comunica vía **LoRa** de largo alcance (zona sin 4G).
- **Gateway LoRa** central conecta a Internet.
- **LSTM-Autoencoder en PyTorch** corre en el VPS Gen+: detecta anomalías sobre las features FFT.
- **n8n** orquesta alertas y generación de reportes.

## Flujo del workflow

```
Tiempo real
1. Acelerómetro en zona crítica (cresta de presa, conducto, espesador)
2. FPGA ejecuta FFT de 1024 puntos cada 1 s, devuelve features (5-10 bandas)
3. ESP32 recibe features y las envía por LoRa al gateway
4. Gateway publica vía MQTT a VPS Gen+
5. LSTM-Autoencoder procesa la ventana de features
6. Calcula reconstruction error y compara contra umbral
7. Si error > umbral (F1 = 0.961 sobre dataset de validación):
   - Alerta inmediata vía WhatsApp a geotecnia (<2 s)
   - Ticket auto en sistema interno
   - Log en Postgres con timestamp, magnitud, ubicación
8. n8n cron mensual (5 días hábiles):
   - Agrupa eventos del mes
   - Genera PDF Anexo 1 formato OSINERGMIN
   - Notifica al ingeniero geotécnico para firma digital
   - Sube a Ventanilla Virtual VVO automáticamente (workflow LRAC-032)
```

## KPIs y métricas

| KPI | Valor objetivo |
|---|---|
| F1 score detección anomalía | 0.961 (medido en validación) |
| Latencia alerta sensor → WhatsApp | <2 s |
| Tiempo medio entre falsos positivos | >30 días |
| Cumplimiento Resolución 122-2024-OS/CD | 100 % reportes mensuales en plazo |
| Cumplimiento DS 034 art. 418 (interpretación geotecnia) | máx 2 meses |

## Estado actual y dependencias

- **Estado:** **prototipo funcional**. Este sistema fue parte de GAIATECH VIGÍA, que obtuvo **2.º lugar AI Talent Demo Day 2026**.
- **Hardware ya probado:**
  - FPGA Gowin GW1NR-9 (Explorer Edge-9K) con FFT funcionando.
  - ESP32 + LoRa de largo alcance.
  - Pipeline LSTM-AE en VPS Gen+.
- **Dependencias para piloto Las Bambas:**
  - Acuerdo con geotecnia sobre puntos de instalación (presa Chuspiri u otra zona crítica).
  - Reentrenamiento del LSTM-AE con datos del sitio específico.
  - Validación cruzada con sensores convencionales (piezómetros, inclinómetros) durante 90 días.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Falsos positivos en zona sísmica (Apurímac) | Filtro adicional cruza-validando con red sísmica IGP |
| Sensor falla sin alerta | Heartbeat cada 60 s + dashboard de salud |
| LoRa interferida o sin cobertura | Backup vía 4G + buffering local en ESP32 |
| Cumplimiento normativo (firma del ingeniero) | Workflow integra firma digital aprobada por SUNAFIL |

## Referencias

- DS 034-2023-EM, Capítulo XII, artículos 418-423. Texto verificado vía análisis legal PRCP (sin acceso al PDF oficial completo al 2026-04-26).
- Resolución 122-2024-OS/CD OSINERGMIN.
- GISTM 2020 (Global Industry Standard on Tailings Management).
- ICMM Tailings Management Good Practice Guide, 2nd ed., Feb 2025.
- Cacciuttolo, C., et al. (2025). *Risk management model for tailings storage facilities in Chile.* Mining.
- GAIATECH VIGÍA: 2.º lugar AI Talent Demo Day 2026.
