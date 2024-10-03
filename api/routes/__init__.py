from fastapi import APIRouter
from .category import router as category_router
from .call import router as call_router

router = APIRouter()
router.include_router(category_router, prefix="/category", tags=["categories"])
router.include_router(call_router, prefix="/call", tags=["calls"])
