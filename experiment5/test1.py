import requests

url = "http://127.0.0.1:9000/avg"
json_body = {
    'data': [
        100,
        2000,
        1.0,
        2
    ]
}

response = requests.post(url, json=json_body)

print(f'status : {response.status_code}')
print(f'data: {response.json()}')
