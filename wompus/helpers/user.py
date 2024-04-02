import requests

from .helpers.tools import put, get_info, hashed, check_size 

path = path.home() / '.wompus' / 'user.conf'
womp_dir = path(__file__).resolve().parent
url = "https://chcohedportal.xyz/wompus"

def logout():
    pass

def signup():
    username = input("please enter a username: ")

    if username_check(username):
        print(f"username: {username} already exists please enter another username")
        signup()
    else:
        password = pass_prompt()
        head = {"womp": "signup"}
        data = {"username": username, "password": hashed(password)}
        response = requests.post(url, json=data, headers=head)

        if response.status_code == 200:
            data = {"username": user["username"], "password": user["password"], 
                    "api-key" : response.json()["api-key"]}
            put(data)
        else:
            print("error while signing up")

def get_key():
    username, key = get_info()
    head = {"X-API-KEY", "username": username}
    data = {"username": info["username"],"password": input("enter password: ")}
    response = requests.post(url,json=data, headers=head)
    
    if response.status_code == 200:
        r_json = response.json()
        user = [r_json["username"], r_json["api-key"]]
        put(user)
        print(f"your key: {user[1]}")
    else:
        print("Incorrect password or username")
        
def change_pass():
    data = {"username": 2}

def check_username(username):
    head = {"womp": "check_username"}
    data = {"womp":"check_username", "data": {"username": username}}
    response = requests.post(url, json=data, headers=head)
    
    if response.status_code == 200:
        if response.json()["message"]:
            return True
        else:
            return False
    else:
        print(response.status_code)

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

