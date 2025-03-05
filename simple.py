import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}
data = {
    "model": "qwen2.5:32b",
    "prompt": "Write a short poem about the moon",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.json()['response'])
else:
    print(f"Error: {response.status_code} - {response.text}")