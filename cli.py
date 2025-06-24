# command definitions
import click
from db import create_project, list_projects, delete_project, get_id, list_task, add_task, get_task_id, mark_task_complete, undo_task_complete
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
    for tid, name, is_complete, notes, status, due in tasks:
        status = get_status(due)
        done = "✅" if is_complete else "❌"
        click.echo(f"[{tid}] {name} {done} - {status} - Due: {due or 'N/A'}")

@cli.command()
@click.argument("project_name")
@click.argument("task_name")
@click.option("--notes", default=None,help="These are the optional notes")
@click.option("--due_date", default=None, help="This is an optional due date")
def add_task_cmd(project_name, task_name, notes, due_date):
    pid = get_id(project_name)
    if not pid:
        click.echo("project not found")
        return
    add_task(pid[0], task_name,notes,due_date)
    click.echo(f"Added task '{task_name}' to project '{project_name}'")

@cli.command
@click.argument('task_name')
def complete_task(task_name):
    tid = get_task_id(task_name)
    mark_task_complete(tid[0])
    click.echo(f"Task {task_name} marked as complete.")

@cli.command
@click.argument('task_name')
def undo_complete_task(task_name):
    tid = get_task_id(task_name)
    undo_task_complete(tid[0])
    click.echo(f"Task {task_name} marked as incomplete.")


