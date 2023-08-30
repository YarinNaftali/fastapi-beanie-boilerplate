from fastapi import APIRouter
from database.database import init_mongo

from api.v1.product.product_endpoint import router as product_router  # Import product router

router = APIRouter(prefix="/v1")  # Create APIRouter instance

router.include_router(product_router)  # Include product router