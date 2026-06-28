from pydantic import BaseModel
from datetime import datetime


class QueueStatusResponse(BaseModel):
    id: int
    sensor_data_id: int
    queue_score: float
    queue_label: str
    created_at: datetime

    class Config:
        from_attributes = True