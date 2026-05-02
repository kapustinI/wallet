from fastapi import APIRouter, Depends

from app.service import wallets as wallet_service
from app.schemas import CreateWalletRequest
from app.dependency import get_db
import sqlalchemy.orm as Session

router = APIRouter()

@router.get("/balance")
def get_balance(wallet_name: str | None = None, db: Session = Depends(get_db)):
    return wallet_service.get_wallet(db, wallet_name)

@router.post("/wallets")
def create_wallet(wallet: CreateWalletRequest, db: Session = Depends(get_db)):
    return wallet_service.create_wallet(db, wallet)  