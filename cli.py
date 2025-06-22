# command definitions
import click
from db import create_project, list_projects

@click.group()
def cli():
    pass

@cli.command()
def test():
    cli.echo("project manager working")

@cli.command()
@click.argument("name")
def new_project(name):
    create_project(name)
    click.echo(f"Created Project : {name}")

@cli.command()
def list_projects_cmd():
    projects = list_projects()
    click.echo("project_id\tname\tcreated_at")
    for pid, name, created in projects:
        click.echo(f"[{pid} {name} {created}]")
