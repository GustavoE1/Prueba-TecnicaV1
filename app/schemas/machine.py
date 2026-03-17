from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict


class MachineCreate(BaseModel):
    name: str
    type: str
    status: Literal["operational", "maintenance", "offline"]
    plant_id: int


class MachineStatusUpdate(BaseModel):
    status: Literal["operational", "maintenance", "offline"]


class MachineResponse(BaseModel):
    id: int
    name: str
    type: str
    status: str
    plant_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)