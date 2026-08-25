# Auth endpoints
# ilya_bisec
# Date: 25/08/2026 15:15

from fastapi import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.sql.functions import current_user

from backend.app.core.security import create_access_token


router = APIRouter()

@router.post("/login")
def login():
    token = create_access_token({"sub": "test_user"})
    return {"token": token}