from fastapi import APIRouter

from .book import router as book_router
from .product import router as product_router

router: APIRouter = APIRouter()

router.include_router(product_router, tags=["Product 🛒"])
router.include_router(book_router, tags=["Book 📚"])
