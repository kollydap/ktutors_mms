import mms.listeners.mms.user_actions as useractions
import logging, asyncio
import mms.database.db_handlers.wallet_db_handler as wallet_db_handler
import json

auth_routing_actions = {"user_wallet_created": useractions.user_wallet_create}

LOGGER = logging.getLogger(__name__)


def auth_listener(ch, method, properties, body: str):
    # convert data from byte to string
    data = body.decode("utf-8")
    asyncio.run(auth_routing_actions["user_wallet_created"](data_obj=data))
