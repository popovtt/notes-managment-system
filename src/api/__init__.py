from fastapi import APIRouter
from .notes.views import router as notes_router
from .notes_versions.views import router as versions_router


router = APIRouter()
router.include_router(router=notes_router, prefix="/notes")
router.include_router(router=versions_router, prefix="/notes-versions")
