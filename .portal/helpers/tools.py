import os
import json
import glob
import base64
import requests

home = os.path.expanduser('~')
path = os.path.join(home,'.portal/.info')

def get_key():
    
    with open(path, 'r') as file:
        data = json.load(file)
    
    return data["api-key"]

def check_key():
    if glob.glob(path):
        return True

    else:
        return False

def put(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def get_info():
    home = os.path.expanduser('~')
    portal_path = os.path.join(home,'.portal/.info')

    with open(portal_path, 'r') as file:
        return json.load(file)


def check_size(filepath):
    max_size = 100 * 1024 * 1024

    file_size = os.path.getsize(filepath)

    if file_size > max_size:
        return False
    else:
        return True

def send_file(filename):
    user = get_info()
    
    headers = { "X-API-KEY": get_key() , "username": user["username"] }
    url = "https://chochedportal.xyz/create"
    
    print(f"path: {filename}")
    name = os.path.basename(filename)
    
    url = "https://chochedportal.xyz/create"    
    if check_size(filename):
        with open(filename, 'rb') as file:
            files = {"file": (filename, open(filename), 'rb')}

    response = requests.post(url, files=files, headers=headers)
    print(response.json()["code"])

def get_file(code):
    user = get_info()
    
    headers = { "X-API-KEY": get_key() , "username": user["username"], "code": code }
    url = "https://chochedportal.xyz/enter"
    response = requests.get(url, headers=headers)        
    name = response.json()['name'] 
    file_content = base64.b64decode(response.json()['file'])
   
    with open(name, "wb") as file:
        file.write(file_content)

    print(response.json())

    print(f"grabbed file {name}")



