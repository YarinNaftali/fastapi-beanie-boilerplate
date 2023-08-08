import pytest
import asyncio

from database.database import init_mongo
from core.settings import Settings

from core.models.product import Product
from core.schemas.category import Category


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="module")
async def beanie_client_fixture():
    await init_mongo()
    yield


@pytest.fixture(scope="module")
def settings():
    return Settings()


@pytest.fixture(scope="module")
def category_chocolate_fixture():
    return Category(
        name="Chocolate", description="A preparation of roasted and ground cacao seeds."
    )


@pytest.fixture(scope="module")
def product_tonybar_fixture(category_chocolate_fixture, beanie_client_fixture):
    return Product(name="Tony's", price=5.95, category=category_chocolate_fixture)


@pytest.fixture(scope="module")
def product_marsbar_fixture(category_chocolate_fixture, beanie_client_fixture):
    return Product(name="Mars", price=1, category=category_chocolate_fixture)
