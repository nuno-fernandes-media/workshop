from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Literal
from datetime import datetime
import re

router = APIRouter(tags=["sensors"], prefix="/sensors")

MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")

class Sensor(BaseModel):
    id: int
    mac_address: str = Field(..., description="MAC address in form AA:BB:CC:DD:EE:FF")
    description: str = Field(min_length=1, max_length=200)
    state: Literal["active", "inactive", "error"]
    created_at: datetime
    updated_at: datetime
    name: str = Field(min_length=1, max_length=100)

    @classmethod
    def validate_mac(cls, v: str) -> str:
        if not MAC_REGEX.match(v):
            raise ValueError("Invalid MAC address format")
        return v

    @classmethod
    def model_validate(cls, obj):
        if isinstance(obj, dict) and "mac_address" in obj:
            obj = dict(obj)
            cls.validate_mac(obj["mac_address"])
        return super().model_validate(obj)

_SENSORS: list[Sensor] = [
    Sensor(
        id=1,
        mac_address="AA:BB:CC:DD:EE:01",
        description="Temperature probe in lab",
        state="active",
        created_at=datetime.fromisoformat("2025-03-21T14:10:00"),
        updated_at=datetime.fromisoformat("2025-03-21T14:10:00"),
        name="Temp-01",
    ),
    Sensor(
        id=2,
        mac_address="AA:BB:CC:DD:EE:02",
        description="Humidity sensor corridor",
        state="inactive",
        created_at=datetime.fromisoformat("2025-03-25T17:20:00"),
        updated_at=datetime.fromisoformat("2025-03-25T17:20:00"),
        name="Hum-02",
    ),
]

@router.get("/", response_model=List[Sensor])
def list_sensors() -> list[Sensor]:
    return _SENSORS

@router.post("/", response_model=Sensor, status_code=201)
def add_sensor(sensor: Sensor) -> Sensor:
    if any(s.id == sensor.id for s in _SENSORS):
        raise HTTPException(status_code=409, detail="Sensor ID already exists")
    if any(s.mac_address.lower() == sensor.mac_address.lower() for s in _SENSORS):
        raise HTTPException(status_code=409, detail="Sensor MAC already exists")
    _SENSORS.append(sensor)
    return sensor

# Teams must implement:
#   GET /api/sensors/{mac_address}
# Case-insensitive search; return 404 if not found.
