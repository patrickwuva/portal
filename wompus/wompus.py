import argparse
import getpass
import os
from .helpers.tools import check_key, get_file, send_file, make_config
from .helpers.signup import signup 
from .helpers.commands import command
import requests
import base64
import click

def main():
    make_config()
    
    if not check_key():
        signup()
    
    c = command() 
    c.execute()

    if c.file and c.code:
        click.echo("can't run both commands")
        click(c.ctx.get_help())

    elif c.file:
        send_file(c.file)
    
    elif c.code:
        get_file(c.code)

    else:
            print("")
        click(c.ctx.get_help())

if __name__ == "__main__":
    try:
        while True:
            main()
        
    except KeyboardInterrupt:
       exit(0)
