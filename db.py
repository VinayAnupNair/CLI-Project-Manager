# sqlite logic
import sqlite3
from datetime import datetime

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
                        notes TEXT,
                        is_complete INTEGER DEFAULT 0,
                        due_date TEXT,
                        status TEXT,
                        created_at TEXT NOT NULL,
                        FOREIGN KEY (project_id) REFERENCES projects(id)
                    )                 
                    """)
        
        conn.commit()
def time_convert(time):
    return time.split('T')[0] + ' ' + time.split('T')[1].split('.')[0]

def create_project(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO projects(name, created_at) VALUES(?, ?)",(name, time_convert(datetime.now().isoformat())))
        conn.commit()

def list_projects():
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
    
def add_task(project_id, name, notes=None, due_date=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO tasks(project_id, name, notes, is_complete, due_date, created_at) 
                          VALUES(?, ?, ?, 0, ?, ?)""",
                       (project_id, name, notes, due_date, time_convert(datetime.now().isoformat())))
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

def get_task_id(task_name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM tasks WHERE name = ?", (task_name,))
        return cursor.fetchone()


def list_task(project_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT id, name, is_complete, notes, status, due_date FROM tasks WHERE project_id = ?""", (project_id,))
        return cursor.fetchall()





