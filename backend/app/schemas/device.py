from pydantic import BaseModel, ConfigDict


class DeviceCreate(BaseModel):
    device_name: str
    location: str


class DeviceUpdate(BaseModel):
    device_name: str
    location: str


class DeviceResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    device_name: str
    location: str