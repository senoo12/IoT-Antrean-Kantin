from app.models.queue_status import QueueStatus
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, desc
from sqlalchemy.orm import selectinload
from app.models.sensor_data import SensorData


class QueueStatusRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, queue_status: QueueStatus):
        self.db.add(queue_status)
        await self.db.commit()
        await self.db.refresh(queue_status)
        return queue_status

    async def get_all(self):

        result = await self.db.execute(
            select(QueueStatus)
            .options(
                selectinload(QueueStatus.sensor_data)
            )
            .order_by(desc(QueueStatus.created_at))
        )

        return result.scalars().all()

    async def get_latest(self):

        result = await self.db.execute(
            select(QueueStatus)
            .options(
                selectinload(QueueStatus.sensor_data)
            )
            .order_by(desc(QueueStatus.created_at))
            .limit(1)
        )

        return result.scalar_one_or_none()

    async def get_by_device(self, device_id: int):

        result = await self.db.execute(
            select(QueueStatus)
            .join(SensorData)
            .where(SensorData.device_id == device_id)
            .options(
                selectinload(QueueStatus.sensor_data)
            )
            .order_by(desc(QueueStatus.created_at))
        )

        return result.scalars().all()