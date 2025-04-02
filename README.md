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
  - `updatetask(id: str)`: Updates the description of a task.
  - `deletetask(id: str, description: str)`: Deletes a task from the database.
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

Add a task to the list
```bash
./tasktrack.py add "touch grass"

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    touch grass                                                                                           |  todo           |    2/4/2025 16:31     |   2/4/2025 16:31
```

Updates the description of a task
```bash
./tasktrack.py update 0 "buy some groceries"

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    buy some groceries                                                                                    |  todo           |    2/4/2025 16:31     |   2/4/2025 16:36
```

Deletes a task from the database
```bash
./tasktrack.py delete 0
```

Marks a task as "in-progress".
```bash
./tasktrack.py mark-in-progress 0

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    buy some groceries                                                                                    |  in-progress    |    2/4/2025 16:31     |   2/4/2025 16:41
```

Marks a task as "done".
```bash
./tasktrack.py mark-done 0

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    buy some groceries                                                                                    |  done           |    2/4/2025 16:31     |   2/4/2025 16:43
```

Lists tasks and optionally allows filtering.
```bash
./tasktrack.py list
       
   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    buy some groceries                                                                                    |  done           |    2/4/2025 16:10     |   2/4/2025 16:13
   1   |    finish task tracker                                                                                   |  todo           |    2/4/2025 16:15     |   2/4/2025 16:15
   2   |    walk the dog                                                                                          |  in-progress    |    2/4/2025 16:15     |   2/4/2025 16:18
   3   |    finish cs50                                                                                           |  done           |    2/4/2025 16:16     |   2/4/2025 16:18
   4   |    pay bills                                                                                             |  todo           |    2/4/2025 16:17     |   2/4/2025 16:17
```
```bash
./tasktrack.py list todo

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   1   |    finish task tracker                                                                                   |  todo           |    2/4/2025 16:15     |   2/4/2025 16:15
   4   |    pay bills                                                                                             |  todo           |    2/4/2025 16:17     |   2/4/2025 16:17
```
```bash
./tasktrack.py list in-progress

   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   2   |    walk the dog                                                                                          |  in-progress    |    2/4/2025 16:15     |   2/4/2025 16:18
```
```bash
./tasktrack.py list done
    
   id  |                                                   tasks                                                  |  status         |      Created At       |     Updated At
   0   |    buy some groceries                                                                                    |  done           |    2/4/2025 16:10     |   2/4/2025 16:13
   3   |    finish cs50                                                                                           |  done           |    2/4/2025 16:16     |   2/4/2025 16:18
```
daddy have mercy i am new at this

This is a project from [Roadmap](https://www.roadmap.sh). Click this [link](https://roadmap.sh/projects/task-tracker) to checkout the project
