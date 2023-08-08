from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from core.settings import Settings
from core.models.product import Product

settings = Settings()


async def init_mongo():
    # Create Motor client
    client = AsyncIOMotorClient(settings.mongo_uri)
    # Initialize beanie with the Product document class and a database
    await init_beanie(
        database=client[settings.db_name], document_models=[Product]
    )
