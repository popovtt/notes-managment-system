from fastapi import APIRouter


router = APIRouter(tags=["Notes"])


@router.get("/hello")
async def hello_notes():
    return {"message": "Hello Notes"}
