from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.auth import api_key_auth
from app.dependencies.db import get_db
from app.schemas.machine import MachineCreate, MachineResponse, MachineStatusUpdate
from app.services.machine_service import (
    create_machine,
    get_machine_by_id,
    update_machine_status,
)


router = APIRouter(
    prefix="/machines",
    tags=["Machines"],
    dependencies=[Depends(api_key_auth)]
)


@router.post("/", response_model=MachineResponse, status_code=status.HTTP_201_CREATED)
def create_machine_endpoint(payload: MachineCreate, db: Session = Depends(get_db)):
    machine = create_machine(
        db=db,
        name=payload.name,
        type=payload.type,
        status=payload.status,
        plant_id=payload.plant_id
    )

    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="La planta asociada no existe"
        )

    return machine


@router.patch("/{machine_id}/status", response_model=MachineResponse)
def update_machine_status_endpoint(
    machine_id: int,
    payload: MachineStatusUpdate,
    db: Session = Depends(get_db)
):
    machine = get_machine_by_id(db=db, machine_id=machine_id)
    if not machine:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Máquina no encontrada"
        )

    updated_machine = update_machine_status(
        db=db,
        machine=machine,
        new_status=payload.status
    )
    return updated_machine