import requests
import json

url = "http://localhost:8000/User/Login"

data = {
    'username': 'james',
    'password': 'secret'
}

headers = {
    "Content-Type": "application/json"
}

data = json.dumps(data)
response = requests.post(url, data=data, headers=headers)

print("Response Content:", response.content)
print("Status Code:", response.status_code)