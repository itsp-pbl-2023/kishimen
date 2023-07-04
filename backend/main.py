from fastapi import FastAPI, Cookie, Response, Request, status
from fastapi.routing import APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from emotion_esimate.emotion_estimate import emotion_estimate
from random_name import random_name
import uuid
from typing import Union

router = APIRouter()


class Image(BaseModel):
    img: str


# image = "/workspace/kishimen/backend/emotion_esimate/data/sad.jpeg"

meeting_map = {}


@router.post("/emotion_estimate")
async def root(image: Image, user_id: Union[str, None] = Cookie(default=None)):
    emotion = emotion_estimate(image.img)
    if user_id is not None:
        for _, meeting in meeting_map.items():
            for usr_id, _ in meeting:
                if usr_id == user_id:
                    meeting[usr_id] = emotion
    return emotion


@router.post("/meeting")
async def post_meeting(response: Response):
    key = random_name()
    if key in meeting_map:
        i = 0
        while key in meeting_map:
            key = random_name() + "_" + str(i)
            i += 1

    user_id = str(uuid.uuid4())
    response.set_cookie("user_id", user_id)
    initial_emotion = 1 / 7
    meeting_map[key] = {}
    meeting_map[key][user_id] = {
        "angry": initial_emotion,
        "disgust": initial_emotion,
        "fear": initial_emotion,
        "happy": initial_emotion,
        "sad": initial_emotion,
        "surprise": initial_emotion,
        "neutral": initial_emotion,
    }

    return {
        "key": key,
    }


class Meeting(BaseModel):
    key: str


@router.post("/meeting/join")
async def join_meeting(meeting: Meeting, response: Response):
    if meeting.key not in meeting_map:
        return JSONResponse(
            content={"message": "meeting not found"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    user_id = str(uuid.uuid4())
    response.set_cookie("user_id", user_id)
    initial_emotion = 1 / 7
    meeting_map[meeting.key][user_id] = {
        "angry": initial_emotion,
        "disgust": initial_emotion,
        "fear": initial_emotion,
        "happy": initial_emotion,
        "sad": initial_emotion,
        "surprise": initial_emotion,
        "neutral": initial_emotion,
    }
    return


@router.get("/meeting/{key}")
async def get_emotion(key: str):
    meeting = meeting_map[key]
    users = 0
    result = {
        "angry": 0,
        "disgust": 0,
        "fear": 0,
        "happy": 0,
        "sad": 0,
        "surprise": 0,
        "neutral": 0,
    }
    for emotion in meeting.values():
        users += 1
        print(emotion)
        for emotion_name, emotion_value in emotion.items():
            result[emotion_name] += emotion_value
    for emotion_name in result.keys():
        result[emotion_name] /= users
    return result


app = FastAPI()


@app.exception_handler(RequestValidationError)
async def handler(request: Request, exc: RequestValidationError):
    print(exc)
    return JSONResponse(
        content={},
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


app.include_router(router, prefix="/api")
