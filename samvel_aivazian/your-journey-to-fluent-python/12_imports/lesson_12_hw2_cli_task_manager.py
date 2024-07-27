import json
import os

import click

TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)


@click.group()
def cli():
    pass


@cli.command()
@click.argument('task')
def add(task):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    click.echo(f'Task added: {task}')


@cli.command()
def list():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        click.echo('No tasks found.')
    for i, task in enumerate(tasks, start=1):
        status = '✓' if task['completed'] else '✗'
        click.echo(f'{i}. {task["task"]} [{status}]')


@cli.command()
@click.argument('task_number', type=int)
def complete(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        click.echo(f'Task {task_number} marked as completed.')
    else:
        click.echo('Invalid task number.')


@cli.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f'Task deleted: {deleted_task["task"]}')
    else:
        click.echo('Invalid task number.')


if __name__ == '__main__':
    cli()
