import requests

response = requests.get("http://127.0.0.1:8000/json")

# print(response.text)
# print(response.json())
print(response.elapsed)