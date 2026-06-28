from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db

from app.schemas.sensor import (
    SensorDataCreate,
    SensorDataResponse
)

from app.services.sensor_service import SensorService

router = APIRouter(
    prefix="/sensor",
    tags=["Sensor"]
)


@router.post("/data", response_model=SensorDataResponse)
async def create_sensor_data(
    payload: SensorDataCreate,
    db: AsyncSession = Depends(get_db)
):

    service = SensorService(db)

    return await service.create(payload)


@router.get("/data", response_model=list[SensorDataResponse])
async def get_all_sensor_data(
    db: AsyncSession = Depends(get_db)
):

    service = SensorService(db)

    return await service.get_all()


@router.get("/latest", response_model=SensorDataResponse)
async def get_latest_sensor(
    db: AsyncSession = Depends(get_db)
):

    service = SensorService(db)

    return await service.get_latest()


@router.get("/device/{device_id}", response_model=list[SensorDataResponse])
async def get_device_history(
    device_id: int,
    db: AsyncSession = Depends(get_db)
):

    service = SensorService(db)

    return await service.get_by_device(device_id)


@router.delete("/history")
async def delete_history(
    db: AsyncSession = Depends(get_db)
):

    service = SensorService(db)

    return await service.delete_history()