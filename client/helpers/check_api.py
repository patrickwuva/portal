import json
import glob

file = "api.key"

def check_api():
    file = ".portal/api.key"
    if glob.glob(file):
        return True

    else:
        return False
