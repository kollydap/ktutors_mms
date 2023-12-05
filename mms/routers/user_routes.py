from fastapi import APIRouter, Body
from mms.models.wallet_models import WalletProfile, WalletRecharge
from typing import Annotated
import mms.service.wallet_service as wallet_service
from uuid import UUID


AnProfilePicture = Annotated[UUID, Body(embed=True)]
api_router = APIRouter(tags=["wallet"], prefix="/api/v1/wallet")


@api_router.post("/recharge", response_model=WalletProfile)
async def recharge_walllet(wallet_recharge: WalletRecharge):
    return await wallet_service.recharge_wallet(wallet_recharge=wallet_recharge)
