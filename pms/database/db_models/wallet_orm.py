import databases
from pms.models.user_models import Currency
from sqlalchemy import Column, Integer, String, Enum, Float
import sqlalchemy

# from sqlalchemy.dialects.sqlite import UUID as SQLiteUUID
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
import uuid

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
database = databases.Database(SQLALCHEMY_DATABASE_URL)

UUIDType = (
    String(length=36)
    if "sqlite" in SQLALCHEMY_DATABASE_URL
    else PostgreSQLUUID(as_uuid=True)
)

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

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
