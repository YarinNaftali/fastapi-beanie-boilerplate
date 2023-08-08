from beanie import Document, Indexed
import pymongo
from core.schemas.category import Category
from uuid import UUID, uuid4
from pydantic import Field
from typing import Optional

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