from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.device import Device


class DeviceRepository:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def create(self, device: Device):

        self.db.add(device)

        await self.db.commit()

        await self.db.refresh(device)

        return device

    async def get_all(self):

        result = await self.db.execute(
            select(Device)
        )

        return result.scalars().all()

    async def get_by_id(self, device_id: int):

        result = await self.db.execute(
            select(Device).where(Device.id == device_id)
        )

        return result.scalar_one_or_none()

    async def update(self, device: Device):

        await self.db.commit()

        await self.db.refresh(device)

        return device

    async def delete(self, device: Device):

        await self.db.delete(device)

        await self.db.commit()