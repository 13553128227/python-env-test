import sqlite3
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
DB_FILE = DATA_DIR / "chat_history.db"


def get_connection():
    DATA_DIR.mkdir(exist_ok=True)
    connection = sqlite3.connect(DB_FILE)
    return connection


def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            reply TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def save_chat(user_message: str, reply: str) -> None:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history (user_message, reply)
        VALUES (?, ?)
        """,
        (user_message, reply)
    )

    connection.commit()
    connection.close()


def load_chats() -> list:
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, user_message, reply, created_at
        FROM chat_history
        ORDER BY id DESC
        """
    )

    rows = cursor.fetchall()
    connection.close()

    chats = []

    for row in rows:
        chat = {
            "id": row[0],
            "user_message": row[1],
            "reply": row[2],
            "created_at": row[3]
        }
        chats.append(chat)

    return chats
