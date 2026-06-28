from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.device import (
    DeviceCreate,
    DeviceUpdate,
    DeviceResponse
)

from app.services.device_service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.post("", response_model=DeviceResponse)
async def create_device(
    payload: DeviceCreate,
    db: AsyncSession = Depends(get_db)
):

    service = DeviceService(db)

    return await service.create(payload)


@router.get("", response_model=list[DeviceResponse])
async def get_all_devices(
    db: AsyncSession = Depends(get_db)
):

    service = DeviceService(db)

    return await service.get_all()


@router.get("/{device_id}", response_model=DeviceResponse)
async def get_device(
    device_id: int,
    db: AsyncSession = Depends(get_db)
):

    service = DeviceService(db)

    return await service.get_by_id(device_id)


@router.put("/{device_id}", response_model=DeviceResponse)
async def update_device(
    device_id: int,
    payload: DeviceUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = DeviceService(db)

    return await service.update(device_id, payload)


@router.delete("/{device_id}")
async def delete_device(
    device_id: int,
    db: AsyncSession = Depends(get_db)
):

    service = DeviceService(db)

    return await service.delete(device_id)