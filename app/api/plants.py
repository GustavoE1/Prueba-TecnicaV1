from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.auth import api_key_auth
from app.dependencies.db import get_db
from app.schemas.plant import (
    PlantCreate,
    PlantListResponse,
    PlantResponse,
    PlantWithMachinesResponse,
)
from app.services.plant_service import create_plant, get_all_plants, get_plant_by_id


router = APIRouter(
    prefix="/plants",
    tags=["Plants"],
    dependencies=[Depends(api_key_auth)]
)


@router.post("/", response_model=PlantResponse, status_code=status.HTTP_201_CREATED)
def create_plant_endpoint(payload: PlantCreate, db: Session = Depends(get_db)):
    return create_plant(db=db, name=payload.name, location=payload.location)


@router.get("/", response_model=list[PlantListResponse])
def get_plants_endpoint(db: Session = Depends(get_db)):
    plants = get_all_plants(db=db)
    return plants


@router.get("/{plant_id}", response_model=PlantWithMachinesResponse)
def get_plant_by_id_endpoint(plant_id: int, db: Session = Depends(get_db)):
    plant = get_plant_by_id(db=db, plant_id=plant_id)
    if not plant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Planta no encontrada"
        )
    return plant