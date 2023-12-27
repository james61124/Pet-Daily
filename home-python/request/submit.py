import requests

url = "http://localhost:81/submit/"

response = requests.get(url)

print("Response Content:", response.content)
print("Status Code:", response.status_code)