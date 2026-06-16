import requests
from utils import show_status

response = requests.get("https://www.example.com")

print(response.status_code)
print(show_status(response.status_code))
print(response.text[:100])