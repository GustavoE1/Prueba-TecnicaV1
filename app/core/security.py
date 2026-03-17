from fastapi import HTTPException, status

from app.core.config import settings


def verify_api_key(api_key: str) -> None:
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida o no proporcionada"
        )