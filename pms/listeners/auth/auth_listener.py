import pms.listeners.auth.user_actions as useractions
import logging, asyncio
import pms.database.db_handlers.user_db_handler as user_db_handler
import json
auth_routing_actions = {"user_wallet_created": useractions.user_wallet_create}

LOGGER = logging.getLogger(__name__)


def auth_listener(ch, method, properties, body:str):
    data = json.loads(body)
    asyncio.run(auth_routing_actions["user_wallet_created"](data_obj=data))
   

