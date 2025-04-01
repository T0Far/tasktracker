# Task Tracker for the CLI
This is a command-line interface (CLI) application for managing tasks. This is a project for roadmap.sh. 

## Features

- **Add a Task**: Users can add a new task to their task list by providing a description. Each task is assigned a unique ID and is initially set to the "todo" status.
- **Delete a Task**: Tasks can be removed from the list by specifying the ID.
- **Update a Task**: The description of an existing task can be updated. This requires the task's ID and the new description.
- **List Tasks**: Users can list all tasks or filter them by status. The statuses available for filtering are "all", "done", "todo", and "in-progress".
- **Mark Task as In-Progress**: Tasks can be marked as "in-progress" by providing their ID.
- **Mark Task as Done**: Tasks can be marked as "done" by specifying their ID.

## Project Structure

- **tasktrack.py**: This is the main file containing the implementation of application. It includes:

  - `main()`: The entry point of the application that handles command-line arguments and invokes the appropriate functions.
  - `addtask(new_task: str)`: Adds a new task to the database.
  - `updatetask(id: str)`: Deletes a task from the database.
  - `deletetask(id: str, description: str)`: Updates the description of a task.
  - `markinprogress(id: str)`: Marks a task as "in-progress".
  - `markdone(id: str)`: Marks a task as "done".
  - `listtasks(status: str = 'all')`: Lists tasks and optionally allows filtering.

## Installation and Usage

### **Installation**: 

Clone the project via git:
```bash
git clone https://github.com/T0Far/tasktracker.git
```

### **Usage**:

Move to the directory added after cloning
```bash
cd tasktracker
```

Commands
