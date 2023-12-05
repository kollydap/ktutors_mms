from pydantic import BaseModel, EmailStr, constr, conlist, Field
from enum import Enum
from uuid import UUID
from typing import Optional
from datetime import datetime


class WalletType(str, Enum):
    DOLLAR = "DOLLAR"
    NAIRA = "NAIRA"


class Currency(str, Enum):
    USD = "USD"


class WalletProfile(BaseModel):
    balance: int
    currency: Currency
    user_uid: UUID
    wallet_uid: UUID


class WalletRecharge(BaseModel):
    amount: int
    currency: Currency


class AddtoCart(BaseModel):
    course_uid: UUID
    user_uid: UUID
    quantity: int
