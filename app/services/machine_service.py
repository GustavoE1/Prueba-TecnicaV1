from sqlalchemy.orm import Session

from app.models.machine import Machine
from app.models.plant import Plant


def create_machine(
    db: Session,
    name: str,
    type: str,
    status: str,
    plant_id: int
) -> Machine | None:
    plant = db.query(Plant).filter(Plant.id == plant_id).first()
    if not plant:
        return None

    new_machine = Machine(
        name=name,
        type=type,
        status=status,
        plant_id=plant_id
    )
    db.add(new_machine)
    db.commit()
    db.refresh(new_machine)
    return new_machine


def get_machine_by_id(db: Session, machine_id: int) -> Machine | None:
    return db.query(Machine).filter(Machine.id == machine_id).first()


def update_machine_status(
    db: Session,
    machine: Machine,
    new_status: str
) -> Machine:
    machine.status = new_status
    db.commit()
    db.refresh(machine)
    return machine