from fastapi import FastAPI
from .routers import health, sensors, metrics

def create_app() -> FastAPI:
    app = FastAPI(title="Sensors Workshop API", version="0.1.0")
    app.include_router(health.router)
    app.include_router(sensors.router, prefix="/api")
    app.include_router(metrics.router, prefix="/api")
    return app

app = create_app()
