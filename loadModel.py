from ollama import chat
from ollama import ChatResponse
from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header':'some-value'}
    )

response = client.generate(model='deepseek-r1:32b')

print(response.message)