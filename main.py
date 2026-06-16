import requests
from utils import show_status

url = "https://www.example.com"
response = requests.get(url)

print("请求地址：", url)
print("状态码：", response.status_code)
print("状态说明：", show_status(response.status_code))
print("网页前 100 个字符：")
print(response.text[:100])