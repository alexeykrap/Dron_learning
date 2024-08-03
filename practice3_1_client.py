import requests
import json

base_url = "http://127.0.0.1:5000"

response = requests.post(url=f"{base_url}/drone/takeoff")
print(f"Код ответа: {response.status_code}")
print(f"Содержимое ответа: {response.json()}")
