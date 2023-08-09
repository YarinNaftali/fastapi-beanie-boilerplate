import pymongo
from pydantic import Field
from typing import Optional
from uuid import UUID, uuid4
from beanie import Document, Indexed
from core.schemas.category import Category
from loguru import logger

class Product(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str]
    price: Indexed(float, pymongo.DESCENDING)
    category: Category

    class Settings:
        name = "products"
        indexes = [
            [
                ("name", pymongo.TEXT),
                ("description", pymongo.TEXT),
            ]
        ]

    async def create_product(self):
        if not self.name or not self.price or not self.category:
            logger.error(f"Missing required fields: name, price, or category")
            raise ValueError("Missing required fields: name, price, or category")
        try:
            res = await self.insert()
            logger.info(f"Created product: {res}")
            return res
        except Exception as e:
            logger.error(e)
            raise e
    

    @classmethod
    async def get_products(cls):
        try:
            res = await cls.find_all().to_list()
            logger.info(f"Found {len(res)} products")
            return res
        except Exception as e:
            logger.error(e)
            return []

    @classmethod
    async def get_product(cls, product_id: UUID):
        if not isinstance(product_id, UUID):
            logger.error(f"Invalid product_id: {product_id}")
            raise ValueError("Invalid product_id")
        try:
            res = await cls.find_one(product_id)
            logger.info(f"Found product: {res}")
            return res
        except Exception as e:
            logger.error(e)
            return None

    @classmethod
    async def delete_product(cls, product_id: UUID):
        if not isinstance(product_id, UUID):
            logger.error(f"Invalid product_id: {product_id}")
            raise ValueError("Invalid product_id")
        try:
            res = await cls.find_one(product_id).delete()
            logger.info(f"Deleted product: {res}")
            return res
        except Exception as e:
            logger.error(e)
            return None
