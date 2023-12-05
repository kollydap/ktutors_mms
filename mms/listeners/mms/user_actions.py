import mms.service.wallet_service as wallet_service


async def user_wallet_create(data_obj: str):
    if data_obj:
        auth_user_uid = data_obj
        await wallet_service.user_wallet_creation_listener(user_uid=auth_user_uid)

