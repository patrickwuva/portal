import argparse
import getpass
import os
from helpers.tools import check_key, get_file, send_file
from helpers.signup import signup 
import requests
import base64

def main():
    if not check_key():
        signup()

    parser = argparse.ArgumentParser(description="easy file sharing")
    parser.add_argument('-c', '--create', dest='filename', type=str, help="create a portal")
    parser.add_argument('-e', '--enter', dest='code', type=str, help="grab a file")
    args = parser.parse_args()
    
    if args.code:
        get_file(args.code)

    elif args.filename:
        send_file(args.filename)

if __name__ == "__main__":
    main()
