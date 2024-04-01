import click

class command:
    def __init__(self):
        self.file = None
        self.code = None
        self.ctx = None

    def execute(self):
        @click.command(help="""

         Example usage:

            womp --dump/-d hello.txt     # upload a file, returns a 5 minute code
            womp --flush/-f 1234         # download a file, use 4 digit code  
        

        """)
        @click.option('--dump/-d', 'file', type=str, help='send a file')
        @click.option('--flush/-f', 'code', type=click.IntRange(1000, 9999, clamp=False), help='grab file <use 4 digit code>')
        @click.pass_context
        
        def command(ctx, file, code):
            self.ctx = ctx
            self.file = file
            self.code = code

        command()

