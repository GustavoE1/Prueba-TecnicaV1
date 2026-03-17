from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func

from app.models.machine import Machine
from app.models.plant import Plant


def create_plant(db: Session, name: str, location: str) -> Plant:
    new_plant = Plant(name=name, location=location)
    db.add(new_plant)
    db.commit()
    db.refresh(new_plant)
    return new_plant


def get_all_plants(db: Session):
    results = (
        db.query(
            Plant.id,
            Plant.name,
            Plant.location,
            Plant.created_at,
            func.count(Machine.id).label("machine_count")
        )
        .outerjoin(Machine, Plant.id == Machine.plant_id)
        .group_by(Plant.id, Plant.name, Plant.location, Plant.created_at)
        .all()
    )

    return results


def get_plant_by_id(db: Session, plant_id: int) -> Plant | None:
    return (
        db.query(Plant)
        .options(joinedload(Plant.machines))
        .filter(Plant.id == plant_id)
        .first()
    )