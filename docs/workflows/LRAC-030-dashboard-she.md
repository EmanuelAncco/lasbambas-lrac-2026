---
id: LRAC-030
modulo: M1.D
nombre: Dashboard SHE — Single Pane of Glass
brecha: Convergencia VPs sin sistema dominante · falta de visibilidad ejecutiva accionable
stack: Next.js 16 + Tailwind + Postgres + VPS Gen+ · login httpOnly · rol-based
metrica: ≥90% supervisores usando dashboard semanal · LRAC Health Score visible
acciones: [A-14]
pilar: L · R · A · C
estado: produccion (Vision Pro PDK)
---

# LRAC-030 · Dashboard SHE Single Pane of Glass

## Brecha que ataca

El análisis del Excel muestra que **no existe un sistema dominante**: las 4 VPs convergen en una banda estrecha (68.57 % – 69.71 %) y los líderes mensuales rotan (SUPPLY enero → SUPPLY febrero → ¿OPERACIONES marzo? → PROYECTOS abril). Esto significa que **nadie tiene una vista única, en tiempo real, accionable del estado del sistema LRAC**.

El dashboard reemplaza el cocktail de Excel exportados + correos + reportes mensuales con una sola pantalla que **el VP SHE abre cada lunes a las 7 am** y entiende el estado en <30 s.

## Stack técnico

- **Next.js 16 + Tailwind 4** (frontend).
- **Postgres** con vistas materializadas para queries rápidas.
- **VPS Gen+ (187.77.250.111)** con SSL.
- **Login httpOnly + cookies seguras** rol-based:
  - Operario → su propios reportes, sus capacitaciones pendientes.
  - Supervisor → equipo + tiempo en campo + alertas EPP.
  - Superintendente → KPIs área + ranking contratistas + auditorías abiertas.
  - Gerente VP SHE → ejecutivo completo + cumplimiento legal + heatmap fatal risks.
  - Auditor externo → vista solo-lectura con trazabilidad ISO 45001.

## Layout objetivo (el "Single Pane")

```
┌────────────────────────────────────────────────────────────┐
│  LRAC HEALTH SCORE                                     72/100 │
├────────────────────────────────────────────────────────────┤
│  Liderazgo (L)    ████████░░  82%   ↑ +3% vs sem-1            │
│  Reporte (R)      ██████░░░░  61%   ↓ -5% vs sem-1            │
│  Auditoría (A)    ████████░░  78%   ↑ +1%                     │
│  Cumplimiento (C) ███████░░░  73%   ↑ +2%                     │
│  Adopción digital ████████░░  75%   ↑ +8%                     │
├────────────────────────────────────────────────────────────┤
│  Top 3 patrones detectados (Gemini Pro):                       │
│  1. Falta de chaleco en zona Chuspiri (8 detecciones/sem)     │
│  2. Contratista X con 0 reportes esta semana                  │
│  3. Tiempo de cierre subiendo (52 h vs meta 48 h)             │
├────────────────────────────────────────────────────────────┤
│  [Heatmap pilares VP × Mes]   [Ranking gerencias]              │
│  [Evolución LRAC-4P]          [Alertas activas (12)]           │
└────────────────────────────────────────────────────────────┘
```

## Flujo del workflow

```
1. Usuario abre dashboard.gaiatech.com (o subdominio Las Bambas)
2. Login con SSO corporativo o credenciales locales
3. Frontend identifica rol → carga vista correspondiente
4. Postgres SELECT optimizado vía vistas materializadas (refresh cada 5 min)
5. Render con drill-down:
   - Click en VP → ve sus gerencias
   - Click en gerencia → ve sus indicadores semanales
   - Click en indicador → ve evolución diaria + acciones abiertas
6. Cada vista incluye un componente "Reporte ejecutivo" que toma el último
   reporte de Gemini Pro (workflow LRAC-031) y lo muestra contextual
7. Botones de acción:
   - Crear acción correctiva manual
   - Marcar alerta como "atendida"
   - Programar reunión con owner de la gerencia
```

## KPIs y métricas

| KPI | Línea base | Meta H1 | Meta H3 |
|---|---|---|---|
| % supervisores con sesión semanal en dashboard | 0 % | 70 % | 95 % |
| % gerentes que abren el dashboard los lunes 7 am | 0 % | 80 % | 95 % |
| Tiempo medio para detectar alerta crítica | n/d (correo) | <5 min | <2 min |
| Sesiones desde móvil vs desktop | n/d | 60/40 | 70/30 |

## Estado actual y dependencias

- **Estado:** **producción**. La plataforma Vision Pro PDK (Gen+) está operativa en VPS Gen+ con login (`vision-pro-2026`). La adaptación al dominio LRAC requiere:
  - Re-cablear los datasources (Postgres del caso LRAC, no del PDK de obra civil).
  - Re-skin con paleta MMG (rojo `#C8102E` + gris).
  - Reconfigurar roles según organigrama Las Bambas.
- **Tiempo de despliegue piloto:** 3 semanas.

## Riesgos y mitigaciones

| Riesgo | Mitigación |
|---|---|
| Acceso desde la red corporativa MMG bloqueado | VPN corporativa MMG + IP whitelisting |
| Dependencia de uptime VPS Gen+ | Backup en mirror + monitoreo Uptime Robot |
| Curva de adopción de gerentes mayores | Versión simplificada "Resumen 1 página" + onboarding personal |

## Referencias

- Skotnicka-Zasadzień, B., & Krynke, M. (2021). *Digital transformation of high reliability organizations: Mining case.* Energies, 14(16), 4721.
- Vlachos et al. (2024). *End-to-end IoT mining workers.* Sensors.
- Vision Pro PDK (asset del autor en producción, VPS 187.77.250.111:3020).
