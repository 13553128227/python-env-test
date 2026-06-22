import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

headers = {
    "Accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)

print("最终 URL：", response.url)
print("状态码：", response.status_code)
print("响应类型：", response.headers.get("Content-Type"))

data = response.json()
print("返回数据：", data)
print("返回数据类型：", type(data))
print("返回数量：", len(data))

first_post = data[0]

print("第一篇文章 ID：", first_post["id"])
print("第一篇文章标题：", first_post["title"])