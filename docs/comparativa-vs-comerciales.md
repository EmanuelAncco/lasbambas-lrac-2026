---
titulo: GAIATECH M1.0 vs plataformas SHE comerciales
tipo: apéndice digital · análisis competitivo
fecha: 2026-05-21
---

# GAIATECH M1.0 vs SAP EHS · Intelex · Enablon

> Comparativa honesta de la propuesta del autor contra las tres plataformas comerciales SHE más usadas en mineras grandes (BHP, Rio Tinto, Anglo American, MMG).

## Resumen ejecutivo

Las plataformas comerciales son robustas, certificadas y bancarias-grado. Cobran **USD 150 000 – 600 000 / año** de licencia + servicios profesionales y suelen tardar **12-18 meses** en implementarse desde la firma del contrato.

**GAIATECH M1.0** no compite con la profundidad funcional de un SAP EHS. Compite en **velocidad, costo, contextualización peruana y capacidad de operar bajo IEM corporativo** sin reemplazarlo. Es una **capa habilitadora** que se monta sobre lo que MMG ya tiene, no una sustitución de su core.

---

## Tabla comparativa estructurada

| Dimensión | SAP EHS Management | Intelex EHS | Enablon EHS | **GAIATECH M1.0** |
|---|---|---|---|---|
| **Origen** | SAP SE · Alemania | Industrial Scientific · Canadá | Wolters Kluwer · USA | Autor independiente · Perú |
| **Licencia base anual** | USD 200-600 k | USD 150-400 k | USD 250-500 k | **OPEX S/ 20 k/año (~USD 5 k)** |
| **CAPEX setup** | USD 300-800 k | USD 200-500 k | USD 400-1 M | **S/ 35 k (~USD 9 k)** |
| **Tiempo de implementación** | 12-18 meses | 9-12 meses | 12-24 meses | **2-3 semanas piloto** |
| **Modelo licencia** | Por usuario (LE Cloud) | Por módulo | Por usuario premium | **Open-source MIT + servicios** |
| **Dependencia del vendor** | Alta · suscripción multi-anual | Media | Alta · contratos largos | **Cero** · código del cliente |
| **Captura RACS móvil** | Sí · módulo EHS Worker Health | Sí · móvil nativo | Sí · EHS Connect | **Sí · WhatsApp bot (zero-install)** |
| **Visión computacional EPP** | No nativo · integración tercero | No nativo | No nativo | **Sí · YOLOv8 87.67 % mAP** |
| **Monitoreo estructural IoT** | Vía SAP IoT (costo extra) | Vía integración OEM | Vía Wolters IoT | **Sí · FPGA propio F1=0.961** |
| **Agente conversacional** | No (chatbot básico) | No | No | **Sí · Aecodito Minero n8n+Gemini** |
| **Datos peruanos en modelos** | No | No | No | **Sí · 14 055 imgs entrenadas localmente** |
| **Cumplimiento DS 024-2016-EM** | Configurable | Configurable | Configurable | **Nativo · plantillas peruanas** |
| **Cumplimiento DS 034-2023-EM Cap. XII (relaves)** | Manual · custom dev | Manual | Manual | **Workflow LRAC-032 automático a VVO OSINERGMIN** |
| **Integración con IEM corporativo MMG** | Necesita conectores propietarios | Requiere middleware | Solo via API REST | **API REST + fallback CSV nocturno** |
| **Soporte local en Perú** | Implementadores certificados (Lima) | Resellers locales | Limitado | **Soporte directo del autor + comunidad gen+** |
| **Curva de adopción operario** | Media (apps móviles complejas) | Media | Baja-media | **Mínima · solo WhatsApp** |
| **Total Cost of Ownership 5 años** | USD 1.3-3.8 M | USD 950 k - 2.5 M | USD 1.7-3.5 M | **USD 35-50 k** |

---

## Análisis por dimensión

### Donde las comerciales ganan

1. **Profundidad funcional regulatoria global**: SAP EHS, Intelex y Enablon cubren OSHA, OSHA Process Safety, Seveso III, EPA, MSHA, REACH, RCRA, ISO 14001, ISO 45001, ICMM CCM, GISTM, IATF 16949 en un solo módulo configurable. GAIATECH M1.0 cubre las cinco normas peruanas críticas y los cuatro estándares internacionales relevantes para MMG; no pretende ser universal.

2. **Audit-grade certifications**: las tres tienen SOC 2 Type II, ISO 27001, certificaciones FedRAMP en algunos casos. GAIATECH M1.0 está en VPS dedicado del autor y requiere auditoría de seguridad independiente antes del piloto en Las Bambas.

3. **Comunidad y ecosistema**: SAP EHS tiene miles de consultores certificados. GAIATECH tiene un autor.

### Donde GAIATECH M1.0 gana

1. **Velocidad**: 2-3 semanas de piloto vs 12-18 meses. Para un caso urgente como el del sistema LRAC al 55 %, la diferencia es operacionalmente crítica.

2. **Costo**: el TCO 5 años de USD 35-50 k vs USD 1.3-3.8 M permite **invertir el 95 % del presupuesto en otros frentes** (cultura, capacitación, embajadores SHE).

3. **Contextualización local**: 14 055 imágenes de obra peruana entrenan el modelo de visión; las plantillas de RACS siguen el formato MMG; el flujo OSINERGMIN VVO está nativo, no configurado por consultora.

4. **Captura conversacional vía WhatsApp**: el operario peruano usa WhatsApp. Las tres plataformas comerciales exigen instalar su app móvil propietaria, capacitar al usuario, gestionar el rollout. WhatsApp ya está en el celular de todos.

5. **Verificación visual de cierre (LRAC-003)**: ninguna comercial valida automáticamente con IA visual que el cierre de un RACS sea real. Es un diferencial técnico significativo dada la evidencia ICMM 2024 (confiabilidad real CCV = 42 %).

6. **Hardware propio para relaves**: el módulo M1.C (FPGA Gowin + LSTM-AE) no tiene equivalente en las plataformas comerciales sin costos de integración de terceros.

### Lectura honesta

Una empresa del tamaño de MMG **probablemente terminará con SAP EHS o Enablon como columna vertebral corporativa**. La propuesta NO es reemplazar eso. La propuesta es:

> **GAIATECH M1.0 = capa habilitadora rápida + capa de innovación + capa de cumplimiento peruano**, que opera sobre IEM corporativo MMG y reduce el time-to-value de 18 meses a 3 semanas mientras el equipo corporativo evalúa una solución global.

El postulante propone una **convivencia inteligente** entre stack corporativo MMG e innovación local rápida, no un reemplazo.

---

## Costos al detalle

### Asumiendo piloto 12 meses · 4 500 trabajadores Mina Juanita S.A.

| Concepto | SAP EHS | Intelex | Enablon | GAIATECH M1.0 |
|---|---|---|---|---|
| Licencia software | USD 350 000 | USD 250 000 | USD 380 000 | USD 0 (MIT) |
| Servicios profesionales setup | USD 500 000 | USD 300 000 | USD 600 000 | USD 5 000 (autor) |
| Infraestructura | USD 80 000 (cloud) | USD 60 000 | USD 100 000 | USD 2 000 (VPS) |
| Soporte + capacitación | USD 120 000 | USD 80 000 | USD 150 000 | USD 3 000 |
| Hardware adicional (cámaras, FPGA, edge) | USD 50 000 | USD 50 000 | USD 50 000 | USD 12 000 |
| **Total piloto año 1** | **USD 1 100 000** | **USD 740 000** | **USD 1 280 000** | **USD 22 000** |
| Recurrente anual desde año 2 | USD 500 000 | USD 350 000 | USD 600 000 | USD 7 000 |

**Diferencia año 1:** GAIATECH M1.0 cuesta **2 % del más barato comercial (Intelex)**. Esto no es por ser inferior; es por aprovechar open-source, infraestructura del autor y simplicidad arquitectónica.

---

## Riesgos de GAIATECH M1.0 (honestos)

1. **Dependencia del autor**: si el autor se ausenta, la continuidad del soporte cae. Mitigación: documentación completa en repo público, transferencia de conocimiento al equipo MMG en H1.
2. **Escalabilidad**: el stack está probado para ~5 000 usuarios; cargas masivas (50 000+) requieren refactor a Kubernetes + bus de eventos. Las comerciales escalan a 100 k+ out-of-the-box.
3. **Certificaciones**: SOC 2 / ISO 27001 toman 12 meses; las comerciales ya las tienen.
4. **Cobertura regulatoria global**: si MMG decide consolidar sus operaciones (Las Bambas Perú + Dugald River AUS + Rosebery AUS + Kinsevere RDC) en una sola plataforma, GAIATECH no cubre eso sin esfuerzo significativo.

## Cuándo NO usar GAIATECH M1.0

- Si MMG ya tiene contrato corporativo activo con SAP EHS / Enablon y quiere consolidar todo ahí.
- Si la decisión es centralización global, no innovación local.
- Si la auditoría corporativa exige certificaciones SOC 2 ya emitidas.

## Cuándo SÍ usar GAIATECH M1.0

- Como capa rápida sobre IEM mientras se evalúa la plataforma corporativa global.
- Para el módulo de visión EPP y relaves estructural, donde las comerciales no tienen nativo.
- Para casos con presupuesto restringido (mineras medianas, contratistas).
- Como prueba de concepto antes de comprometer USD 1 M en una comercial.
- Para validar hipótesis con un piloto barato y rápido.

---

## Conclusión

GAIATECH M1.0 no compite con SAP EHS en su terreno. **Compite en velocidad, costo, contextualización y especialización local.** Para Mina Juanita S.A. en el escenario del Caso 13, esa es la combinación que el plan necesita: **acción inmediata, presupuesto razonable, métricas verificables en 90 días**.
