import requests

url = "http://127.0.0.1:5000/sum"
params = {'num1': 1, 'num2': '9'}

response = requests.get(url, params=params)

print(f'status : {response.status_code}')
print(f'data: {response.text}')