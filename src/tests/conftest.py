import pytest
import asyncio

from database.database import init_mongo

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