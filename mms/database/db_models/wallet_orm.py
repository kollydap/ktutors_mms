import databases
from mms.models.wallet_models import Currency
from sqlalchemy import Column, Integer, String, Enum, Float
import sqlalchemy

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)


metadata = sqlalchemy.MetaData()

Wallet = sqlalchemy.Table(
    "wallet",
    metadata,
    Column(
        "wallet_uid", String, primary_key=True, unique=True, nullable=False, index=True
    ),
    Column("balance", Float, nullable=False, default=0),
    Column("auth_user_uid", String, unique=True, index=True, nullable=False),
    Column("currency", Enum(Currency), nullable=True, default=Currency.USD),
)
Cart = sqlalchemy.Table(
    "cart",
    metadata,
    Column(
        "cart_uid", String, rimary_key=True, unique=True, nullable=False, index=True
    ),
    Column("auth_user_uid", String, index=True, nullable=False),
    Column("product_uid", String, index=True, nullable=True),
)
engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
