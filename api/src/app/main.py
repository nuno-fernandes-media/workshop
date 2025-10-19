import os
from fastapi import FastAPI
from .routers import health, sensors

def create_app() -> FastAPI:
    # Get environment variables with defaults
    api_title = os.getenv("API_TITLE", "Sensor Workshop API")
    api_version = os.getenv("API_VERSION", "1.0.0")
    api_env = os.getenv("API_ENV", "development")
    
    app = FastAPI(
        title=api_title,
        version=api_version,
        description=f"Sensor management API running in {api_env} environment"
    )
    
    app.include_router(health.router)
    app.include_router(sensors.router, prefix="/api")
    
    return app

app = create_app()
