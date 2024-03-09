import json
import glob
import os

home = os.path.expanduser('~')
path = os.path.join(home,'.portal/.info')
def get_key():
    
    with open(path, 'r') as file:
        data = json.load(file)
    
    return data["api-key"]

def check():
    if glob.glob(path):
        return True

    else:
        return False

def put(data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

