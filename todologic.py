def add_task(task_list, task):
    """Add a task to the list. Returns updated list."""
    if not task or not task.strip():
        raise ValueError("Task cannot be empty")
    task_list.append({"text": task.strip(), "done": False})
    return task_list


def remove_task(task_list, index):
    """Remove a task by index. Returns updated list."""
    if index < 0 or index >= len(task_list):
        raise IndexError("Task index out of range")
    task_list.pop(index)
    return task_list


def complete_task(task_list, index):
    """Mark a task as done. Returns updated list."""
    if index < 0 or index >= len(task_list):
        raise IndexError("Task index out of range")
    task_list[index]["done"] = True
    return task_list


def get_pending_tasks(task_list):
    """Return only tasks that are not done."""
    return [task for task in task_list if not task["done"]]


def get_completed_tasks(task_list):
    """Return only tasks that are done."""
    return [task for task in task_list if task["done"]]