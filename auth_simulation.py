import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

expected_key = "fake_key_for_learning"

print("请求头：")
print(headers)

if not api_key:
    print("401 Unauthorized：没有提供 API Key")
elif api_key != expected_key:
    print("401 Unauthorized：API Key 不正确")
else:
    print("200 OK：认证成功，可以继续请求 API")