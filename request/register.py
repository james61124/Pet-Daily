import requests
import json

url = "http://107.191.60.115:81/User/Register"

data = {
    'username': 'username',
    'password': 'password',
    'breed': 'breed',
    'petName': 'petName',
    'age': 10,
    'gender': 'gender'
}

headers = {
    "Content-Type": "application/json"
}

data = json.dumps(data)
response = requests.post(url, data=data, headers=headers)

print("Response Content:", response.content)
print("Status Code:", response.status_code)
