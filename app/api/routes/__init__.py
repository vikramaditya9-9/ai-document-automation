"""API routes package"""

from fastapi import APIRouter

router = APIRouter()

from app.api.routes import auth, documents

router.include_router(auth.router)
router.include_router(documents.router)
