# command definitions
import click
from db import (
    create_project, projects_list, delete_project, get_id,
    list_task, task_add, get_task_id,
    mark_task_complete, undo_task_complete,
    get_notes_id, search_tasks, task_delete
)
from utils import get_status, open_task_note

@click.group()
def cli():
    pass

@cli.command()
def test():
    click.echo("Project manager working")

@cli.command()
@click.argument("name")
def new_project(name):
    create_project(name)
    click.echo(f"Created Project: {name}")

@cli.command()
@click.argument("name")
def remove_project(name):
    delete_project(name)
    click.echo(f"Deleted Project: {name}")

@cli.command()
def list_projects():
    projects = projects_list()
    if not projects:
        click.echo("No projects currently")
        return
    click.echo("Projects:")
    for pid, name, created in projects:
        click.echo(f"[{pid}] {name} - Created on {created}")

@cli.command()
@click.argument("project_name")
@click.option("--sort-by", default="due_date", help="Sort by: name, due_date, priority")
def list_tasks(project_name, sort_by):
    pid = get_id(project_name)
    if not pid:
        click.echo("Project not found.")
        return
    tasks = list_task(pid[0],sort_by)
    if not tasks:
        click.echo("No tasks found.")
        return

    click.echo(f"Tasks for '{project_name}':")
    for tid, name, is_complete, notes_id, status, due, priority in tasks:
        status = get_status(due)
        done = "✅" if is_complete else "❌"
        note_tag = "📝" if notes_id else ""
        click.echo(f"[{tid}] {name} {done} {note_tag} - {priority} - {status} - Due: {due or 'N/A'}")

@cli.command()
@click.argument("project_name")
@click.argument("task_name")
@click.option("--due_date", default=None, help="Optional due date in YYYY-MM-DD")
@click.option("--priority", default="MEDIUM", help="Priority: LOW, MEDIUM, HIGH")
def add_task(project_name, task_name, due_date, priority):
    pid = get_id(project_name)
    if not pid:
        click.echo("Project not found.")
        return
    task_add(pid[0], task_name, due_date, priority)
    click.echo(f"Added task '{task_name}' to project '{project_name}'. with priority {priority}.,")

@cli.command()
@click.argument('project_name')
@click.argument('task_name')
def complete(project_name, task_name):
    pid = get_id(project_name)
    if not pid:
        click.echo(f"Project '{project_name}' not found")
        return
    tid = get_task_id(project_name, task_name)
    if not tid:
        click.echo(f"Task '{task_name}' not found in Project '{project_name}'")
        return
    mark_task_complete(tid[0])
    click.echo(f"Task '{task_name}' marked as complete.")

@cli.command()
@click.argument('project_name')
@click.argument('task_name')
def undo_complete(project_name, task_name):
    pid = get_id(project_name)
    if not pid:
        click.echo(f"Project '{project_name}' not found")
        return
    tid = get_task_id(project_name, task_name)
    if not tid:
        click.echo(f"Task '{task_name}' not found in Project '{project_name}'")
        return
    undo_task_complete(tid[0])
    click.echo(f"Task '{task_name}' marked as incomplete.")

@cli.command()
@click.argument("project_name")
@click.argument("task_name")
def edit_notes(project_name, task_name):
    pid = get_id(project_name)
    if not pid:
        click.echo(f"Project '{project_name}' not found")
        return
    tid = get_task_id(project_name, task_name)
    if not tid:
        click.echo(f"Task '{task_name}' not found.")
        return

    notes_id = get_notes_id(tid[0])
    if not notes_id:
        click.echo("No notes linked to this task.")
        return

    open_task_note(notes_id)
    click.echo(f"Opened notes for task '{task_name}'.")

@cli.command()
@click.argument("project_name")
@click.argument("keyword")
def search_task(project_name, keyword):
    pid = get_id(project_name)
    if not pid:
        click.echo("Project not found.")
        return
    results = search_tasks(pid[0], keyword)
    if not results:
        click.echo("No matching tasks found.")
        return
    for tid, name, is_complete, status, due in results:
        done = "✅" if is_complete else "❌"
        click.echo(f"[{tid}] {name} {done} - Status: {status} - Due: {due or 'N/A'}")

@cli.command()
@click.argument("project_name")
@click.argument("task_name")
def delete_task(project_name, task_name):
    pid = get_id(project_name)
    if not pid:
        click.echo(f"Project '{project_name}' not found")
        return
    tid = get_task_id(project_name, task_name)
    if not tid:
        click.echo(f"Task '{task_name}' not found in Project '{project_name}'")
        return
    task_delete(tid[0])
    click.echo(f"Task '{task_name}' deleted")


