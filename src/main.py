import uvicorn
from fastapi import FastAPI

from src.api import router as api_router

app = FastAPI()
app.include_router(router=api_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
