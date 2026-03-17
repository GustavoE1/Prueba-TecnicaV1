from fastapi import Header

from app.core.security import verify_api_key


def api_key_auth(x_api_key: str = Header(...)) -> None:
    verify_api_key(x_api_key)