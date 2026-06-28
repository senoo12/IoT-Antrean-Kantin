from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.device import Device
from app.repository.device_repository import DeviceRepository
from app.schemas.device import DeviceCreate, DeviceUpdate
from app.utils.datetime import now_jakarta

class DeviceService:

    def __init__(self, db: AsyncSession):
        self.repo = DeviceRepository(db)

    async def create(self, payload: DeviceCreate):

        device = Device(
            device_name=payload.device_name,
            location=payload.location,
            created_at=now_jakarta()
        )

        return await self.repo.create(device)

    async def get_all(self):

        return await self.repo.get_all()

    async def get_by_id(self, device_id: int):

        device = await self.repo.get_by_id(device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device tidak ditemukan"
            )

        return device

    async def update(
        self,
        device_id: int,
        payload: DeviceUpdate
    ):

        device = await self.repo.get_by_id(device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device tidak ditemukan"
            )

        device.device_name = payload.device_name
        device.location = payload.location

        return await self.repo.update(device)

    async def delete(self, device_id: int):

        device = await self.repo.get_by_id(device_id)

        if not device:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Device tidak ditemukan"
            )

        await self.repo.delete(device)

        return {"message": "Device berhasil dihapus"}