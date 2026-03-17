from fastapi import FastAPI

from app.api.machines import router as machines_router
from app.api.plants import router as plants_router
from app.db.database import Base, engine
from app.models import machine, plant


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Prueba Tecnica Backend API",
    version="1.0.0"
)

app.include_router(plants_router)
app.include_router(machines_router)