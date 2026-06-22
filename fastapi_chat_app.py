from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "这是我的 FastAPI 服务"
    }


@app.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    return {
        "user_message": user_message,
        "reply": f"你刚才说的是：{user_message}"
    }