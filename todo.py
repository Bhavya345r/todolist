import tkinter as tk
from tkinter import messagebox
from todologic import add_task, remove_task, complete_task, get_pending_tasks, get_completed_tasks

tasks = []

def refresh_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        prefix = "✓" if task["done"] else "○"
        listbox.insert(tk.END, f"{prefix} {task['text']}")
        if task["done"]:
            listbox.itemconfig(i, fg="gray")

def handle_add():
    task_text = entry.get()
    try:
        add_task(tasks, task_text)
        entry.delete(0, tk.END)
        refresh_listbox()
    except ValueError as e:
        messagebox.showwarning("Warning", str(e))

def handle_complete():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Please select a task to mark as complete.")
        return
    try:
        complete_task(tasks, selection[0])
        refresh_listbox()
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def handle_remove():
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Warning", "Please select a task to remove.")
        return
    try:
        remove_task(tasks, selection[0])
        refresh_listbox()
    except IndexError as e:
        messagebox.showerror("Error", str(e))

def show_summary():
    pending = get_pending_tasks(tasks)
    completed = get_completed_tasks(tasks)
    messagebox.showinfo(
        "Summary",
        f"Pending tasks: {len(pending)}\nCompleted tasks: {len(completed)}"
    )

# --- UI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.resizable(False, False)

tk.Label(root, text="To-Do List", font=("Helvetica", 16, "bold")).pack(pady=10)

entry = tk.Entry(root, width=35, font=("Helvetica", 12))
entry.pack(pady=5)

tk.Button(root, text="Add Task", width=20, command=handle_add).pack(pady=3)

listbox = tk.Listbox(root, width=45, height=12, font=("Helvetica", 11))
listbox.pack(pady=10)

tk.Button(root, text="Mark as Complete", width=20, command=handle_complete).pack(pady=3)
tk.Button(root, text="Remove Task", width=20, command=handle_remove).pack(pady=3)
tk.Button(root, text="Show Summary", width=20, command=show_summary).pack(pady=3)

root.mainloop()