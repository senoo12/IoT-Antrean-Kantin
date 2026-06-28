from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SensorDataCreate(BaseModel):
    device_id: int
    distance_cm: float


class SensorDataResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    device_id: int
    distance_cm: float
    created_at: datetime