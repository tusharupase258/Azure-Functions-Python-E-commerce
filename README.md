# Azure Functions — Static SPA E‑commerce (Git‑Ready Repo)

Host a **static frontend (HTML/CSS/JS)** from **Azure Functions (Python)** using a single HTTP trigger.
Push this repo to GitHub, then deploy to your Function App via **ZIP Deploy** or **GitHub Actions**.

---

## 📂 Repo Layout
```plaintext
host.json
requirements.txt
.gitignore
public/
  ├── index.html
  ├── styles.css
  ├── app.js
  └── products.json
ServeStatic/
  ├── function.json
  └── __init__.py
.github/workflows/deploy.yml   # (optional) CI/CD via Publish Profile
local.settings.json.example    # local dev only (sample)
```

---

## 🛠 Prerequisites
1) Azure account & an existing **Function App** (Linux/Windows).  
2) **Azure CLI** → https://learn.microsoft.com/cli/azure/install-azure-cli  
3) **Python 3.9–3.10** installed locally.  
4) (Optional) **Azure Functions Core Tools v4** for local run: `npm i -g azure-functions-core-tools@4`  
5) **Git** installed.

---

## 🧩 Quick Start (Local)
```bash
# clone your repo
git clone https://github.com/<you>/<repo>.git
cd <repo>

# create venv (recommended)
python -m venv .venv && . .venv/Scripts/activate  # (Windows)
# source .venv/bin/activate                      # (macOS/Linux)

pip install -r requirements.txt

# optional: run locally if you have func tools
func start
# open http://localhost:7071/
```

---

## 🚀 Deploy via ZIP (Portal/CLI)
> Replace `<RG>` (resource group) and `<APP>` (function app name).

```powershell
# from repo root, create zip (ensure host.json is at zip root)
Compress-Archive -Path * -DestinationPath azure-func-spa.zip -Force

# set required settings (once)
az functionapp config appsettings set `
  --resource-group <RG> `
  --name <APP> `
  --settings FUNCTIONS_WORKER_RUNTIME=python WEBSITE_RUN_FROM_PACKAGE=1

# deploy
az functionapp deployment source config-zip `
  --resource-group <RG> `
  --name <APP> `
  --src azure-func-spa.zip

# open https://<APP>.azurewebsites.net
```

**If you see the blue Functions page** → your ZIP root is wrong. Re‑zip so `host.json` is at the archive root.

---

## 🔁 Deploy via GitHub Actions (CI/CD)
1) In Azure Portal → Function App → **Get Publish Profile** (Download).  
2) In GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**:  
   - Name: `AZUREAPPSERVICE_PUBLISH_PROFILE`  
   - Value: *(paste entire publish profile XML)*
3) Commit & push this repo (workflow is already included).  
4) On push to `main`, the workflow deploys automatically.

---

## 🧪 Verify
- Browse your app URL: `https://<APP>.azurewebsites.net`
- Everything (including `/anything`) should serve your SPA (`index.html`) due to wildcard route.

---

## 🛠 Troubleshooting
- **Function not detected**: ensure ZIP/Git root contains `host.json` and `ServeStatic/` folder.  
- **List functions**:
  ```powershell
  az extension add --name azure-functions
  az functionapp function list --resource-group <RG> --name <APP>
  ```
- **Logs**:
  ```powershell
  az webapp log tail --resource-group <RG> --name <APP>
  ```

---

## 📦 Git Commands (first push)
```bash
git init
git add .
git commit -m "Initial commit: Azure Functions SPA"
git branch -M main
git remote add origin https://github.com/<you>/<repo>.git
git push -u origin main
```
