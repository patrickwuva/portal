import argparse
import click
import getpass
import os
from .helpers.tools import check_info, make_config
from .helpers.user import signup, logout, login, get_key, change_pass, flush, dump  
import requests
import base64

@click.command(
    context_settings=dict(help_option_names=['-h', '--help']),
    help="""
    Example usage:
        womp --dump/-d hello.txt     # upload a file, returns a 5 minute code
        womp --flush/-f 1234         # download a file, use 4 digit code  
    """)
@click.option('--dump', '-d', 'file', type=str, help='send a file')
@click.option('--flush', '-f', 'code', type=click.IntRange(1000, 9999, clamp=False), help='grab file <use 4 digit code>')
@click.option('--user', '-u', 'user', type=str, help='user configuration')
@click.option('')
@click.pass_context
    
def main(ctx, file, code):
    make_config()
    
    if not check_key():
        signup()

    if file or code:
        if file and code:
            click.echo("can't run both commands")
            click.echo(ctx.get_help())

        elif file:
            dump(file)
        elif code:
            flush(code)
        else:
            click.echo(ctx.get_help())
    elif user:
        if signin:
            pass
        elif signup:
            pass
        elif logout:
            pass
        elif change:
            pass
        elif get:
            pass
    else:
        click.echo("Usage: womp [OPTION]\nTry 'womp -h' for help\n")

if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
       exit(0)
