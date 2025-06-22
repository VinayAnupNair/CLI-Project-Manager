# command definitions
import click
from db import create_project, list_projects, delete_project
# local_time = current_time.split('T')[0] + ' ' + current_time.split('T')[1].split('.')[0]

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
@click.argument("name")
def remove_project(name):
    delete_project(name)
    click.echo(f"{name} deleted")

@cli.command()
def list_projects_cmd():
    projects = list_projects()
    if len(projects) == 0:
        click.echo("No projects currently")
        return
    click.echo("Project:")
    for pid, name, created in projects:
        click.echo(f"[{pid}\t{name}\t{created}]")
