# data handelling, formatters
from datetime import datetime

def get_status(due_date_str):
    if due_date_str == None:
        return "no due date"
    due = datetime.strptime(due_date_str,"%Y-%m-%d")
    now = datetime.now()
    if due < now:
        return "overdue"
    if due <=now+2:
        return "due soon"
    else:
        return "on track"