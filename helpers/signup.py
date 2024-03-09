# lets handle the signup process
import bcrypt
import requests
import getpass
import time
from helpers import key

print("Welcome to portal a simple file sharing program")

def pass_check(password):
    l = len(password)
    
    if l < 8 or l > 20:
        return False

    return True

def hashed(password):
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_bytes.decode('utf-8')


def username_check(username):
    url = "https://chochedportal.xyz/checkuser"
    data = {"username": username}
    response = requests.post(url, json=data)
    
    if response.status_code == 200:
        if response.json()["message"]:
            return True
        else:
            return False
    else:
        print(response.status_code)

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

def signup():
    url = "https://chochedportal.xyz/signup"

    username = input("please enter a username: ")

    if username_check(username):
        print(f"username: {username} already exists please enter another username")
        signup()

    else:
        password = pass_prompt()

        user_info = {"username": username, "password": hashed(password) }
        response = requests.post(url, json=user_info)
                
        if response.status_code == 200:
            data = {"username": user_info["username"], "password": user_info["password"], "api-key" : response.json()["api-key"]}
            key.put(data)
        else:
            print("error while signing up")


