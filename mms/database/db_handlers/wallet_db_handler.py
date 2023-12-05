from uuid import UUID
from sqlalchemy import update, insert, select, delete, insert
from mms.database.db_models.wallet_orm import Wallet as WalletDb, Currency
from mms.models.wallet_models import WalletProfile
import logging, uuid
from sqlalchemy import desc
from sqlalchemy.exc import IntegrityError, OperationalError
import random
from mms.service.service_exceptions import (
    DuplicateError,
    NotFoundError,
)
from mms.database.db_models.wallet_orm import database

LOGGER = logging.getLogger(__file__)


async def create_user_wallet(x_user_uid: UUID, **kwargs):
    query = WalletDb.insert().values(
        wallet_uid=str(uuid.uuid4()),
        auth_user_uid=x_user_uid,
        balance=random.randint(1200, 1000000),
        currency=Currency.USD,
    )
    try:
        await database.execute(query)
        new_wallet_query = WalletDb.select().where(
            WalletDb.c.auth_user_uid == x_user_uid
        )
        new_wallet = await database.fetch_one(new_wallet_query)

        return WalletProfile(
            balance=0,
            currency=Currency.USD,
            user_uid=x_user_uid,
            wallet_uid=new_wallet.wallet_uid,
        )

    except IntegrityError as e:
        print(f"Error creating user: {e}")
        return False


async def get_wallet_balance(x_user_uid: int, **kwargs):
    query = WalletDb.select.where(auth_user_uid=x_user_uid)
    result = await database.execute(query)
    print(result)
    if not result:
        raise NotFoundError("Wallet was not found")
    return WalletProfile()


# async def update_user_profile(user_update: UserUpdate, x_user_uid: UUID, **kwargs):
#     user_update_dict = user_update.dict(exclude_none=True)
#     # query = UserDb.update(


# async def delete_user_profile(user_uid: int, **kwargs):
#     # Define a SQLAlchemy DELETE statement with the returning clause
#     delete_query = (
#         delete(UserDb).where(UserDb.auth_user_uid == user_uid).returning(UserDb)
#     )

#     # Execute the DELETE query and fetch the deleted row
#     result = await database.execute(delete_query)

#     # Check if any rows were deleted and return the deleted user info
#     if not result:
#         raise NotFoundError  # Assuming it returns a single row

#     return UserProfile(**result.as_dict())  # User not found or already deleted
