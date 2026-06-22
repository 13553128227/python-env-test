import requests

url = "http://127.0.0.1:8000/chat"

payload = {
    "message": "API 是什么"
}

response = requests.post(url, json=payload)

print("状态码：", response.status_code)
print("响应类型：", response.headers.get("Content-Type"))
print("原始文本：", response.text)

data = response.json()

print("用户消息：", data["user_message"])
print("接口回复：", data["reply"])