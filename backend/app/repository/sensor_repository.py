from sqlalchemy import desc
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.sensor_data import SensorData


class SensorRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, sensor: SensorData):

        self.db.add(sensor)

        await self.db.commit()

        await self.db.refresh(sensor)

        return sensor

    async def get_all(self):

        result = await self.db.execute(
            select(SensorData).order_by(
                desc(SensorData.created_at)
            )
        )

        return result.scalars().all()

    async def get_latest(self):

        result = await self.db.execute(
            select(SensorData).order_by(
                desc(SensorData.created_at)
            ).limit(1)
        )

        return result.scalar_one_or_none()

    async def get_by_device(self, device_id: int):

        result = await self.db.execute(
            select(SensorData)
            .where(SensorData.device_id == device_id)
            .order_by(desc(SensorData.created_at))
        )

        return result.scalars().all()

    async def delete_all(self):

        result = await self.db.execute(
            select(SensorData)
        )

        data = result.scalars().all()

        for item in data:
            await self.db.delete(item)

        await self.db.commit()