from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.analysis.crud import analyze_notes
from src.database import db_helper


router = APIRouter(tags=["Analysis"])


@router.get("/")
async def get_analysis(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await analyze_notes(session)
