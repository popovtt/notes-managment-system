from fastapi import APIRouter

from .notes.views import router as notes_router
from .notes_versions.views import router as versions_router
from .analysis.views import router as analysis_router


router = APIRouter()
router.include_router(router=notes_router, prefix="/notes")
router.include_router(router=versions_router, prefix="/notes-versions")
router.include_router(router=analysis_router, prefix="/analysis")
