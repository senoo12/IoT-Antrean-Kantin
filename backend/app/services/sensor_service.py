from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sensor_data import SensorData
from app.repository.sensor_repository import SensorRepository
from app.repository.device_repository import DeviceRepository
from app.models.queue_status import QueueStatus
from app.repository.queue_status_repository import QueueStatusRepository
from app.schemas.sensor import SensorDataCreate
from app.utils.datetime import now_jakarta

class SensorService:
    def __init__(self, db: AsyncSession):
        self.sensor_repo = SensorRepository(db)
        self.device_repo = DeviceRepository(db)
        self.queue_status_repo = QueueStatusRepository(db)

    def calculate_queue(self, distance: float):
        if distance > 120:
            return 0.0, "Kosong"

        elif distance >= 50:
            return 0.5, "Ada Antrean"

        return 1.0, "Antrean Panjang"

    async def create(self, payload: SensorDataCreate):
        device = await self.device_repo.get_by_id(payload.device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device tidak ditemukan"
            )

        sensor = SensorData(
            device_id=payload.device_id,
            distance_cm=payload.distance_cm,
            created_at=now_jakarta()
        )

        sensor = await self.sensor_repo.create(sensor)

        score, label = self.calculate_queue(sensor.distance_cm)

        queue_status = QueueStatus(
            sensor_data_id=sensor.id,
            queue_score=score,
            queue_label=label,
            created_at=now_jakarta()
        )

        await self.queue_status_repo.create(queue_status)

        return sensor

    async def get_all(self):

        return await self.sensor_repo.get_all()

    async def get_latest(self):

        latest = await self.sensor_repo.get_latest()

        if not latest:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Belum ada data sensor"
            )

        return latest

    async def get_by_device(self, device_id: int):

        return await self.sensor_repo.get_by_device(device_id)

    async def delete_history(self):

        await self.sensor_repo.delete_all()

        return {
            "message": "History sensor berhasil dihapus"
        }