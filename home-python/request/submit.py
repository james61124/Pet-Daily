import requests

url = "http://localhost:8000/Iot/FoodIntake/"

data = {
    'FoodIntake': 12
}

try:
    response = requests.post(url, data=data)
    print("Response Content:", response.content)
    print("Status Code:", response.status_code)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")



