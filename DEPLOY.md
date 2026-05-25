# Guía de despliegue

Pasos para publicar el repo en GitHub y desplegar la app Streamlit en la nube.

## 1) Inicializar Git y publicar en GitHub

```powershell
# 1. Posicionarse en el repo
cd "c:\Users\Emanuel\.gemini\antigravity\scratch\n8n\lasbambas-lrac-2026"

# 2. Init local + primer commit
git init -b main
git add .
git status   # revisar que no haya credenciales/secrets antes del commit
git commit -m "init: LRAC governance analysis + GAIATECH M1.0 workflows + Streamlit demo"

# 3. Crear el repo público en GitHub (necesita gh CLI autenticado)
gh repo create emanuelancco/lasbambas-lrac-2026 --public --source=. --remote=origin --push --description "Innovadores en Acción 2026 · Caso 13 LRAC · MMG Las Bambas. Análisis estadístico reproducible, plan de acción ejecutable y 12 workflows GAIATECH M1.0."

# Alternativa si no se tiene gh CLI:
# - Crear el repo manualmente en github.com/new (público, sin README ni gitignore - ya existen)
# - git remote add origin https://github.com/emanuelancco/lasbambas-lrac-2026.git
# - git push -u origin main
```

Una vez subido:
- El badge de CI debería ponerse verde tras unos minutos (GitHub Actions ejecuta los scripts de `analysis/`).
- Verificar que `data/00_data_caso.xlsx` está incluido (el .gitignore actual NO lo excluye).
- Confirmar que `.streamlit/secrets.toml` NO existe en el repo (el .gitignore lo protege).

## 2) Desplegar en Streamlit Community Cloud

1. Ir a <https://share.streamlit.io>.
2. Click en "New app" → "From existing repo".
3. Configurar:
   - **Repository:** `emanuelancco/lasbambas-lrac-2026`
   - **Branch:** `main`
   - **Main file path:** `app/main.py`
   - **App URL (custom):** `lasbambas-lrac-emanuel` (o el alias que prefieras)
4. Click "Deploy" → primer build ~3-5 min.
5. URL final esperada: `https://lasbambas-lrac-emanuel.streamlit.app`.

Si Streamlit Cloud detecta problemas:
- Revisar que `requirements.txt` esté en la raíz del repo.
- Revisar que `app/main.py` exista (sí está).
- Revisar logs en la pestaña "Manage app" de Streamlit Cloud.

## 3) Backup en VPS Gen+

Por si Streamlit Cloud cae el domingo:

```bash
# en el VPS Gen+ 187.77.250.111
ssh emanuel@187.77.250.111
cd /opt/
git clone https://github.com/emanuelancco/lasbambas-lrac-2026.git
cd lasbambas-lrac-2026

# Crear venv y deps
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Levantar Streamlit detrás de nginx o caddy en un puerto libre
streamlit run app/main.py --server.port 8520 --server.headless true --server.address 0.0.0.0

# Configurar subdominio nip.io
# https://lasbambas-lrac.187-77-250-111.nip.io → proxy reverso al :8520
```

## 4) Verificación pre-envío (sábado AM)

- [ ] Repo GitHub público, badge CI verde
- [ ] Streamlit Cloud URL responde HTTP 200 desde móvil
- [ ] Las 3 páginas se renderizan: 📊 Dashboard, 🎯 Simulador, 🤖 Workflows
- [ ] Las URLs están actualizadas en `report/Emanuel Edgar Ancco Guaygua.pdf` (Sección 8 Anexos)
- [ ] Backup en VPS Gen+ levantado y verificado
- [ ] Nombre archivo PDF exacto: `Emanuel Edgar Ancco Guaygua.pdf`

## 5) Comandos útiles posteriores

```powershell
# Levantar Streamlit localmente
streamlit run app/main.py

# Re-correr todos los scripts de análisis
cd analysis
python 01_analisis_completo.py
python 02_figuras.py
python 03_estadistica_inferencial.py
python 04_plan_ejecutable.py

# Recompilar el PDF
cd ../report
pdflatex "Emanuel Edgar Ancco Guaygua.tex"
pdflatex "Emanuel Edgar Ancco Guaygua.tex"
```
