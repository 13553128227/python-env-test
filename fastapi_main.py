from fastapi import FastAPI

from database_tools import init_db
from routes import router

app = FastAPI()

init_db()

app.include_router(router)
