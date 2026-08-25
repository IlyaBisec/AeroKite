# User
# ilya_bisec
# Date: 25/08/2026 15:06

from sqlalchemy import Column, Integer, String
from backend.app.db.base import Base
import uuid

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)
    password = Column(String)
