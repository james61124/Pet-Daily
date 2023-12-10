import requests

url = "http://localhost:81/register/"

data = {
    'username': 'james',
    'password': 'secret'
}

response = requests.post(url, data=data)

print("Response Content:", response.content)
print("Status Code:", response.status_code)