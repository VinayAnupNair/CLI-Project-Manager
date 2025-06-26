# 🗂️ Project Manager CLI

A Python-based command-line tool to manage projects and tasks efficiently using SQLite.

---

## 📦 Features

- Create and delete projects  
- Add, list, complete, undo, and delete tasks  
- Sort tasks by name, due date, or priority  
- Edit and view notes for tasks  
- Search tasks by keyword  
- Dynamic task status updates  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/project-manager-cli.git
cd project-manager-cli
```

### 2. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install click
```

### 4. Run the CLI

```bash
python main.py [COMMAND]
```

---

## 📋 Commands

### ✅ Test CLI

```bash
python main.py test
```
> Output: `Project manager working`

---

### 📁 Project Commands

#### Create a new project

```bash
python main.py new-project "ProjectName"
```

#### List all projects

```bash
python main.py list-projects
```

#### Delete a project

```bash
python main.py delete-project "ProjectName"
```

---

### 📌 Task Commands

#### Add a task

```bash
python main.py add-task "ProjectName" "Task Name" --due_date YYYY-MM-DD --priority LOW|MEDIUM|HIGH
```

#### List tasks in a project

```bash
python main.py list-tasks "ProjectName" --sort-by name|due_date|priority
```

#### Mark a task as complete

```bash
python main.py complete "ProjectName" "Task Name"
```

#### Undo task completion

```bash
python main.py undo-complete "ProjectName" "Task Name"
```

#### Delete a task

```bash
python main.py delete-task "ProjectName" "Task Name"
```

---

### 📝 Notes

#### Edit task notes (in your system text editor)

```bash
python main.py edit-notes "ProjectName" "Task Name"
```

---

### 🔍 Search

#### Search for tasks by keyword

```bash
python main.py search-task "ProjectName" "keyword"
```

---

## 📂 Folder Structure

```
project-manager-cli/
│
├── cli.py              # CLI commands defined using Click
├── db.py               # SQLite database logic
├── utils.py            # Helper functions (e.g., open notes, status)
├── main.py             # Entry point to run the CLI
├── notes/              # Stores text note files
└── project_manager.db  # SQLite database file
```

---

## ✍️ Notes Integration

- Notes are plain `.txt` files stored in the `notes/` directory.
- They are opened using your system’s default text editor.
- Each task can be linked to one note file.

---

## 🛠️ Requirements

- Python 3.7+
- `click` library
- Works offline with SQLite

---

## 🔒 Future Features (optional)

- Notifications / Reminders  
- Task tags or labels  
- Project export/import  
- Better note formatting (Markdown support)