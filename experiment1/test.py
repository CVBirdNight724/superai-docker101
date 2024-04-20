import requests

url = "http://127.0.0.1:5000"

response = requests.get(url)

print(f'status : {response.status_code}')
print(f'data: {response.text}')