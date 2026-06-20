import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)
data = response.json()

print("最终请求地址:", response.url)
print("状态码:", response.status_code)
print("返回数量:", len(data))

for post in data[:3]:
    print(post["id"], post["title"])