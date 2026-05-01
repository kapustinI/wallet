from fastapi import FastAPI, HTTPException
from app.api.v1.operations import router as operartions_router
from app.api.v1.wallets import router as wallet_router
from app.db import Base, engine
import app.models

app = FastAPI()

app.include_router(wallet_router, prefix="/api/v1", tags = ["wallet"])
app.include_router(operartions_router, prefix="/api/v1", tags = ["operations"])

Base.metadata.create_all(bind=engine)
