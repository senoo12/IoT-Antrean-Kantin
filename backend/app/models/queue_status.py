from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime

from app.core.database import Base
from app.utils.datetime import now_jakarta

class QueueStatus(Base):
    __tablename__ = "queue_status"

    id = Column(Integer, primary_key=True, index=True)

    sensor_data_id = Column(
        Integer,
        ForeignKey("sensor_data.id", ondelete="CASCADE"),
        nullable=False
    )

    queue_score = Column(Float, nullable=False)

    queue_label = Column(String(20), nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=now_jakarta,
        nullable=False
    )

    sensor_data = relationship("SensorData", back_populates="queue_status")