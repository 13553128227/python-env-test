import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

response = requests.get(url, params=params)

print("最终 URL：", response.url)
print("状态码：", response.status_code)
print("响应类型：", response.headers.get("Content-Type"))

if response.status_code == 200:
    try:
        data = response.json()

        print("返回数据类型：", type(data))
        print("返回数量：", len(data))
        print("文章 ID：", data.get("id"))
        for post in data[:3]:
            print("文章 ID：", post.get("id"))
            print("文章标题：", post.get("title"))
            print("---")

    except Exception as e:
        print("JSON 解析失败：", e)
        print("原始内容：", response.text[:200])
else:
    print("请求失败，状态码：", response.status_code)
    print("原始内容：", response.text[:200])