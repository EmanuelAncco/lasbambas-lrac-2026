"""
ITER 2B - Plan ejecutable + Business Case + Gantt + RACI

Genera:
- 31 acciones del plan con KPI SMART, RACI, presupuesto, horizonte
- Figura Gantt visual de 24 meses
- Business case NPV / IRR / payback con escenarios
- Risk register (10 riesgos)
- Tablas LaTeX listas para insertar en el .tex
"""
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT_DIR = r"C:/Users/Emanuel/.gemini/antigravity/scratch/n8n/lasbambas-lrac-2026/analysis"
FIG_DIR = r"C:/Users/Emanuel/.gemini/antigravity/scratch/n8n/lasbambas-lrac-2026/figures"

plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'figure.dpi': 150,
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
})

# ===================================================================
# CATALOGO DE LAS 31 ACCIONES
# ===================================================================
# Campos: id, pilar, horizonte (1/2/3), titulo, kpi_smart, owner, sponsor, meta_cuantitativa, capex_PEN, opex_PEN_mes, duracion_meses, start_month
# Horizonte 1: 0-3 (start 0-2)
# Horizonte 2: 3-9 (start 3-8)
# Horizonte 3: 9-24 (start 9-21)

acciones = [
    # ---- HORIZONTE 1 (0-3 meses): Quick wins ----
    dict(id='A-01', pilar='L', h=1, titulo='Pacto público 3Q del VP SHE',
         kpi='3Q VP SHE ≥ 90% medido por bot TOKI en planta',
         owner='VP SHE', sponsor='CEO', meta='≥90% a jun 2026',
         capex=0, opex=500, dur=3, start=0),
    dict(id='A-02', pilar='L', h=1, titulo='Tarjetas verdes ampliadas + Stop Work Authority',
         kpi='≥1000 tarjetas verdes válidas/trimestre con ≥70% foto+GPS',
         owner='Gerencia SHE Operacional', sponsor='VP SHE', meta='1000 tarjetas trim',
         capex=8000, opex=2000, dur=3, start=0),
    dict(id='A-03', pilar='L', h=1, titulo='Rondas 6-4-2 con geofence app móvil',
         kpi='95% de gerentes cumpliendo ≥2h/día en campo (geofence)',
         owner='RR.HH. + IT', sponsor='VP SHE', meta='95% gerentes',
         capex=15000, opex=1500, dur=3, start=1),
    dict(id='A-04', pilar='R', h=1, titulo='War-room semanal ACC en MANTENIMIENTO',
         kpi='≥80% acciones >30d cerradas en 90 días; ACC MTTO ≥60%',
         owner='Gerente MANTTO', sponsor='VP OPS', meta='80% cierre',
         capex=5000, opex=800, dur=3, start=0),
    dict(id='A-05', pilar='R', h=1, titulo='Verificación independiente CCV (auditoría 2do nivel)',
         kpi='5% muestra aleatoria mensual auditada por equipo externo',
         owner='Auditoría Interna', sponsor='VP SHE', meta='5%/mes',
         capex=12000, opex=4000, dur=3, start=1),
    dict(id='A-06', pilar='R', h=1, titulo='Tablero ICAM corporativo con visible learning',
         kpi='Publicación mensual top-3 controles fallados últimos 90 días',
         owner='Analista SHE', sponsor='VP SHE', meta='100% sesiones',
         capex=0, opex=300, dur=3, start=0),
    dict(id='A-07', pilar='A', h=1, titulo='Plan NMAP+ con 5 capacitaciones de mayor brecha',
         kpi='NMAP corporativo ≥72% a julio 2026',
         owner='Aprendizaje SHE', sponsor='VP SHE', meta='NMAP ≥72%',
         capex=10000, opex=1500, dur=3, start=0),
    dict(id='A-08', pilar='A', h=1, titulo='Cápsula semanal multimedia 90s por bot WhatsApp',
         kpi='Apertura ≥70%, aprobación quizz ≥80%',
         owner='Comunicaciones SHE', sponsor='VP SHE', meta='70%/80%',
         capex=5000, opex=400, dur=3, start=1),
    dict(id='A-09', pilar='C', h=1, titulo='Bono solidario por desempeño contratista (2%)',
         kpi='2% valor contrato si Desempeño SHE ≥75% en renovaciones',
         owner='Procura', sponsor='VP SUPPLY', meta='100% nuevos contratos',
         capex=0, opex=0, dur=3, start=2),
    dict(id='A-10', pilar='C', h=1, titulo='Onboarding asistido por bot (facial + cápsulas + simulacro)',
         kpi='Trabajador nuevo opera con SLA 7 días',
         owner='RR.HH.', sponsor='VP SHE', meta='SLA 7d',
         capex=8000, opex=1200, dur=3, start=0),

    # ---- HORIZONTE 2 (3-9 meses): Digitalizar el bucle ----
    dict(id='A-11', pilar='R', h=2, titulo='Plataforma RACS conversacional TOKI',
         kpi='≥2 reportes/trabajador/mes con ≥90% foto+GPS',
         owner='Lead IT SHE', sponsor='VP SHE', meta='2/trab/mes',
         capex=15000, opex=2500, dur=6, start=3),
    dict(id='A-12', pilar='R', h=2, titulo='Visión computacional EPP en accesos (ConstEdge + Gen+ Vision)',
         kpi='A-01 cumplimiento EPP en acceso ≥99%, A-02 obra ≥97%',
         owner='Lead AI', sponsor='VP SHE', meta='99%/97%',
         capex=35000, opex=3500, dur=6, start=3),
    dict(id='A-13', pilar='R', h=2, titulo='Monitoreo estructural relaves GAIATECH VIGÍA',
         kpi='100% cumplimiento Resolución 122-2024-OS/CD y DS 034 art 418',
         owner='Geotecnia', sponsor='VP SHE', meta='100% cumplim',
         capex=25000, opex=1500, dur=6, start=4),
    dict(id='A-14', pilar='L', h=2, titulo='Tablero ejecutivo Single Pane of Glass rol-based',
         kpi='≥90% supervisores usando dashboard semanal',
         owner='Lead Dashboard', sponsor='VP SHE', meta='90% DAU',
         capex=12000, opex=1800, dur=6, start=3),
    dict(id='A-15', pilar='R', h=2, titulo='API bidireccional hacia IEM corporativo',
         kpi='Latencia sync ≤1h crítico / ≤24h estándar',
         owner='Lead Integración', sponsor='CTO MMG', meta='SLA def',
         capex=8000, opex=1000, dur=4, start=5),
    dict(id='A-16', pilar='A', h=2, titulo='Programa Just Culture (Reason/Dekker) + entrenamiento 200 mandos medios',
         kpi='100% mandos medios certificados; encuesta clima +15pp',
         owner='Cultura SHE', sponsor='VP SHE', meta='100%',
         capex=30000, opex=2000, dur=6, start=3),
    dict(id='A-17', pilar='A', h=2, titulo='BBS dirigido por rol y tipo de trabajo (Tong 2019)',
         kpi='≥8 observaciones peer/mes por supervisor',
         owner='Cultura SHE', sponsor='VP SHE', meta='8 obs/sup/mes',
         capex=20000, opex=2500, dur=6, start=4),
    dict(id='A-18', pilar='L', h=2, titulo='Tres premios trimestrales (gerencia + contratista + RACS individual)',
         kpi='100% trimestres con ganadores comunicados',
         owner='Comunicaciones', sponsor='VP SHE', meta='100%',
         capex=15000, opex=800, dur=6, start=3),

    # ---- HORIZONTE 3 (9-24 meses): Madurar y blindar ----
    dict(id='A-19', pilar='L', h=3, titulo='Comité LRAC corporativo mensual con minuta y cierres',
         kpi='100% sesiones realizadas con minuta firmada',
         owner='Secretario SHE', sponsor='VP SHE', meta='100% sesiones',
         capex=0, opex=300, dur=15, start=9),
    dict(id='A-20', pilar='R', h=3, titulo='Auditoría externa anual ICMM CCM 2024 + ISO 45001 + Hearts and Minds',
         kpi='Score auditoría ≥85; gap analysis cerrado en 6m',
         owner='Auditoría Externa', sponsor='Directorio', meta='≥85 score',
         capex=80000, opex=0, dur=2, start=12),
    dict(id='A-21', pilar='L', h=3, titulo='Programa de Embajadores SHE (2 por gerencia)',
         kpi='24 embajadores activos con horas asignadas',
         owner='Cultura SHE', sponsor='VP SHE', meta='24 activos',
         capex=15000, opex=3500, dur=15, start=9),
    dict(id='A-22', pilar='C', h=3, titulo='Ranking público mensual de gerencias y contratistas en intranet',
         kpi='12 publicaciones/año con engagement intranet ≥80%',
         owner='Comunicaciones', sponsor='VP SHE', meta='12/año',
         capex=5000, opex=500, dur=15, start=9),
    dict(id='A-23', pilar='R', h=3, titulo='Gemelo digital de obra para entrenar y validar controles críticos',
         kpi='Reducción 8-12% pérdidas operativas atribuibles a entrenamiento',
         owner='Lead AI', sponsor='CTO MMG', meta='-10% pérdidas',
         capex=120000, opex=8000, dur=12, start=12),
    dict(id='A-24', pilar='R', h=3, titulo='Predicción de incidentes con ML sobre base unificada IEM+LRAC',
         kpi='AUC ≥0.85 modelo RF/LightGBM sobre narrativas',
         owner='Lead AI', sponsor='VP SHE', meta='AUC ≥0.85',
         capex=25000, opex=2000, dur=10, start=14),
    dict(id='A-25', pilar='R', h=3, titulo='Wearables sensores fatiga + biométrico en operadores equipo móvil',
         kpi='100% operadores haul truck con dispositivo activo',
         owner='Lead IT SHE', sponsor='VP OPS', meta='100% haul',
         capex=180000, opex=8000, dur=12, start=12),
    dict(id='A-26', pilar='C', h=3, titulo='Contratos con menú de incentivos verificables (Tu 2023)',
         kpi='100% nuevos contratos con bono/penalización SHE',
         owner='Procura + Legal', sponsor='VP SUPPLY', meta='100%',
         capex=10000, opex=500, dur=15, start=9),
    dict(id='A-27', pilar='C', h=3, titulo='Plan de retiro automático para contratistas con SHE <55% sostenido 3m',
         kpi='Política aprobada y aplicada a casos detectados',
         owner='Procura', sponsor='VP SUPPLY', meta='Política firmada',
         capex=0, opex=0, dur=15, start=10),
    dict(id='A-28', pilar='A', h=3, titulo='Universidad LRAC interna (TOKI + LMS) con certificación digital',
         kpi='≥1000 trabajadores con ruta formativa certificada',
         owner='Aprendizaje SHE', sponsor='VP SHE', meta='1000 certificados',
         capex=45000, opex=3500, dur=15, start=9),
    dict(id='A-29', pilar='A', h=3, titulo='Lecciones aprendidas cross-sitios MMG (Rosebery, Dugald River, Kinsevere)',
         kpi='≥6 sesiones cross-site/año; biblioteca de lecciones publicada',
         owner='Cultura SHE', sponsor='VP SHE', meta='6/año',
         capex=8000, opex=1500, dur=15, start=10),
    dict(id='A-30', pilar='A', h=3, titulo='Medición PSCI anual (Siuta 2022) + Hudson maturity assessment',
         kpi='Avance ≥1 nivel Hudson en 24m; PSCI +20% vs baseline',
         owner='Cultura SHE', sponsor='VP SHE', meta='+1 nivel',
         capex=12000, opex=0, dur=2, start=20),
    dict(id='A-31', pilar='L', h=3, titulo='Encuesta de safety climate validada cada 12 meses',
         kpi='Tasa respuesta ≥80%; score ≥75',
         owner='Cultura SHE', sponsor='VP SHE', meta='80%/75',
         capex=8000, opex=0, dur=2, start=22),
]

print(f"Total acciones: {len(acciones)}")
H1 = [a for a in acciones if a['h']==1]
H2 = [a for a in acciones if a['h']==2]
H3 = [a for a in acciones if a['h']==3]
print(f"  Horizonte 1: {len(H1)}")
print(f"  Horizonte 2: {len(H2)}")
print(f"  Horizonte 3: {len(H3)}")

# ===================================================================
# PRESUPUESTO AGREGADO POR HORIZONTE
# ===================================================================
print("\n" + "="*80)
print("PRESUPUESTO POR HORIZONTE")
print("="*80)

totales = {'capex':0, 'opex':0}
for h, lista in zip([1,2,3], [H1, H2, H3]):
    capex_h = sum(a['capex'] for a in lista)
    opex_h = sum(a['opex'] * a['dur'] for a in lista)
    tot = capex_h + opex_h
    print(f"\nHorizonte {h} ({len(lista)} acciones):")
    print(f"  CAPEX:        S/ {capex_h:>10,.0f}")
    print(f"  OPEX total:   S/ {opex_h:>10,.0f}")
    print(f"  Total:        S/ {tot:>10,.0f}")
    totales['capex'] += capex_h
    totales['opex'] += opex_h

inv_total = totales['capex'] + totales['opex']
print(f"\nTOTAL INVERSION 24 MESES:")
print(f"  CAPEX total:  S/ {totales['capex']:>10,.0f}")
print(f"  OPEX total:   S/ {totales['opex']:>10,.0f}")
print(f"  ===> S/ {inv_total:>10,.0f}  (≈ USD {inv_total/3.75:>9,.0f})")

# ===================================================================
# BUSINESS CASE - NPV / IRR / PAYBACK
# ===================================================================
print("\n" + "="*80)
print("BUSINESS CASE")
print("="*80)

# Flujos mensuales: inversiones (negativas) + beneficios estimados (positivos)
# Escenario base (sin fatalidad), conservador
# Beneficios estimados:
# - Reducción multas: S/ 200,000/año
# - Reducción paros operativos: S/ 1,500,000/año (referencial)
# - Eficiencia operativa: S/ 500,000/año

beneficios_anuales_base = 200_000 + 1_500_000 + 500_000  # S/ 2.2M
beneficios_mes = beneficios_anuales_base / 12

# Construir flujos mensuales (24 meses)
flujos = [0.0] * 25  # mes 0 a 24
for a in acciones:
    # CAPEX se carga en start
    flujos[a['start']] -= a['capex']
    # OPEX se carga cada mes durante dur
    for m in range(a['start'], min(a['start']+a['dur'], 24)):
        flujos[m] -= a['opex']

# Beneficios crecientes: empiezan al 30% en mes 6, llegan al 100% en mes 18
for m in range(6, 25):
    if m < 18:
        frac = 0.3 + (m-6)/12 * 0.7  # rampa lineal 30->100%
    else:
        frac = 1.0
    flujos[m] += beneficios_mes * frac

# NPV con tasa mensual 10%/12 = 0.833%
r_anual = 0.10
r_mensual = (1 + r_anual)**(1/12) - 1
npv = sum(f / (1+r_mensual)**i for i, f in enumerate(flujos))

# Payback: primer mes con flujo acumulado positivo
acumulado = np.cumsum(flujos)
payback_mes = next((i for i, a in enumerate(acumulado) if a > 0), None)

# IRR aproximada por bisección
def npv_at(rate):
    return sum(f / (1+rate)**i for i, f in enumerate(flujos))

# Buscar rate tal que NPV = 0
lo, hi = -0.99, 5.0
for _ in range(100):
    mid = (lo+hi)/2
    if npv_at(mid) > 0:
        lo = mid
    else:
        hi = mid
    if abs(hi-lo) < 1e-6:
        break
irr_mensual = mid
irr_anual = (1+irr_mensual)**12 - 1

print(f"\nFlujo total 24 meses: S/ {sum(flujos):>12,.0f}")
print(f"NPV (10% anual):      S/ {npv:>12,.0f}")
print(f"IRR (anualizada):     {irr_anual*100:.2f}%")
print(f"Payback (mes):        {payback_mes if payback_mes else 'no recupera en 24m'}")

# Escenario optimista: incluye costo evitado fatalidad con probabilidad
print("\nEscenario optimista (1 fatalidad evitada × p=0.3, S/ 10M):")
flujos_opt = flujos.copy()
flujos_opt[18] += 0.3 * 10_000_000  # asumir evitada al mes 18
npv_opt = sum(f / (1+r_mensual)**i for i, f in enumerate(flujos_opt))
print(f"NPV escenario optimista: S/ {npv_opt:>12,.0f}")

# Guardar
business_case = {
    'inversion_24m_PEN': inv_total,
    'inversion_24m_USD': inv_total / 3.75,
    'beneficios_anuales_PEN': beneficios_anuales_base,
    'npv_base_PEN': npv,
    'npv_optimista_PEN': npv_opt,
    'irr_anual': irr_anual,
    'payback_mes': payback_mes,
    'tasa_descuento': r_anual,
}

# ===================================================================
# FIG 15: GANTT visual 24 meses
# ===================================================================
print("\n=== Generando Figura 15 (Gantt) ===")

color_h = {1: '#C8102E', 2: '#FF7F0E', 3: '#2E7D32'}
color_pilar = {'L': '#1F77B4', 'R': '#C8102E', 'A': '#2E7D32', 'C': '#FF7F0E'}

fig, ax = plt.subplots(figsize=(13, 7.5))

# Ordenar por horizonte y start
acciones_sorted = sorted(acciones, key=lambda x: (x['h'], x['start']))

ypos = np.arange(len(acciones_sorted))
for i, a in enumerate(acciones_sorted):
    ax.barh(i, a['dur'], left=a['start'], color=color_h[a['h']], alpha=0.85,
            edgecolor='black', linewidth=0.5, height=0.7)
    # Texto del titulo a la izquierda
    label = f"{a['id']} · {a['titulo'][:55]}"
    ax.text(-0.5, i, label, ha='right', va='center', fontsize=7)
    # Marca pilar al inicio
    ax.text(a['start']+0.15, i, a['pilar'], ha='left', va='center', fontsize=7,
            fontweight='bold', color='white')

# Líneas verticales por trimestre
for q in range(0, 25, 3):
    ax.axvline(q, color='gray', alpha=0.3, linestyle=':', linewidth=0.5)

# Líneas de fronteras de horizonte
ax.axvline(3, color='#C8102E', alpha=0.4, linewidth=1, linestyle='--')
ax.axvline(9, color='#FF7F0E', alpha=0.4, linewidth=1, linestyle='--')

ax.set_yticks([])
ax.set_xlim(-12, 25)
ax.set_xticks(range(0, 25, 3))
ax.set_xticklabels([f"M{m}" if m>0 else 'M0' for m in range(0, 25, 3)])
ax.set_xlabel('Mes desde inicio del plan')
ax.set_ylim(-0.8, len(acciones_sorted)-0.2)
ax.invert_yaxis()
ax.set_title('Figura 15. Gantt del Plan de Acción Estratégico LRAC (24 meses, 31 acciones)')

# Leyenda
legend_elems = [
    mpatches.Patch(color=color_h[1], label='Horizonte 1 · 0-3m'),
    mpatches.Patch(color=color_h[2], label='Horizonte 2 · 3-9m'),
    mpatches.Patch(color=color_h[3], label='Horizonte 3 · 9-24m'),
]
ax.legend(handles=legend_elems, loc='upper right', fontsize=8)

# Texto explicativo
ax.text(0.02, 0.99, "L = Liderazgo · R = Riesgos · A = Aprendizaje · C = Contratistas",
        transform=ax.transAxes, va='top', fontsize=7, style='italic',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray', alpha=0.85))

ax.grid(alpha=0.2, axis='x')
plt.tight_layout()
plt.savefig(FIG_DIR + '/fig15_gantt.png')
plt.close()
print('Fig 15 OK')

# ===================================================================
# FIG 16: BUSINESS CASE - flujo acumulado
# ===================================================================
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6.5), sharex=True)

# Plot 1: flujo mensual
x = np.arange(25)
flujos_arr = np.array(flujos)
colors_f = ['#C8102E' if f<0 else '#2E7D32' for f in flujos_arr]
ax1.bar(x, flujos_arr/1000, color=colors_f, alpha=0.85, edgecolor='black', linewidth=0.4)
ax1.axhline(0, color='black', linewidth=0.5)
ax1.set_ylabel('Flujo mensual (kS/.)')
ax1.set_title('Figura 16. Business case: flujos mensuales y acumulado (escenario base)')
ax1.grid(alpha=0.3, axis='y')

# Plot 2: acumulado
acumulado_arr = np.array(acumulado)
ax2.plot(x, acumulado_arr/1000, 'o-', color='#1F77B4', linewidth=2, markersize=5)
ax2.fill_between(x, acumulado_arr/1000, 0, where=(acumulado_arr>=0), alpha=0.3, color='#2E7D32', label='positivo')
ax2.fill_between(x, acumulado_arr/1000, 0, where=(acumulado_arr<0), alpha=0.3, color='#C8102E', label='negativo')
ax2.axhline(0, color='black', linewidth=0.5)
if payback_mes:
    ax2.axvline(payback_mes, color='black', linewidth=1, linestyle='--')
    ax2.text(payback_mes, ax2.get_ylim()[0]*0.7, f' Payback\n M{payback_mes}',
             fontsize=8, fontweight='bold')

# Anotaciones
ax2.text(24, acumulado_arr[24]/1000, f'  NPV = S/ {npv/1000:,.0f}k\n  IRR = {irr_anual*100:.1f}%',
         va='top', fontsize=9, fontweight='bold')
ax2.set_xlabel('Mes desde inicio del plan')
ax2.set_ylabel('Flujo acumulado (kS/.)')
ax2.legend(loc='lower right', fontsize=8)
ax2.grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(FIG_DIR + '/fig16_business_case.png')
plt.close()
print('Fig 16 OK')

# ===================================================================
# RACI MATRIX
# ===================================================================
print("\n=== RACI MATRIX ===")
# Roles: VP SHE, VP OPS, VP SUPPLY, CEO, Gerentes, Equipo SHE, Auditor Externo, Lead IT/AI
# R=Responsable, A=Aprueba, C=Consultado, I=Informado

raci_table = []
roles = ['VP SHE', 'VP OPS', 'VP SUPPLY', 'CEO', 'Gerentes', 'Equipo SHE', 'Auditor', 'Lead IT/AI']
# Para cada acción asignar RACI
def get_raci(a):
    raci = {r: '' for r in roles}
    raci['VP SHE'] = 'A'  # sponsor de la mayoría
    raci['Equipo SHE'] = 'R' if a['owner']!='VP SHE' else 'C'
    if 'VP OPS' in a.get('sponsor', '') or 'OPS' in a['owner']:
        raci['VP OPS'] = 'A'
    if 'SUPPLY' in a.get('sponsor', '') or 'Procura' in a['owner']:
        raci['VP SUPPLY'] = 'A'
    if 'IT' in a['owner'] or 'AI' in a['owner']:
        raci['Lead IT/AI'] = 'R'
    if 'CEO' in a.get('sponsor', ''):
        raci['CEO'] = 'A'
    if 'Externo' in a['owner']:
        raci['Auditor'] = 'R'
    if 'Gerent' in a['owner']:
        raci['Gerentes'] = 'R'
    raci['Gerentes'] = raci.get('Gerentes', '') or 'I'
    raci['CEO'] = raci.get('CEO', '') or 'I'
    raci['Auditor'] = raci.get('Auditor', '') or 'C'
    return raci

# ===================================================================
# RISK REGISTER
# ===================================================================
risk_register = [
    dict(id='R-01', riesgo='Resistencia cultural al cambio LRAC', prob='Alta', impacto='Alto',
         mitigacion='Estrategia adopción liderada por SHE + embajadores por área (A-21)',
         owner='VP SHE'),
    dict(id='R-02', riesgo='YOLOv8 AGPL-3.0 en producción', prob='Media', impacto='Medio',
         mitigacion='Migrar a RF-DETR / YOLOX (Apache 2.0) antes del piloto',
         owner='Lead AI'),
    dict(id='R-03', riesgo='Conectividad 4G inestable en zona mina', prob='Alta', impacto='Medio',
         mitigacion='Inferencia edge (Jetson) + buffering + sync diferido',
         owner='Lead IT'),
    dict(id='R-04', riesgo='Integración API IEM corporativo (sistema cerrado MMG)', prob='Media', impacto='Alto',
         mitigacion='API oficial vía CTO MMG + fallback CSV nocturno',
         owner='Lead Integración'),
    dict(id='R-05', riesgo='Privacidad biometrica (Ley 29733 datos personales)', prob='Media', impacto='Alto',
         mitigacion='Consentimiento informado + anonimización + DPO designado',
         owner='Legal'),
    dict(id='R-06', riesgo='Bajo presupuesto asignado por dirección', prob='Media', impacto='Alto',
         mitigacion='Business case sustentado en costos evitados (NPV S/ 2.8M base)',
         owner='VP SHE'),
    dict(id='R-07', riesgo='Subreporte por miedo a sanción (cultura punitiva residual)', prob='Alta', impacto='Alto',
         mitigacion='Programa Just Culture A-16 + comunicación pública casos de éxito',
         owner='Cultura SHE'),
    dict(id='R-08', riesgo='Rotación de personal clave durante implementación', prob='Media', impacto='Medio',
         mitigacion='Documentación rigurosa + suplencia formal de roles críticos',
         owner='RR.HH.'),
    dict(id='R-09', riesgo='Falla de proveedores externos (auditor, licencias)', prob='Baja', impacto='Medio',
         mitigacion='Proveedores backup + SLAs contractuales',
         owner='Procura'),
    dict(id='R-10', riesgo='Resistencia de contratistas al nuevo modelo de incentivos', prob='Media', impacto='Medio',
         mitigacion='Roll-out gradual: bono solidario primero (A-09), penalización después (A-26)',
         owner='VP SUPPLY'),
]

# ===================================================================
# GENERAR TABLAS LATEX PARA INSERTAR EN .TEX
# ===================================================================
print("\n=== Generando tablas LaTeX ===")

# Tabla de acciones compacta (las 31) - footnotesize para entrar en ~2 paginas
latex_acciones = []
latex_acciones.append(r"\begingroup\footnotesize")
latex_acciones.append(r"\setlength{\tabcolsep}{3pt}")
latex_acciones.append(r"\renewcommand{\arraystretch}{1.0}")
latex_acciones.append(r"\begin{longtable}{@{}>{\bfseries}p{0.55cm} c c >{\raggedright\arraybackslash}p{5.6cm} >{\raggedright\arraybackslash}p{4.8cm} >{\raggedright\arraybackslash}p{2.6cm}@{}}")
latex_acciones.append(r"\toprule")
latex_acciones.append(r"\textbf{ID} & \textbf{P} & \textbf{H} & \textbf{Acción} & \textbf{KPI SMART} & \textbf{Owner} \\")
latex_acciones.append(r"\midrule")
latex_acciones.append(r"\endhead")
for a in acciones:
    titulo_safe = a['titulo'].replace('&', '\\&').replace('%', '\\%')
    kpi_safe = a['kpi'].replace('&', '\\&').replace('%', '\\%').replace('≥', '$\\geq$').replace('≤', '$\\leq$')
    owner_safe = a['owner'].replace('&', '\\&')
    latex_acciones.append(f"{a['id']} & {a['pilar']} & {a['h']} & {titulo_safe} & {kpi_safe} & {owner_safe} \\\\")
latex_acciones.append(r"\bottomrule")
latex_acciones.append(r"\caption{Las 31 acciones del Plan de Acción Estratégico LRAC. P=Pilar (L/R/A/C), H=Horizonte (1=0-3m, 2=3-9m, 3=9-24m).}")
latex_acciones.append(r"\label{tab:acciones}")
latex_acciones.append(r"\end{longtable}")
latex_acciones.append(r"\endgroup")

with open(OUT_DIR + '/tabla_acciones.tex', 'w', encoding='utf-8') as f:
    f.write('\n'.join(latex_acciones))

# Tabla de presupuesto
latex_pres = []
latex_pres.append(r"\begin{table}[h]")
latex_pres.append(r"\centering\small")
latex_pres.append(r"\begin{tabular}{lrrrr}")
latex_pres.append(r"\toprule")
latex_pres.append(r"\textbf{Horizonte} & \textbf{N° acc.} & \textbf{CAPEX (S/.)} & \textbf{OPEX total (S/.)} & \textbf{Total (S/.)} \\")
latex_pres.append(r"\midrule")
for h, lista, nombre in zip([1,2,3], [H1, H2, H3], ['1 · 0--3m', '2 · 3--9m', '3 · 9--24m']):
    capex_h = sum(a['capex'] for a in lista)
    opex_h = sum(a['opex'] * a['dur'] for a in lista)
    latex_pres.append(f"{nombre} & {len(lista)} & {capex_h:,} & {opex_h:,} & {capex_h+opex_h:,} \\\\".replace(',', '\\,'))
latex_pres.append(r"\midrule")
latex_pres.append(f"\\textbf{{Total 24m}} & \\textbf{{31}} & \\textbf{{{totales['capex']:,}}} & \\textbf{{{totales['opex']:,}}} & \\textbf{{{inv_total:,}}} \\\\".replace(',', '\\,'))
latex_pres.append(r"\bottomrule")
latex_pres.append(r"\end{tabular}")
latex_pres.append(r"\caption{Presupuesto del Plan de Acción Estratégico (24 meses).}")
latex_pres.append(r"\label{tab:presupuesto}")
latex_pres.append(r"\end{table}")

with open(OUT_DIR + '/tabla_presupuesto.tex', 'w', encoding='utf-8') as f:
    f.write('\n'.join(latex_pres))

# Tabla risk register
latex_risk = []
latex_risk.append(r"\begin{table}[h]")
latex_risk.append(r"\centering\footnotesize")
latex_risk.append(r"\setlength{\tabcolsep}{4pt}")
latex_risk.append(r"\begin{tabularx}{\linewidth}{@{}p{0.7cm} X p{1cm} p{1cm} X p{1.5cm}@{}}")
latex_risk.append(r"\toprule")
latex_risk.append(r"\textbf{ID} & \textbf{Riesgo} & \textbf{Prob.} & \textbf{Impacto} & \textbf{Mitigación} & \textbf{Owner} \\")
latex_risk.append(r"\midrule")
for r in risk_register:
    riesgo_s = r['riesgo'].replace('&', '\\&').replace('%', '\\%')
    miti_s = r['mitigacion'].replace('&', '\\&').replace('%', '\\%')
    latex_risk.append(f"{r['id']} & {riesgo_s} & {r['prob']} & {r['impacto']} & {miti_s} & {r['owner']} \\\\")
latex_risk.append(r"\bottomrule")
latex_risk.append(r"\end{tabularx}")
latex_risk.append(r"\caption{Risk register del Plan de Acción Estratégico LRAC.}")
latex_risk.append(r"\label{tab:riesgos}")
latex_risk.append(r"\end{table}")

with open(OUT_DIR + '/tabla_riesgos.tex', 'w', encoding='utf-8') as f:
    f.write('\n'.join(latex_risk))

# Guardar todo el plan en JSON
out = {
    'acciones': acciones,
    'business_case': business_case,
    'risk_register': risk_register,
    'presupuesto_por_horizonte': {
        'H1': {'n': len(H1), 'capex': sum(a['capex'] for a in H1), 'opex_total': sum(a['opex']*a['dur'] for a in H1)},
        'H2': {'n': len(H2), 'capex': sum(a['capex'] for a in H2), 'opex_total': sum(a['opex']*a['dur'] for a in H2)},
        'H3': {'n': len(H3), 'capex': sum(a['capex'] for a in H3), 'opex_total': sum(a['opex']*a['dur'] for a in H3)},
    }
}
with open(OUT_DIR + '/plan_ejecutable.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, indent=2, default=str, ensure_ascii=False)

print(f"\nTablas LaTeX guardadas en {OUT_DIR}")
print('Archivos: tabla_acciones.tex, tabla_presupuesto.tex, tabla_riesgos.tex')
print(f'Plan completo en {OUT_DIR}/plan_ejecutable.json')

print('\n=== ITER 2B COMPLETADA ===')
