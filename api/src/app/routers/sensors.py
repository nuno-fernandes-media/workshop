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
    Sensor(
        id=3,
        mac_address="AA:BB:CC:DD:EE:03",
        description="Pressure sensor in server room",
        state="active",
        created_at=datetime.fromisoformat("2025-03-15T09:30:00"),
        updated_at=datetime.fromisoformat("2025-03-28T11:45:00"),
        name="Press-03",
    ),
    Sensor(
        id=4,
        mac_address="AA:BB:CC:DD:EE:04",
        description="Motion detector entrance",
        state="error",
        created_at=datetime.fromisoformat("2025-03-10T16:20:00"),
        updated_at=datetime.fromisoformat("2025-03-30T08:15:00"),
        name="Motion-04",
    ),
    Sensor(
        id=5,
        mac_address="AA:BB:CC:DD:EE:05",
        description="Light sensor conference room",
        state="active",
        created_at=datetime.fromisoformat("2025-03-18T13:45:00"),
        updated_at=datetime.fromisoformat("2025-03-18T13:45:00"),
        name="Light-05",
    ),
    Sensor(
        id=6,
        mac_address="AA:BB:CC:DD:EE:06",
        description="CO2 monitor office floor",
        state="inactive",
        created_at=datetime.fromisoformat("2025-03-12T10:00:00"),
        updated_at=datetime.fromisoformat("2025-03-27T14:30:00"),
        name="CO2-06",
    ),
    Sensor(
        id=7,
        mac_address="AA:BB:CC:DD:EE:07",
        description="Vibration sensor equipment rack",
        state="active",
        created_at=datetime.fromisoformat("2025-03-20T11:15:00"),
        updated_at=datetime.fromisoformat("2025-03-29T16:20:00"),
        name="Vib-07",
    ),
    Sensor(
        id=8,
        mac_address="AA:BB:CC:DD:EE:08",
        description="Water leak detector basement",
        state="active",
        created_at=datetime.fromisoformat("2025-03-08T08:30:00"),
        updated_at=datetime.fromisoformat("2025-03-08T08:30:00"),
        name="Water-08",
    ),
    Sensor(
        id=9,
        mac_address="AA:BB:CC:DD:EE:09",
        description="Smoke detector kitchen area",
        state="error",
        created_at=datetime.fromisoformat("2025-03-14T15:45:00"),
        updated_at=datetime.fromisoformat("2025-03-31T09:10:00"),
        name="Smoke-09",
    ),
    Sensor(
        id=10,
        mac_address="AA:BB:CC:DD:EE:10",
        description="Door sensor main entrance",
        state="inactive",
        created_at=datetime.fromisoformat("2025-03-16T12:00:00"),
        updated_at=datetime.fromisoformat("2025-03-26T17:45:00"),
        name="Door-10",
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
