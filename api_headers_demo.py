import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

headers = {
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("状态码:", response.status_code)
print("请求头:", headers)
print("响应内容:", response.json())