from sqlalchemy import ForeignKey, Float, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.core.database import Base
from app.utils.datetime import now_jakarta

class SensorData(Base):

    __tablename__ = "sensor_data"

    id: Mapped[int] = mapped_column(primary_key=True)

    device_id: Mapped[int] = mapped_column(
        ForeignKey("devices.id")
    )

    distance_cm: Mapped[float] = mapped_column(Float)
    queue_status = relationship(
        "QueueStatus",
        back_populates="sensor_data",
        uselist=False,
        cascade="all, delete-orphan"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=now_jakarta,
        nullable=False
    )