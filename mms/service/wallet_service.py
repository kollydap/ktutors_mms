import mms.database.db_handlers.wallet_db_handler as wallet_db_handler
from uuid import UUID
from mms.models.wallet_models import WalletRecharge


async def recharge_wallet(x_user_uid: UUID, wallet_recharge: WalletRecharge, **kwargs):
    return


# ========================== listener functions=========================================#


async def user_wallet_creation_listener(user_uid: UUID):
    await wallet_db_handler.create_user_wallet(x_user_uid=user_uid)
