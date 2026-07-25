import json
import os
import tkinter as tk
from tkinter import messagebox

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def refresh():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        listbox.insert(tk.END, f"{status} {task['task']}")

def add_task():
    text = entry.get().strip()
    if text:
        tasks.append({"task": text, "done": False})
        save_tasks()
        refresh()
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        save_tasks()
        refresh()
    except:
        messagebox.showwarning("Warning", "Select a task.")

def complete_task():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        save_tasks()
        refresh()
    except:
        messagebox.showwarning("Warning", "Select a task.")

tasks = load_tasks()

root = tk.Tk()
root.title("To-Do App")
root.geometry("400x450")

entry = tk.Entry(root, width=35)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()

listbox = tk.Listbox(root, width=45, height=15)
listbox.pack(pady=15)

tk.Button(root, text="Mark Completed", command=complete_task).pack(pady=5)

tk.Button(root, text="Delete Task", command=delete_task).pack()

refresh()

root.mainloop()
