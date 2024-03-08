import requests

base = "https://chochedportal.xyz"

data = {"username": "patrick", "password": "test", "api_key": "test"}

response = requests.post(f"{base}/portal", json=data)

if response.status_code == 200:
    print('POST request was successful!')
    print('Response:', response.json())
else:
    print('POST request failed with status code:', response.status_code)

