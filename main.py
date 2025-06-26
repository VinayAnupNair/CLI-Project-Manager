# entry point
from cli import cli
from db import init_db, get_important_tasks
import sys

def run_interactive():
    print("Welcome to the Project Manager CLI!")
    print("Type '--help' after any command to see options.")
    print("Type 'quit' or 'exit' to exit the program.")
    imp = get_important_tasks()
    if imp:
        print("Important Tasks")
        for name, due, project in imp:
            print(f"name : {name} due : {due} project : {project}")
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