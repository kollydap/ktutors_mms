from uuid import UUID
import uuid
from mms.database.db_models.wallet_orm import database
from mms.database.db_models.wallet_orm import Cart as CartDb


async def add_course_to_cart(x_user_uid: UUID, course_uid: UUID, quantity: int = 1):
    # Check if the user has an existing cart
    # existing_cart = await database.fetch_one(
    #     query=CartDb.select().where((CartDb.c.auth_user_uid == x_user_uid))
    # )
    update_query = (
        CartDb.update()
        .where((CartDb.c.auth_user_uid == x_user_uid))
        .values(course_uid=course_uid)
    )
    await database.execute(update_query)


async def create_cart(x_user_uid: UUID):
    query = CartDb.insert().values(
        cart_uid=str(uuid.uuid4()),
        auth_user_uid=x_user_uid,
    )
    await database.execute(query)

    # if existing_cart:
    #     # If the cart already exists, update the quantity
    #     new_quantity = existing_cart['quantity'] + quantity
    #     update_query = (
    #         CartDb.update()
    #         .where(
    #             (CartDb.c.auth_user_uid == x_user_uid)
    #         )
    #         .values(course_uid=course_uid)
    #     )
    #     await database.execute(update_query)
    # else:
    #     # If the cart doesn't exist, create a new one
    #     insert_query = CartDb.insert().values(
    #         cart_uid=str(uuid.uuid4()),
    #         auth_user_uid=x_user_uid,
    #         course_uid=course_uid,
    #         quantity=quantity,
    #     )
    #     await database.execute(insert_query)
