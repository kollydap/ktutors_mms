from fastapi import FastAPI, BackgroundTasks
from mms.routers.user_routes import api_router as mms_router
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from mms.database.db_models.wallet_orm import database
import pika, asyncio, threading
from mms.listeners.mms.wallet_listener import auth_listener
from mms.service.wallet_service import user_wallet_creation_listener

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()

    channel.queue_declare(queue="auth_to_mms")
    channel.basic_consume(
        queue="auth_to_mms", on_message_callback=auth_listener, auto_ack=True
    )

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


def get_app():
    
    app = FastAPI(
        title="KTutors Money management Service Routes",
        description=(
            "This routes helps create user profile"
            "for all other services of KTutors Project\t"
        ),
        version="0.0.1",
    )

    app.include_router(mms_router)

    @app.on_event("startup")
    async def startup():
        user_wallet_creation_listener(89)
        await database.connect()
        print(threading.enumerate())
        background_thread = threading.Thread(target=consume_messages)
        background_thread.daemon = True
        background_thread.start()
        print(threading.enumerate())
        print("db connected")

    @app.on_event("shutdown")
    async def shutdown():
        await database.disconnect()
        print("db disconnected")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
