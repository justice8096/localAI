from ollama import chat
from ollama import ChatResponse
from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header':'some-value'}
    )

response = client.chat(model="qwen2.5-coder:32b", messages=[{"role": "user", "content": "What is your version"}])

print(response.message)