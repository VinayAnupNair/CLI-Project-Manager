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
                        description TEXT NOT NULL,
                        is_complete INTEGER DEFAULT 0,
                        due_date TEXT,
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
        cursor.execute(f"INSERT INTO projects(name, created_at) VALUES(?, ?)",(name, time_convert(datetime.now().isoformat())))
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