import argparse
import getpass
from helpers import key
from helpers.signup import signup 
from helpers.user import get_info
from helpers import choch
from helpers.cli import get_file, send_file 
import requests
import os
import base64

def main():
    if not key.check():
        signup()

    parser = argparse.ArgumentParser(description="easy file sharing")
    parser.add_argument('-c', '--create', dest='filename', type=str, help="create a portal")
    parser.add_argument('-e', '--enter', action='store_true', help="grab a file")
    args = parser.parse_args()
    
    if args.enter:
        get_file()

    elif args.filename:
        send_file(args.filename)

if __name__ == "__main__":
    main()
