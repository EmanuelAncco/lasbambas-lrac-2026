---
id: LRAC-032
modulo: M1.D
nombre: Auto-cumplimiento legal OSINERGMIN
brecha: Resolución 122-2024-OS/CD · 5 días hábiles mensuales · DS 034 art. 418
stack: n8n + Postgres + PDFkit + firma digital + Ventanilla Virtual VVO
metrica: 100% reportes enviados en plazo · 0 multas SUNAFIL/OSINERGMIN
acciones: [A-13, A-20]
pilar: R
estado: diseno (componentes existentes en otros dominios)
---

# LRAC-032 · Auto-cumplimiento legal OSINERGMIN

## Brecha que ataca

La Resolución 122-2024-OS/CD OSINERGMIN (junio 2024) reglamenta operativamente el DS 034-2023-EM art. 418:
- **Reporte mensual** (5 días hábiles desde el cierre del mes) firmado por el ingeniero geotécnico, vía Ventanilla Virtual VVO.
- **Reporte semestral** (octubre y abril, 10 días hábiles).
- **Anexo 1** con datos de monitoreo geotécnico.

En la práctica, el cumplimiento es **manual y consume entre 8 y 16 h/mes** de personal técnico, con riesgo de:
- Olvido del plazo → multa SUNAFIL/OSINERGMIN.
- Datos incompletos por error humano.
- Pérdida de evidencia por archivo desorganizado.

## Stack técnico

- **n8n cron** segundo día hábil de cada mes.
- **Postgres** consume datos de monitoreo (vienen del workflow LRAC-020 VIGÍA).
- **PDFkit (Python)** o **wkhtmltopdf** para renderizar el PDF con el formato exacto del Anexo 1.
- **Firma digital** vía proveedor certificado (Reniec o equivalente).
- **API o RPA (Playwright)** para subir el reporte a la Ventanilla Virtual VVO de OSINERGMIN.
- **Gmail + Drive** para notificaciones y archivo histórico auditable.

## Flujo del workflow

```
Mensual: día hábil #2 del mes nuevo
1. n8n cron dispara
2. Postgres SELECT de datos del mes anterior:
   - Lecturas de monitoreo VIGÍA (FFT, anomalías, alertas)
   - Eventos relevantes (cierres, mantenciones, suspensiones de bombeo)
   - Borde libre medido (DS 034 art. 420 ≥ 1 m)
   - Cumplimiento del programa de monitoreo geotécnico (art. 418)
3. n8n estructura los datos según formato Anexo 1
4. Renderiza el PDF con plantilla oficial
5. Envía al ingeniero geotécnico responsable:
   - Email + WhatsApp con link a la firma digital
   - El ingeniero revisa el PDF y firma digitalmente
6. Una vez firmado:
   - n8n ejecuta upload automatizado a Ventanilla Virtual VVO
     (vía API si OSINERGMIN la ofrece, o vía RPA Playwright)
   - Captura screenshot del comprobante de envío
   - Archiva en Drive: "Cumplimiento Legal > OSINERGMIN > 2026 > Mes-NN"
7. Notifica al VP SHE: "Reporte mensual OSINERGMIN enviado el [fecha]
                       con comprobante #[NN]"
8. Si el día hábil #5 está cerca y el reporte aún no se firma:
   - Escalamiento automático al jefe del ingeniero geotécnico
   - Recordatorio diario hasta cumplimiento
```

## Cumplimiento normativo cubierto

| Norma | Requisito | Cómo lo cumple LRAC-032 |
|---|---|---|
| DS 034-2023-EM art. 418 | Programa monitoreo geotécnico, interpretación máx 2 meses, firma ingeniero | Pipeline VIGÍA (LRAC-020) + firma digital integrada |
| DS 034-2023-EM art. 419 | PPRE incluye falla/colapso | Plan de respuesta disparado por alertas LRAC-020 |
| DS 034-2023-EM art. 420 | Borde libre ≥ 1 m | Sensor de nivel + alerta automática al violar umbral |
| DS 034-2023-EM art. 423 | Suspensión automática de bombeo ante fuga | Sensor presión/flujo + corte automático integrado |
| Resolución 122-2024-OS/CD | Reporte mensual 5 días hábiles vía VVO | Workflow automatizado |
| Resolución 122-2024-OS/CD | Reporte semestral oct/abr 10 días hábiles | Cron especial bimestral |

## KPIs y métricas

| KPI | Meta |
|---|---|
| % reportes enviados en plazo | 100 % |
| Multas SUNAFIL/OSINERGMIN por incumplimiento | 0 |
| Horas/mes ahorradas a personal técnico | 8–16 |
| Tiempo medio firma → envío | <24 h |

## Estado actual y dependencias

- **Estado:** **diseño**. Cada componente del stack (n8n + Postgres + PDFkit + firma + RPA Playwright) existe en producción para otros dominios; integración estimada 2–3 semanas.
- **Dependencias:**
  - LRAC-020 VIGÍA operativo (data source).
  - Acuerdo con el ingeniero geotécnico responsable y proceso formal de firma digital.
  - Credenciales Ventanilla Virtual VVO de Las Bambas.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| OSINERGMIN cambia el formato del Anexo 1 | Versionado de plantillas + revisión trimestral del cumplimiento |
| Falla de la firma digital al cierre del plazo | Backup: firma escaneada notarizada como fallback declarado en política |
| VVO cambia su interfaz (rompe RPA) | Monitoreo del RPA + endpoint API si OSINERGMIN lo expone |

## Referencias

- DS 024-2016-EM (Reglamento SSO Minería) + modificatorias DS 023-2017-EM y DS 034-2023-EM.
- Resolución 122-2024-OS/CD OSINERGMIN.
- GISTM 2020 (Global Industry Standard on Tailings Management).
- ICMM Tailings Management Good Practice Guide, 2nd ed., Feb 2025.
