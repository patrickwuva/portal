import os
import json
import glob
import base64
import shutil 
import getpass
import time
from pathlib import Path

path = path.home() / '.wompus' / 'user.conf'
womp_dir = path(__file__).resolve().parent

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

def hashed(password):
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_bytes.decode('utf-8')

def pass_check(password):
    l = len(password)
    
    if l < 8 or l > 20:
        return False

    return True

def pass_prompt():
    password = getpass.getpass("enter a password between 8-20 characters: ")
    
    if not pass_check(password):
        print(f"invalid password, try again")
        time.sleep(.5)
        pass_prompt()

    password_second = getpass.getpass("re-enter password: ")

    if password_second != password:
        print(f"passwords don't match")
        time.sleep(.5)
        pass_prompt()
    return password



