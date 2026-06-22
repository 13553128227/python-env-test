def generate_reply(message: str) -> str:
    message = message.strip()

    if message == "":
        return "你还没有输入内容。"

    if "你好" in message:
        return "你好！我是一个模拟 AI 助手。"

    if "你是谁" in message:
        return "我是一个用 FastAPI 写出来的假 AI 助手，现在还没有接入真实大模型。"

    if "API" in message or "api" in message:
        return "API 是程序之间互相通信的接口，常用 JSON 传递数据。"

    return f"我收到了你的消息：{message}"