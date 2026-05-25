---
id: LRAC-004
modulo: M1.B
nombre: Cápsula semanal multimedia + quiz adaptativo
brecha: NMAP 65.71% (cuello de botella corporativo) + brecha contratistas
stack: n8n cron + DaVinci Resolve auto + Gemini quiz + WhatsApp + Postgres
metrica: Apertura ≥70% · aprobación quizz ≥80%
acciones: [A-08, A-10, A-28]
pilar: A · C
estado: produccion (cron y quiz); video gen semiautomatizado
---

# LRAC-004 · Cápsula semanal multimedia + quiz adaptativo

## Brecha que ataca

El análisis del Excel identifica **NMAP en 65.71 %** como la herramienta más débil del sistema a nivel corporativo. NMAP = Nivel de Madurez de Aprendizaje. Zhang et al. (2022) midieron en 305 mineros chinos que **el entrenamiento es el predictor número 1 del comportamiento seguro** (peso causal β = 0.504), muy por encima de "política sola" (β = 0.110). Sin embargo, la capacitación tradicional (PPT pasivo en sala, retención 10–30 %) está obsoleta. Bęś & Strzałkowski (2024, *Sustainability*) demuestran que **métodos activos elevan retención a 60–90 %**.

## Stack técnico

- **n8n cron** lunes 7:00 hora Perú.
- **Generación de video 90 s** usando DaVinci Resolve MCP (~280 tools disponibles): plantilla + voiceover Gemini TTS voz Kore + capturas + transiciones predefinidas.
- **Generación del quiz** vía Gemini Pro: 3 preguntas de opción múltiple a partir del contenido del video.
- **Distribución** vía WhatsApp con Evolution API.
- **Postgres** para tracking de aperturas, respuestas, ranking.

## Flujo del workflow

```
Lunes 7:00 hora Perú
1. n8n cron dispara
2. Selección del tema de la semana (basado en últimos eventos + Regla para la Vida rotativa)
3. Gemini Pro genera el guion del video (90 s, 3 escenas)
4. DaVinci MCP renderiza el video con voz Kore + capturas/animaciones
5. Gemini Pro genera 3 preguntas + 4 opciones por pregunta
6. n8n envía a TODOS los trabajadores activos vía WhatsApp:
   - Texto del tema + video 90 s + botón "Hacer quiz"
7. Trabajador hace quiz; respuestas se guardan en Postgres
8. Si responde mal:
   - Bot le envía cápsula remedial 24 h después (más detallada)
   - Re-evaluación a las 48 h
   - Si vuelve a fallar 3 veces → notifica supervisor + plan formativo personalizado
9. Si responde bien:
   - Bot felicita + suma puntos a su gerencia/contratista
10. Lunes 7 días después: ranking por gerencia publicado en intranet + workflow LRAC-030
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| NMAP corporativo | 65.71 % | 72 % | 82 % |
| Tasa de apertura de la cápsula | n/d | 50 % | 75 % |
| Aprobación quiz primera vuelta | n/d | 60 % | 85 % |
| Trabajadores con remedial activo | n/d | <15 % | <5 % |
| Reducción de incidentes por tema cubierto | n/d | medir 90 d post-cápsula | -25 % vs control |

## Estado actual y dependencias

- **Estado de los componentes:**
  - n8n cron + Postgres tracking: **producción**.
  - WhatsApp distribución: **producción**.
  - Quiz generation con Gemini: **producción**.
  - Video gen DaVinci MCP: **semiautomatizado** (la primera versión es manual; la generación 100 % auto requiere ~3 días de prompt engineering + plantillas).
- **Dependencia clave:** registro maestro de trabajadores activos sincronizado con RR.HH.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Fatiga del trabajador (cápsula sentida como spam) | Máx 1 video/semana + posibilidad de skip + métricas honestas |
| Contratistas sin teléfono empresa | Bono solidario (A-09) cubre acceso al canal personal con consentimiento |
| Brecha digital (trabajadores mayores) | Versión audio + soporte presencial primer mes |

## Referencias

- Zhang, J. et al. (2022). *Safety leadership of mine managers: Multi-dimensional structure and empirical study.* IJERPH, 19(10), 6187.
- Bęś, P., & Strzałkowski, P. (2024). *Effectiveness of safety training methods.* Sustainability.
- Tong, R. et al. (2019). *Critical safety behaviors targeted intervention in Chinese underground coal miners.* IJERPH, 16(3), 422.
- Urbanek, S. et al. (2025). *VR training for mining safety culture.* Sustainability, 17(13), 6205.
