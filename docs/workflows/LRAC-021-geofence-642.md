---
id: LRAC-021
modulo: M1.C
nombre: Geofence 6-4-2 de liderazgo visible
brecha: Regla 6-4-2 no se mide objetivamente · 3Q MEDIO AMBIENTE 39%
stack: App PWA + GPS + Postgres + n8n cron + dashboard rol-based
metrica: ≥95% gerentes ≥2 h/día · ≥85% superintendentes ≥4 h/día · ≥75% supervisores ≥6 h/día
acciones: [A-03]
pilar: L
estado: diseno (stack PWA + GPS disponible)
---

# LRAC-021 · Geofence 6-4-2 de liderazgo visible

## Brecha que ataca

Las Bambas tiene formalmente la **regla 6-4-2**: 6 h supervisores, 4 h superintendentes, 2 h gerentes en campo todos los días. En la práctica, **no existe medición objetiva**: depende del autorreporte y de auditorías esporádicas. El Excel del caso muestra:
- **3Q en MEDIO AMBIENTE = 39 %** (la peor del set en enero 2026).
- **Pilar L (Liderazgo) corporativo en 67.6 %**, segundo más débil.

Si la VP custodio del sistema (SHE, donde está MEDIO AMBIENTE) no aplica ni siquiera "las 3 preguntas" en terreno, todo el sistema LRAC pierde legitimidad. La regla 6-4-2 debe **medirse, no asumirse**.

## Stack técnico

- **App PWA** (Progressive Web App) Next.js que se instala en el celular sin tienda.
- **GPS API del navegador** + service worker para tracking en background.
- **Geofences definidos** por staff SHE: zonas operativas (planta, tajo, talleres, relaves, accesos).
- **n8n** consolida eventos diarios.
- **Postgres** para registro auditable.
- **Dashboard rol-based** (LRAC-030) publica el ranking.

## Flujo del workflow

```
Diario
1. PWA abierta en celular del gerente/superintendente/supervisor
2. Service worker registra posición cada 60 s (con permiso del usuario)
3. Cliente clasifica si está dentro de uno de los geofences operativos:
   - Si dentro → cuenta minutos
   - Si fuera → no cuenta (oficina, casa, viaje)
4. Sincroniza cada 5 min con backend (resiliente a desconexión 4G)
5. Postgres acumula minutos por persona-día
6. n8n cron 17:00 hora Perú diario:
   - Calcula horas totales por persona-día
   - Compara con regla esperada por nivel jerárquico
   - Genera reporte:
     * Top 5 con más horas en campo (kudos)
     * Bottom 5 con menos horas (alerta privada al jefe)
7. Mensualmente:
   - Ranking público en intranet por gerencia
   - Histograma de cumplimiento 6-4-2
   - Correlación con LRAC-4P de la gerencia
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| % gerentes ≥2 h/día | n/d | 80 % | 95 % |
| % superintendentes ≥4 h/día | n/d | 70 % | 85 % |
| % supervisores ≥6 h/día | n/d | 65 % | 75 % |
| Correlación horas en campo ↔ LRAC-4P gerencia | n/d | medir | r ≥ 0.5 |

## Estado actual y dependencias

- **Estado:** **diseño**. PWA + GPS + n8n son tecnologías maduras en el stack del autor; integración estimada 2 semanas.
- **Dependencias:**
  - Definición formal de los geofences operativos (con SHE y planeamiento minero).
  - Consentimiento informado de cada empleado (privacy by design: solo se registra dentro de los geofences, no fuera).
  - Política corporativa: la métrica no se usa con fines disciplinarios, solo de gestión cultural (Just Culture, Reason 1997).

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Resistencia por percepción de vigilancia | Comunicar que solo se registra dentro de geofences + opt-in |
| Trampa: dejar el celular en zona operativa | Sensor de movimiento del celular + foto aleatoria de validación |
| GPS impreciso en zonas con poca señal | Suplementar con geofence de Wi-Fi corporativo |
| Batería del celular | Modo bajo consumo del PWA + horas autorizadas de tracking |

## Referencias

- Cooper, M. D. (2015). *Effective Safety Leadership: Understanding Types and Styles That Improve Safety Performance.* Professional Safety, 60(2), 49-53.
- British Safety Council (2024). *Visible Felt Safety Leadership: because we are stronger together.*
- Reason, J. (1997). *Managing the Risks of Organizational Accidents.* Ashgate. — Concepto de "Just Culture".
- Revista Seguridad Minera. *Estrategia de seguridad en Las Bambas.* — Documenta la regla 6-4-2.
