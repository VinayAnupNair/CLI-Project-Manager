# entry point

import click
from cli import cli
from db import init_db

if __name__ == "__main__":
    init_db()
    cli()