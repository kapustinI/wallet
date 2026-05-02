
from fastapi import APIRouter, Depends, HTTPException
from app.service import operations as operation_service

from app.schemas import OperationRequest
from app.dependency import get_db
import sqlalchemy.orm as Session

router = APIRouter()



@router.post("/operations/income")
def add_income(operation: OperationRequest, db: Session = Depends(get_db)):
    return operation_service.add_income(db,operation)

@router.post("/operations/expense")
def add_expense(operation: OperationRequest, db: Session = Depends(get_db)):
    return operation_service.add_expense(db,operation)

