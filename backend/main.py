from fastapi import FastAPI
from fastapi.routing import APIRouter
from emotion_esimate.emotion_estimate import emotion_estimate

router = APIRouter()

image = "/workspace/kishimen/backend/emotion_esimate/data/sad.jpeg"


@router.get("/")
async def root():
    emotion = emotion_estimate(image)
    return emotion


app = FastAPI()
app.include_router(router, prefix="/api")
