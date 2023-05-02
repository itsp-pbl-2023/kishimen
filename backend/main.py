from fastapi import FastAPI
from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}

app = FastAPI()
app.include_router(router, prefix="/api")
