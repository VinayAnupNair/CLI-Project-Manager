# data handelling, formatters
from datetime import datetime, timedelta
import os

def get_status(due_date_str):
    if due_date_str == None:
        return "no due date"
    due = datetime.strptime(due_date_str,"%Y-%m-%d")
    now = datetime.now()
    if due < now:
        return "overdue"
    if due <=now + timedelta(days=2):
        return "due soon"
    else:
        return "on track"

def open_task_note(notes_id):
    file_path = f"notes/{notes_id}.txt"
    os.system(f"${{EDITOR:-vim}} {file_path}")

def time_convert(time):
    return time.split('T')[0] + ' ' + time.split('T')[1].split('.')[0]
