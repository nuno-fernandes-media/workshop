# 📋 Tarefas do Workshop (API-only, sem testes)

## 0) Branches & Proteções
1. Criar branches: `dev` (default), `staging`, `prod`.
2. Ativar proteção em todos:
   - PR obrigatório, 1 aprovação
   - Dismiss stale reviews
   - Checks obrigatórios (Python CI import check)
3. PR: `chore/BOOT-branches` → `dev` · Labels: `docs 📓`, `Semver-Patch`

## 1) Labels & Template de PR
- Criar labels: `feature ✨`, `bugfix 🐛`, `docs 📓`, `Semver-Major`, `Semver-Minor`, `Semver-Patch` (+ `pre-release 🚀`, `release 🚀` opcional)
- Adicionar `.github/PULL_REQUEST_TEMPLATE.md` (já incluído)
- PR: `docs/LBL-setup` → `dev` · Labels: `docs 📓`, `Semver-Patch`

## 2) Auto-label por prefixo de branch
- Adicionar `label-by-branch.yml` (incluído)
- PR: `feature/CI-labels` → `dev` · Labels: `feature ✨`, `Semver-Patch`

## 3) Exigir Semver num PR
- Adicionar `require-semver.yml` (incluído)
- PR: `feature/CI-semver` → `dev` · Labels: `feature ✨`, `Semver-Patch`

## 4) Versionamento automático (tag ao merge em `prod`)
- Ficheiro `VERSION` começa em `0.1.0`
- Workflow `tag-on-prod.yml` (incluído) lê label Semver do PR mergeado e faz bump + tag
- PR: `feature/CI-versioning` → `dev` · Labels: `feature ✨`, `Semver-Patch`

## 5) Deploy simulado
- `deploy-staging.yml` (push para `staging`) e `deploy-prod.yml` (push para `prod`)
- PR: `feature/CI-deploy` → `dev` · Labels: `feature ✨`, `Semver-Patch`

## 6) CI mínimo (sem testes)
- `python-ci.yml` faz apenas import check da app
- PR: `feature/CI-python` → `dev` · Labels: `feature ✨`, `Semver-Patch`

## 7) Tarefa de API (única)
**Implementar:** `GET /api/sensors/{mac_address}` (case-insensitive, valida MAC `AA:BB:CC:DD:EE:FF`)
- **200** com `Sensor` completo, **404** se não existir
- Pequena docstring no handler
- PR: `feature/API-101-get-sensor-by-mac` → `dev` · Labels: `feature ✨`, `Semver-Minor`

## 8) Fluxo de release
1. `pre-release/v1.0.0` (de `dev`) → PR para `staging` (label `pre-release 🚀`)
2. `release/v1.0.0` (de `staging`) → PR para `prod` (label `release 🚀`)
