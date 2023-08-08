from core.models.product import Product
from uuid import UUID
from fastapi import APIRouter

router = APIRouter(prefix="/product")

@router.get("/")
async def get_products():
    return await Product.find_all().to_list()

@router.post("/")
async def create_product(product: Product):
    return await product.insert()

@router.get("/{product_id}")
async def get_product(product_id: UUID):
    return await Product.find_one(product_id)

@router.put("/{product_id}")
async def update_product(product_id: UUID, product: Product):
    return await Product.replace_one(product_id, product)

@router.delete("/{product_id}")
async def delete_product(product_id: UUID):
    return await Product.find_one(product_id).delete()

