import requests

from .helpers.tools import put, get_info, hashed, check_size, pass_prompt  

path = path.home() / '.wompus' / 'user.conf'
womp_dir = path(__file__).resolve().parent
url = "https://chcohedportal.xyz/wompus"

def logout():
    with open(path, "w") as f:
        json.dump({"api-key": 0, "username": ""})
    print("done.\n'womp -h for help'")

def signup():
    username = input("please enter a username: ")

    if username_check(username):
        print(f"username: {username} already exists please enter another username")
        signup()
    else:
        password = hashed(pass_prompt())
        head = {"womp": "signup"}
        data = {"username": username, "password": password}
        response = requests.post(url, json=data, headers=head)

        if response.status_code == 200:
            data = {"api-key" : response.json()["api-key"], "username": username}
            put(data)
        else:
            print("error while signing up")

def get_key():
    key, username = get_info()
    head = {"X-API-KEY": key, "womp": "get"}
    data = {"username": username, "password": hashed(password(input("enter password: ")))}
    response = requests.post(url,json=data, headers=head)
    
    if response.status_code == 200:
        r_json = response.json()
        user = [r_json["api-key"], r_json["username"]]
        put(user)
        print(f"your key: {user[0]}")
    else:
        print("Incorrect password or username")
        
def change_pass():
    password = input('enter password: ')
    key, username = get_info()
    head = {'X-API-KEY': key, 'womp': 'change'}
    data = {'username': username, "password": hashed(password), "new_password": hashed(pass_prompt())}
    response = requests.post(url, json=data, headers=head)

    if response.status_code == 200:
        r_json = response.json()
        print("password changed")
    else:
        print("password change error")

def check_username(username):
    head = {"womp": "check_username"}
    data = {"username": username}
    response = requests.post(url, json=data, headers=head)
    
    if response.status_code == 200:
        if response.json()["message"]:
            return True
        else:
            return False
    else:
        print(response.status_code)

def dump(filename,name=""):
    key, username = get_info()
    headers = { "X-API-KEY": key, "womp": "dump"}
    name = str(name)

    if name != "":
        name = os.path.basename(filename)
    
    if check_size(filename):
        with open(filename, 'rb') as f:
            f = {"file": (filename, open(filename), 'rb')}

    data = {"name": name, "size"}
    response = requests.post(url, files=files, headers=head, json=data)
    r_json = response.json()

    # could make an error class
    if "error" in r_json:
        if r_json["error"] == 100:
            print(r_json["message"])
            exit(0)
        exit(0)

def flush(code):
    key, username = get_info()
    headers = { "X-API-KEY": key, "womp": "flush"}
    data = {"username": username, "code": code}
    response = requests.get(url, headers=headers)
    r_json = response.json()

    if "error" in r_json:
        if r_json["error"] == 100:
            print(r_json["message"])
            exit(0)
   
        exit(0)

        name = r_json['name']
        size = r_json['size']
        file_content = base64.b64decode(r_json['file'])
   
    with open(name, "wb") as file:
        file.write(file_content)
    
    print(r_json)
    print(f"grabbed file {name} --- {size}")
    
