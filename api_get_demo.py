import requests
url="https://jsonplaceholder.typicode.com/posts/1"
response=requests.get(url)
print("状态码：",response.status_code)
print("响应类型：",response.headers.get("Content-Type"))
data=response.json()
print("标题：",data["title"])
print("内容：",data["body"])