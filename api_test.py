import requests

url = "https://www.example.com"
response = requests.get(url)

print("URL:", url)
print("状态码:", response.status_code)
print("响应内容前100个字符:")
print(response.text[:100])