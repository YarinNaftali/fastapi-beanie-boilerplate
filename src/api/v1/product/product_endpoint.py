from core.models.product import Product
from uuid import UUID
from fastapi import APIRouter

router = APIRouter(prefix="/product")

@router.get("/")
async def get_products():
    return await Product.get_products()

@router.post("/")
async def create_product(product: Product):
    return await product.create_product()

@router.get("/{product_id}")
async def get_product(product_id: UUID):
    return await Product.find_one(product_id)

@router.delete("/{product_id}")
async def delete_product(product_id: UUID):
    return await Product.delete_product(product_id)

