from fastapi import APIRouter

from models import ChatRequest, ChatResponse
from services import generate_reply

router = APIRouter()


@router.get("/")
def home():
    return {
        "message": "这是拆分后的 FastAPI 服务"
    }


@router.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = generate_reply(request.message)

    return ChatResponse(
        user_message=request.message,
        reply=reply
    )