# entry point
from cli import cli
from db import init_db
import sys

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
            print(f"error occured : {e}")    

if __name__ == "__main__":
    init_db()
    if (len(sys.argv) == 1):
        run_interactive()
    else:
        cli()