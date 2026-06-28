from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.services.queue_status_service import QueueStatusService
from app.schemas.queue_status import QueueStatusResponse

router = APIRouter(
    prefix="/queue-status",
    tags=["Queue Status"]
)


@router.get(
    "/",
    response_model=list[QueueStatusResponse]
)
async def get_all(
    db: AsyncSession = Depends(get_db)
):
    service = QueueStatusService(db)
    return await service.get_all()


@router.get(
    "/latest",
    response_model=QueueStatusResponse
)
async def get_latest(
    db: AsyncSession = Depends(get_db)
):
    service = QueueStatusService(db)
    return await service.get_latest()


@router.get(
    "/device/{device_id}",
    response_model=list[QueueStatusResponse]
)
async def get_by_device(
    device_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = QueueStatusService(db)
    return await service.get_by_device(device_id)