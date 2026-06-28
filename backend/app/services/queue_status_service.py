from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.queue_status_repository import QueueStatus, QueueStatusRepository


class QueueStatusService:

    def __init__(self, db: AsyncSession):
        self.repository = QueueStatusRepository(db)

    async def get_all(self):
        return await self.repository.get_all()

    async def get_latest(self):
        return await self.repository.get_latest()

    async def get_by_device(self, device_id: int):
        return await self.repository.get_by_device(device_id)