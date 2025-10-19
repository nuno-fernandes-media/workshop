from fastapi import FastAPI
from .routers import health, sensors

def create_app() -> FastAPI:
    app = FastAPI(title="Simple Sensors API", version="0.1.0")
    app.include_router(health.router)
    app.include_router(sensors.router, prefix="/api")
    return app

app = create_app()
