import requests
import base64
from helpers.user import get_info
from helpers import key
from helpers import choch
import os

def send_file(filename):
    user = get_info()
    
    headers = { "X-API-KEY": key.get_key() , "username": user["username"] }
    url = "https://chochedportal.xyz/create"

    name = os.path.basename(filename)
    url = "https://chochedportal.xyz/create"    
    if choch.check_size(filename):
        with open(filename, 'rb') as file:
            files = {"file": (filename, open(filename), 'rb')}

    response = requests.post(url, files=files, headers=headers)
    print(response)

def get_file():
    user = get_info()
    
    headers = { "X-API-KEY": key.get_key() , "username": user["username"] }
    url = "https://chochedportal.xyz/enter"
    response = requests.get(url, headers=headers)        
    name = response.json()['name'] 
    file_content = base64.b64decode(response.json()['file'])
    
    with open("test.txt", "wb") as file:
        file.write(file_content)

    print(response.json())

    print(f"grabbed file {name}")



