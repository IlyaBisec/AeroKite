# Security
# ilya_bisec
# Date: 25/08/2026 15:05

from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "super-secret"
ALGORITHM = "HS256"

def create_access_token(data: dict, to_encode_request: dict):
    to_encode = data.copy()
    epire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": epire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)