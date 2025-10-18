from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

router = APIRouter(tags=["sensors"], prefix="/sensors")

class Sensor(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=100)
    sent_at: datetime

_SENSORS: list[Sensor] = [
    Sensor(id=1, name="Temp-01", sent_at=datetime.fromisoformat("2025-01-05T10:00:00")),
    Sensor(id=2, name="Hum-02",  sent_at=datetime.fromisoformat("2025-01-07T12:30:00")),
    Sensor(id=3, name="Temp-03", sent_at=datetime.fromisoformat("2025-02-02T09:15:00")),
    Sensor(id=4, name="CO2-04",  sent_at=datetime.fromisoformat("2025-02-11T18:45:00")),
    Sensor(id=5, name="Temp-05", sent_at=datetime.fromisoformat("2025-03-21T14:10:00")),
    Sensor(id=6, name="Temp-06", sent_at=datetime.fromisoformat("2025-03-22T08:05:00")),
    Sensor(id=7, name="Hum-07",  sent_at=datetime.fromisoformat("2025-03-25T17:20:00")),
    Sensor(id=8, name="Pressure-08", sent_at=datetime.fromisoformat("2025-04-01T06:30:00")),
    Sensor(id=9, name="Light-09", sent_at=datetime.fromisoformat("2025-04-03T11:45:00")),
    Sensor(id=10, name="Motion-10", sent_at=datetime.fromisoformat("2025-04-05T15:20:00")),
    Sensor(id=11, name="Sound-11", sent_at=datetime.fromisoformat("2025-04-08T09:10:00")),
    Sensor(id=12, name="Vibration-12", sent_at=datetime.fromisoformat("2025-04-10T13:55:00")),
    Sensor(id=13, name="Air-Quality-13", sent_at=datetime.fromisoformat("2025-04-12T16:40:00")),
    Sensor(id=14, name="Water-Level-14", sent_at=datetime.fromisoformat("2025-04-15T07:25:00")),
    Sensor(id=15, name="Wind-Speed-15", sent_at=datetime.fromisoformat("2025-04-18T12:15:00")),
    Sensor(id=16, name="UV-Index-16", sent_at=datetime.fromisoformat("2025-04-20T14:30:00")),
    Sensor(id=17, name="Soil-Moisture-17", sent_at=datetime.fromisoformat("2025-04-22T08:45:00")),
    Sensor(id=18, name="Gas-Leak-18", sent_at=datetime.fromisoformat("2025-04-25T19:10:00")),
    Sensor(id=19, name="Smoke-19", sent_at=datetime.fromisoformat("2025-04-28T10:35:00")),
    Sensor(id=20, name="Door-Contact-20", sent_at=datetime.fromisoformat("2025-05-01T22:50:00")),
]

@router.get("/", response_model=List[Sensor])
def list_sensors() -> list[Sensor]:
    return _SENSORS

@router.post("/", response_model=Sensor, status_code=201)
def add_sensor(sensor: Sensor) -> Sensor:
    if any(s.id == sensor.id for s in _SENSORS):
        raise HTTPException(status_code=409, detail="Sensor ID already exists")
    _SENSORS.append(sensor)
    return sensor
