from fastapi import FastAPI, Request, status
from fastapi.routing import APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from emotion_esimate.emotion_estimate import emotion_estimate

router = APIRouter()


class Image(BaseModel):
    img: str


# image = "/workspace/kishimen/backend/emotion_esimate/data/sad.jpeg"


@router.post("/emotion_estimate")
async def root(image: Image):
    emotion = emotion_estimate(image.img)
    return emotion


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(
        content={},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


app.include_router(router, prefix="/api")
