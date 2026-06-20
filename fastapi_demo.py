from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/hello")
def hello():
    return {"message": "你好，这是我的第一个 API"}