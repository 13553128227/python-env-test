from fastapi import APIRouter

from database_tools import load_chats, save_chat
from models import ChatRequest, ChatResponse
from services import generate_reply

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = generate_reply(request.message)

    save_chat(
        user_message=request.message,
        reply=reply
    )

    return ChatResponse(
        user_message=request.message,
        reply=reply
    )


@router.get("/history")
def history():
    return load_chats()
