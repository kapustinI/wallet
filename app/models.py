from decimal import Decimal

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base


class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(127))
    balance: Mapped[Decimal] = mapped_column(nullable=False, default=0)
