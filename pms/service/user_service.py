import pms.database.db_handlers.user_db_handler as user_db_handler
import uuid
# ========================== listener functions=========================================#


async def user_wallet_creation_listener(user_uid: uuid.UUID):
    await user_db_handler.create_user_wallet(x_user_uid=user_uid)


async def user_profile_deletion_listener(user_uid: int):
    await user_db_handler.delete_user_profile(x_user_uid=user_uid)
