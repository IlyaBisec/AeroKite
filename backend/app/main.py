# MAIN
# ilya_bisec
# Date: 25/08/2026 15:18

from fastapi import FastAPI
from backend.app.api.routes.auth import router as auth_router
from backend.app.api.routes.auth import router as files_router
from backend.app.db.base import Base
from backend.app.db.session import engine

# Crate tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AeroKite", description="AeroKite")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(files_router, prefix="/files", tags=["Files"])



