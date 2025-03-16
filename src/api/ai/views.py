from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from src.models import db_helper


router = APIRouter(tags=["AI"])


@router.post("/summarize")
async def get_summarize(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.summarize(session)