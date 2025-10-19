# 🚀 Workshop — GitHub Actions & Repository Setup with FastAPI

Welcome to the workshop!  
Each team will set up a **real GitHub repository**, automate its workflow using **GitHub Actions**, and implement a small **Python API (FastAPI)**.

---

## 🎯 Goal

This workshop focuses on **repository setup and automation**, not complex code.  
You’ll learn to:

- Create and protect branches (`dev`, `staging`, `prod`)
- Set up **labels** and a **Pull Request template**
- Use **GitHub Actions** to:
  - Automatically label PRs by branch prefix (`feature/`, `bugfix/`, etc.)
  - Enforce a **SemVer label** (`Semver-Major`, `Semver-Minor`, `Semver-Patch`)
  - **Automatically version and tag** on merge to `prod`
  - Simulate **deployments** to `staging` and `prod`
- Implement a small **API endpoint** as a final coding exercise

---

## 🧠 Project Context

All teams start from the same base project:
- A simple FastAPI app with:
  - `GET /health` → health check  
  - `GET /api/sensors` → list mock sensors  
  - `POST /api/sensors` → add mock sensor (in-memory only)
- The `Sensor` model looks like this:
  ```json
  {
    "id": 1,
    "mac_address": "AA:BB:CC:DD:EE:01",
    "description": "Temperature probe in lab",
    "state": "active",
    "created_at": "2025-03-21T14:10:00",
    "updated_at": "2025-03-21T14:10:00",
    "name": "Temp-01"
  }
  ```

---

## 🧩 What You’ll Learn

1. How to structure branches (`dev`, `staging`, `prod`)
2. How to automate labels, versioning, and tagging with **GitHub Actions**
3. How to enforce good PR practices (naming, labels, SemVer discipline)
4. How to simulate environment-specific deploys (staging → prod)
5. How to add and document a small FastAPI endpoint

---

## 🧰 Local Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Set PYTHONPATH and run the API
export PYTHONPATH=api/src
./api/run.sh

# Test it
curl http://localhost:8000/health
curl http://localhost:8000/api/sensors
```

---

## 🧑‍💻 Repository Structure

```
.
├── api/
│   ├── run.sh
│   └── src/app/
│       ├── main.py
│       └── routers/
│           ├── health.py
│           └── sensors.py
├── .github/
│   ├── workflows/
│   │   ├── deploy-prod.yml
│   │   ├── deploy-staging.yml
│   │   ├── label-by-branch.yml
│   │   ├── python-ci.yml
│   │   ├── require-semver.yml
│   │   └── tag-on-prod.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── TASKS.md
├── VERSION
└── requirements.txt
```

---

## ⚙️ How to Participate

### 1. Fork the repository
Each team should **fork this template repository** into their own account.  
Recommended naming: `workshop-team-X` (where X is your team number).

### 2. Clone your fork
```bash
git clone https://github.com/<your-username>/workshop-team-X.git
cd workshop-team-X
```

### 3. Follow the `TASKS.md` file
The [`TASKS.md`](./TASKS.md) file lists **all required tasks**, in order:
- Repository setup (branches, protections, labels)
- Add CI/CD workflows under `.github/workflows/`
- Simulated deployments
- API enhancement (`GET /api/sensors/{mac_address}`)

### 4. Create Pull Requests
Each task should be completed via:
- A properly named branch (`feature/...`, `docs/...`, `chore/...`)
- A Pull Request to `dev`
- Correct labels applied (e.g. `feature ✨`, `Semver-Minor`)
- Review by teammates before merging

---

## 🧩 Final Coding Task

**Implement the following endpoint:**
```
GET /api/sensors/{mac_address}
```

Requirements:
- Match `mac_address` **case-insensitively**
- Return 404 if the sensor does not exist
- Validate MAC format (`AA:BB:CC:DD:EE:FF`)
- Use branch `feature/API-101-get-sensor-by-mac` → PR to `dev`
- Labels: `feature ✨`, `Semver-Minor`

---

## 🏁 Success Criteria

✔️ Branches configured with protection rules  
✔️ Labels and PR template set up correctly  
✔️ CI/CD workflows active and passing  
✔️ SemVer labels enforced  
✔️ Version bump + tag on merge to `prod`  
✔️ Simulated staging/prod deploys running  
✔️ Working endpoint: `GET /api/sensors/{mac_address}`  

---

**Have fun, collaborate, and learn!** 💡  
Each team is encouraged to experiment, ask questions, and improve the workflow.
