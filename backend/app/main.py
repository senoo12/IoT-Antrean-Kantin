from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.device import router as device_router
from app.api.v1.sensor import router as sensor_router
from app.api.v1.queue_status import router as queue_status_router

app = FastAPI(
    title="IoT Ultrasonic API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(device_router)
app.include_router(sensor_router)
app.include_router(queue_status_router)

@app.get("/")
async def root():
    return {
        "message": "IoT Ultrasonic API"
    }