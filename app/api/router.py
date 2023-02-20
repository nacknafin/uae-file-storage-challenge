from fastapi import APIRouter

from .views.files import router as files_router

router = APIRouter()

router.include_router(files_router, prefix="/files")
