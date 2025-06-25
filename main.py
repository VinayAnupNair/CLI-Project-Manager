# entry point

import click
from cli import cli
from db import init_db

def run_interactive():
    print("Welcome to the project manager, type 'quit' or 'exit' to exit the program")
    while True:
        try:
            cmd = input("pm >>> ")
            if cmd.lower() in {'quit','exit'}:
                break
            if cmd:
                cli.main(args=cmd.split(), standalone_mode=False)
        except Exception as e:
            print("error occured : {e}")    

if __name__ == "__main__":
    init_db()
    run_interactive()