import os
from pathlib import Path

from openai import OpenAI
from dotenv import load_dotenv

PROJECT_DIR = Path(__file__).resolve().parent
load_dotenv(PROJECT_DIR / ".env")

client = OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url=os.getenv("AI_BASE_URL")
)


def generate_reply(message: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("AI_MODEL"),
        messages=[
            {"role": "system", "content": "你是一个Python学习助手"},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content
