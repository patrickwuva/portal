import os

def check_size(filepath):
    max_size = 100 * 1024 * 1024

    file_size = os.path.getsize(filepath)

    if file_size > max_size:
        return False
    else:
        return True
