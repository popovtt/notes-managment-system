from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import db_helper
from ..notes import crud


router = APIRouter(tags=["Notes"])


@router.get("/notes")
async def get_notes(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.read_notes(session=session)


@router.get("/hello")
async def hello_notes():
    return {"message": "Hello Notes"}
