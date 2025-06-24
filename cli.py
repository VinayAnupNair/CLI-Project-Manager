# command definitions
import click
from db import create_project, list_projects, delete_project, get_id, list_task
from utils import get_status

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

@cli.command()
@click.argument("project_name")
def list_tasks(project_name):
    pid = get_id(project_name)
    if not pid:
        click.echo("Project not found.")
        return
    tasks = list_task(pid[0])
    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo(f"Tasks for '{project_name}':")
    for tid, notes, name, status, due in tasks:
        status = get_status(due)
        click.echo(f"[{tid}] {name} - {status} - Due: {due or 'N/A'}")
