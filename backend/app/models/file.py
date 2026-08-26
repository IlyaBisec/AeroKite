# File
# ilya_bisec
# Date: 25/08/2026 15:07

from sqlalchemy import String, Column, Integer
from app.db.base import Base
import uuid


class File(Base):
    __tablename__ = "files"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    filename = Column(String)
    size = Column(Integer)
    owner_id = Column(String)
    storage_key = Column(String)