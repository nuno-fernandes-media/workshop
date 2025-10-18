# Simple Python Workshop — API + Data Pipeline (Mock)

- API (FastAPI): list/add sensors, Bayesian monthly metrics
- Pipeline (pandas/matplotlib): Bayesian average per month + chart
- Mock data embedded in code

## Run API
```bash
pip install -r requirements.txt
export PYTHONPATH=api/src
cd api && ./run.sh
# or
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir src
# http://localhost:8000/health
# http://localhost:8000/api/sensors
# http://localhost:8000/api/metrics/bayesian-monthly?m=7
```

## Run Pipeline
```bash
pip install -r requirements.txt
cd pipeline
python compute_bayesian.py --m 7
python compute_bayesian.py --month 2025-03 --m 7
# chart saved to charts/bayesian_monthly.png
```

## Tests
```bash
pip install -r requirements.txt
export PYTHONPATH=api/src
pytest -q
```
