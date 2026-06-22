import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "学习 API",
    "body": "我正在学习 requests 的 POST 请求",
    "userId": 1
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print("状态码：", response.status_code)
print("响应类型：", response.headers.get("Content-Type"))

data = response.json()

print("返回数据：", data)
print("标题：", data["title"])
print("内容：", data["body"])