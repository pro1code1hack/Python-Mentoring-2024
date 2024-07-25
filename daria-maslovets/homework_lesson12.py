"""
### Task 2: CLI Task Manager
**Objective**: Create a command-line interface (CLI) task manager application that allows users to add, list, and delete tasks.
**Requirements**:
  - Create a virtual environment and install `Pillow` for image processing.
  - Enable users to add new tasks, mark tasks as completed, list all tasks, and delete tasks through command-line arguments.
  - Use the `argparse` or `click` library to handle command-line arguments for different operations (e.g., `--add`, `--complete`, `--list`, `--delete`).
"""


import argparse
import json
import os
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f'Task added: {task}')

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f'Task {task_index} marked as completed.')
    else:
        print('Invalid task index.')

def list_tasks():
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        status = '✓' if task['completed'] else '✗'
        print(f'{index}: [{status}] {task["task"]}')

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task deleted: {removed_task["task"]}')
    else:
        print('Invalid task index.')

def main():
    parser = argparse.ArgumentParser(description='CLI Task Manager')
    parser.add_argument('--add', type=str, help='Add a new task')
    parser.add_argument('--complete', type=int, help='Mark a task as completed by index')
    parser.add_argument('--list', action='store_true', help='List all tasks')
    parser.add_argument('--delete', type=int, help='Delete a task by index')
    args = parser.parse_args()
    if args.add:
        add_task(args.add)
    elif args.complete is not None:
        complete_task(args.complete)
    elif args.list:
        list_tasks()
    elif args.delete is not None:
        delete_task(args.delete)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()








