# Common Tasks & PRs

## Environment
- **E1** Create branches `dev` (default), `staging`, `prod`; protect all (PR required, 1 approval, checks pass).  
  PR: `chore/BOOT-setup` → `dev` · Labels: `docs 📓` + `Semver-Patch`

## API
- **A1** Validate existing **GET /api/sensors**; add unit test if missing.  
  PR: `feature/API-101-list` → `dev` · `feature ✨` + `Semver-Patch`
- **A2** Validate/add **POST /api/sensors** with conflict test and success test.  
  PR: `feature/API-102-add` → `dev` · `feature ✨` + `Semver-Minor`
- **A3** Add a **new GET** (pick one):  
  - `GET /api/sensors/{id}` OR `GET /api/sensors/by-month/{YYYY-MM}`  
  PR: `feature/API-103-new-get` → `dev` · `feature ✨` + `Semver-Minor`
- **A4** Expose **GET /api/metrics/bayesian-monthly?m=7** (already present, adjust if needed).  
  PR: `feature/API-104-bayesian` → `dev` · `feature ✨` + `Semver-Patch`

## Pipeline
- **P1** Run the pipeline and output table to console.  
  PR: `feature/DATA-201-pipeline` → `dev` · `feature ✨` + `Semver-Patch`
- **P2** Add a **new GET-like option** to CLI (e.g., `--month 2025-03`).  
  PR: `feature/DATA-202-filter` → `dev` · `feature ✨` + `Semver-Patch`
- **P3** Generate **chart** `charts/bayesian_monthly.png` (already implemented); improve labels/legend.  
  PR: `feature/DATA-203-chart` → `dev` · `feature ✨` + `Semver-Patch`

## CI/CD & Versioning
- **C1** Ensure **Python CI** runs (already included) and optionally add coverage.  
  PR: `feature/CI-301-ci` → `dev` · `feature ✨` + `Semver-Patch`
- **C2** Create Actions for **staging** and **prod** deploys (simulated).  
  PR: `feature/CI-302-deploy` → `dev` · `feature ✨` + `Semver-Patch`
- **C3** Add **Semver label enforcement** (included).  
  PR: `feature/CI-303-semver` → `dev` · `feature ✨` + `Semver-Patch`

## Release Flow
- **R1** `pre-release/v1.0.0` → PR → `staging`  
- **R2** `release/v1.0.0` → PR → `prod`

## PR Checklist
- Summary · Changes · How to Test
- Labels: category + **one** `Semver-*`
- CI green (tests + pipeline + chart artifact)
- 1 approval and conversations resolved
