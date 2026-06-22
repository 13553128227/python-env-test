import json
from pathlib import Path


DATA_DIR = Path("data")
HISTORY_FILE = DATA_DIR / "chat_history.json"


def load_history() -> list:
    DATA_DIR.mkdir(exist_ok=True)

    if not HISTORY_FILE.exists():
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_message(user_message: str, reply: str) -> None:
    history = load_history()

    record = {
        "user_message": user_message,
        "reply": reply
    }

    history.append(record)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, ensure_ascii=False, indent=2)