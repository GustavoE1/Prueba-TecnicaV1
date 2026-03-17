from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.machine import MachineResponse


class PlantCreate(BaseModel):
    name: str
    location: str


class PlantResponse(BaseModel):
    id: int
    name: str
    location: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PlantListResponse(BaseModel):
    id: int
    name: str
    location: str
    created_at: datetime
    machine_count: int

    model_config = ConfigDict(from_attributes=True)


class PlantWithMachinesResponse(BaseModel):
    id: int
    name: str
    location: str
    created_at: datetime
    machines: list[MachineResponse]

    model_config = ConfigDict(from_attributes=True)