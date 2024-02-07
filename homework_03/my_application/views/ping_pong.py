from fastapi import APIRouter

router = APIRouter()


@router.get("/ping/")
def say_ping_pong():
    return {"message": "pong"}
