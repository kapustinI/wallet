from fastapi import HTTPException
from app.repository import wallets as wallets_repository
from app.schemas import OperationRequest


def add_income(operation: OperationRequest):
    if wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code = 404,
            detail = "Wallet {operation.wallet_name} not found"
        )
    
    new_balance = wallets_repository.add_income(operation.name, operation.amount)
    return {
        "message": "Income added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    } 
def add_expense(operation: OperationRequest):
    if wallets_repository.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code = 404,
            detail = "Wallet {operation.wallet_name} not found"
        )
    if operation.amount <= 0:
        raise HTTPException(
            status_code = 400,
            detail = "Amount must be positive"
        )
    balance = wallets_repository.get_wallet_balance_by_name(operation.wallet_name)
    if balance < operation.amount:
        raise HTTPException(
            status_code = 400,
            detail = f"Insufficient founds. Avialable: {balance}"
        )
    new_balance = wallets_repository.add_expense(operation.name, operation.amount)
    return {
        "message": "Expense added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    } 