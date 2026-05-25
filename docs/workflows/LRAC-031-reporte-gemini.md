---
id: LRAC-031
modulo: M1.D
nombre: Reporte semanal ejecutivo Gemini Pro
brecha: Análisis manual del equipo SHE consume horas · narrativa inconsistente
stack: n8n cron + Postgres + Gemini Pro + Gmail/Drive + Slack/Telegram opcional
metrica: Reporte de 1 página automático cada lunes 6 am · cobertura 4 VPs
acciones: [A-06, A-19]
pilar: L · A
estado: produccion (componentes existentes)
---

# LRAC-031 · Reporte semanal ejecutivo Gemini Pro

## Brecha que ataca

El staff SHE actual prepara reportes ejecutivos manualmente cada semana. Esto consume **6–10 horas/semana de un analista** y produce narrativas inconsistentes (un analista enfatiza A, otro enfatiza B). El VP SHE recibe el reporte el martes o miércoles, no el lunes a primera hora cuando lo necesita para la reunión de comité.

## Stack técnico

- **n8n cron** lunes 6:00 hora Perú (1 hora antes del comité corporativo).
- **Postgres**: query consolidada de la semana (LRAC-4P diario, eventos, RACS abiertos, cierres, alertas).
- **Gemini Pro** con prompt cuidadosamente diseñado: rol = "VP SHE senior con 20 años en minería peruana", instrucciones = "produce un reporte ejecutivo de 1 página dirigido a la junta directiva".
- **Gmail + Drive** para distribución y archivo histórico.
- **Slack / Telegram** opcional para canal interno SHE.

## Flujo del workflow

```
Lunes 6:00 hora Perú
1. n8n cron dispara
2. Postgres extrae:
   - LRAC-4P diario última semana (delta vs semana previa)
   - Eventos: RACS abiertos, cierres, near-misses, ICAM activos
   - Detecciones IA: incumplimientos EPP por gerencia
   - Alertas estructurales (workflow LRAC-020)
   - Cumplimiento 6-4-2 (workflow LRAC-021)
   - Cápsulas: tasa de apertura, aprobación quizzes (LRAC-004)
3. n8n estructura los datos en JSON
4. POST a Gemini Pro con prompt:
   {
     rol: "VP SHE senior 20 años en mineria peruana",
     tarea: "produce reporte ejecutivo 1 pag para junta directiva",
     formato: "markdown con encabezados",
     estructura: [
       "RESUMEN (3 frases con cifras clave)",
       "QUE FUNCIONO (top 3 logros)",
       "QUE NO FUNCIONO (top 3 alertas)",
       "RECOMENDACIONES (3 acciones para la semana)",
       "TENDENCIA (proyeccion proximas 4 semanas)"
     ],
     tono: "directo, ejecutivo, sin jergas"
   }
5. Gemini devuelve el reporte ~600 palabras
6. n8n:
   - Renderiza el markdown a PDF con plantilla MMG
   - Envía vía Gmail al VP SHE + VPs + junta directiva
   - Archiva en Drive carpeta "Reportes Ejecutivos SHE > 2026 > Semana NN"
   - Publica en canal Slack/Telegram interno SHE
7. Métricas:
   - Tracking de aperturas del email
   - Click en links del PDF
   - Feedback opcional ("útil / inútil") por reacción
```

## Ejemplo de reporte generado (mockup)

```markdown
## Reporte ejecutivo SHE · Semana 19-2026 (12–18 mayo)

**RESUMEN.** LRAC-4P cerró la semana en 69.4 % (+0.3 pp vs semana 18). NMAP
sigue siendo el cuello de botella en 66.1 %. Se detectaron 8 incidentes EPP
en zona Chuspiri (zona crítica).

**QUE FUNCIONO.** (1) ACC en MANTENIMIENTO subió de 39 % a 51 % tras el
war-room semanal (A-04). (2) La cápsula "Trabajo en altura" tuvo 76 % de
apertura, el más alto del año. (3) PROYECTOS 1 alcanzó LRAC-4P de 78 %.

**QUE NO FUNCIONO.** (1) MEDIO AMBIENTE sigue en 3Q de 41 % (-2 pp vs sem-18).
(2) Reapertura de 3 ACC en SERV. TÉCNICOS por verificación visual fallida
(workflow LRAC-003). (3) Cumplimiento 6-4-2 cayó al 67 % en gerentes esta
semana (días con visita de auditoría externa).

**RECOMENDACIONES.**
1. Reunión 1:1 con gerente MEDIO AMBIENTE el martes para entender la caída.
2. Reforzar el war-room ACC en SERV. TÉCNICOS los próximos 14 días.
3. Mantener la racha de PROYECTOS 1 con reconocimiento público en el ranking.

**TENDENCIA.** Si las palancas se mantienen, LRAC-4P alcanzaría 71 % en
4 semanas. NMAP requiere intervención específica además del LRAC-004 actual.
```

## KPIs y métricas

| KPI | Meta |
|---|---|
| % reportes enviados el lunes antes 7 am | 100 % |
| Apertura email VP SHE | 100 % |
| Tasa de "feedback útil" | ≥80 % |
| Horas/semana ahorradas a analista | 6–10 |

## Estado actual y dependencias

- **Estado:** **producción**. Gen+ Vision PDK ya tiene reportes ejecutivos automáticos Gemini Pro en otro dominio. Adaptación al dominio LRAC ~1 semana.
- **Dependencias:**
  - Postgres con vistas semanales (LRAC-030).
  - API key Gemini Pro.
  - Cuenta Workspace Gmail/Drive.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Gemini alucina o reporta cifras inexistentes | Validación cruzada con los datos Postgres + prompt con anti-hallucination + revisión humana primera 4 semanas |
| Reportes genéricos (no agregan valor) | Iteración del prompt mensual + feedback explícito de los VPs |
| Costo de Gemini Pro | ~USD 0.05 por reporte; aceptable vs costo de 6-10 h analista |

## Referencias

- Skotnicka-Zasadzień, B., & Krynke, M. (2021). *Digital transformation of HRO.* Energies.
- Yedla, A., Kakhki, F. D., Jannesari, A. (2020). *Predictive modeling for occupational safety outcomes.* IJERPH.
- Vision Pro PDK (asset del autor con reportes Gemini Pro en producción).
