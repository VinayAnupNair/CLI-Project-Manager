# sqlite logic
import sqlite3
from datetime import datetime, timedelta
import uuid
import os
from utils import time_convert

DB_NAME = "project_manager.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY,
                project_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                is_complete INTEGER DEFAULT 0,
                due_date TEXT,
                priority TEXT,
                created_at TEXT NOT NULL,
                status TEXT,
                notes_id TEXT,
                FOREIGN KEY (project_id) REFERENCES projects(id)
            )
        """)

        conn.commit()


def create_project(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects(name, created_at) VALUES(?, ?)",(name, time_convert(datetime.now().isoformat())))
        conn.commit()

def projects_list():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM projects")
        return cursor.fetchall()

def delete_project(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM projects WHERE name = ?",(name,))
        conn.commit()
def get_id(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM projects WHERE name = ?", (name,))
        return cursor.fetchone()
    
def task_add(project_id, name, due_date=None, priority = "MEDIUM"):
    notes_id = str(uuid.uuid4())
    status = None  # status is optional or can be updated later

    notes_dir = "notes"
    os.makedirs(notes_dir, exist_ok=True)
    file_path = os.path.join(notes_dir, f"{notes_id}.txt")
    with open(file_path, "w") as f:
        f.write("")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO tasks(project_id, name, is_complete, due_date, created_at, status, notes_id, priority)
            VALUES(?, ?, 0, ?, ?, ?, ?, ?)""",
            (project_id, name, due_date, time_convert(datetime.now().isoformat()), status, notes_id, priority))
        conn.commit()

def task_delete(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT notes_id FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        if row and row[0]:
            try:
                os.remove(f"notes/{row[0]}.txt")
            except FileNotFoundError:
                pass  # No file to delete

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
def search_tasks(project_id, keyword):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            Select id, name, is_complete, status, due_date
            FROM tasks
            WHERE project_id = ? AND name LIKE ?""", (project_id, f"%{keyword}%"))
        return cursor.fetchall()
    
def add_priority_column():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'MEDIUM'")
        conn.commit()

    
def mark_task_complete(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET is_complete = 1 WHERE id = ?", (task_id,))
        conn.commit()

def undo_task_complete(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET is_complete = 0 WHERE id = ?", (task_id,))
        conn.commit()

def get_task_id(project_name, task_name):
    with get_connection() as conn:
        pid = get_id(project_name)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE name = ? AND project_id = ?", (task_name,pid[0]))
        return cursor.fetchone()


def list_task(project_id, sort_by="due_date"):
    with get_connection() as conn:
        cursor = conn.cursor()
        allowed = {"name", "due_date", "priority"}
        if sort_by not in allowed:
            sort_by = "due_date"
        cursor.execute(f"""
            SELECT id, name, is_complete, notes_id, status, due_date, priority
            FROM tasks WHERE project_id = ?
            ORDER BY {sort_by} ASC
        """, (project_id,))
        return cursor.fetchall()

def get_notes_id(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT notes_id FROM tasks WHERE id = ?", (task_id,))
        row = cursor.fetchone()
        return row[0] if row else None
    
def get_important_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        limit = (datetime.now()+ timedelta(2)).strftime("%Y-%m-%d") 
        cursor.execute("""
            SELECT tasks.name, tasks.due_date, projects.name
            FROM tasks
            INNER JOIN projects ON tasks.project_id = projects.id
            WHERE tasks.is_complete = 0 AND tasks.due_date < ?
        """, (limit,))
        return cursor.fetchall()

    






