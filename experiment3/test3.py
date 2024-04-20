import requests

url = "http://127.0.0.1:5000/avg"
json_body = {
    'datas': [
        100,
        2000,
        1.0,
        2
    ]
}

response = requests.post(url, json=json_body)

print(f'status : {response.status_code}')

if response.status_code == 200:
    print(f'data: {response.json()}')

else:
    print(f'data: {response.text}')