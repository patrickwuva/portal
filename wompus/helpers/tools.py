import os
import json
import glob
import base64
import requests
import shutil 
from pathlib import Path

path = Path.home() / '.wompus' / 'user.conf'
womp_dir = Path(__file__).resolve().parent

def make_config():
    if not path.exists():
        file = womp_dir / 'user.conf'
        path.parent.mkdir(exist_ok=True)
        shutil.copyfile(file, path)

def get_info():
    with open(path, 'r') as file:
        return json.load(file)

def check_key():
    user = get_info()
    if user["username"] == "" or user["api-key"] == 0:
        return False

    return True

def put(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def check_size(filepath):
    max_size = 100 * 1024 * 1024
    file_size = os.path.getsize(filepath)

    if file_size > max_size:
        return False
  
    else:
        return True

def send_file(filename):
    user = get_info()
    headers = { "X-API-KEY": user["api-key"] , "username": user["username"] }
    url = "https://chochedportal.xyz/dump"
    print(f"path: {filename}")
    name = os.path.basename(filename)
    if check_size(filename):
        with open(filename, 'rb') as file:
            files = {"file": (filename, open(filename), 'rb')}

    response = requests.post(url, files=files, headers=headers)
    
    r_json = response.json()

    # could make an error class
    if "error" in r_json:
        if r_json["error"] == 100:
            print(r_json["message"])
            exit(0)
        exit(0)

    print(response.json())

def get_file(code):
    user = get_info()
    
    headers = { "X-API-KEY": user["api-key"] , "username": user["username"], "code": code }
    url = "https://chochedportal.xyz/flush"
    response = requests.get(url, headers=headers)        
    r_json = response.json()

    if "error" in r_json:
        if r_json["error"] == 100:
            print(r_json["message"])
            exit(0)
   
        exit(0)

        name = r_json['name'] 
        file_content = base64.b64decode(r_json['file'])
   
    with open(name, "wb") as file:
        file.write(file_content)
    
    print(r_json)

    print(f"grabbed file {name}")



