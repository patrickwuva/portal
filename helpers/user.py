import json
import os

def get_info():
    home = os.path.expanduser('~')
    portal_path = os.path.join(home,'.portal/.info')

    with open(portal_path, 'r') as file:
        return json.load(file)
