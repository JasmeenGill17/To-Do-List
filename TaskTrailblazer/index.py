# TO DO LIST
# py filename.py
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    messagebox.showinfo("Success", "Task added successfully!")

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        messagebox.showinfo("Success", f"Task '{removed_task}' removed successfully!")
    else:
        messagebox.showerror("Error", "Invalid task index!")

def list_tasks(tasks):
    if not tasks:
        messagebox.showinfo("Info", "No tasks in the list.")
    else:
        task_list = "\n".join(tasks)
        messagebox.showinfo("Tasks", task_list)

def show_list():
    root1 = tk.Tk()
    list_tasks

def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("Task Trailblazer")

    window_width = 500
    window_height = 600
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    def add_task_callback():
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task:
            add_task(tasks, task)

    def remove_task_callback():
        list_tasks(tasks)
        task_index = simpledialog.askinteger("Remove Task", "Enter the index of the task to remove:")
        if task_index is not None:
            remove_task(tasks, task_index)

    def list_tasks_callback():
        list_tasks(tasks)

    img = tk.PhotoImage(file="todolist.png")
    image_label = tk.Label(root, image=img)
    image_label.pack()

    menu_frame = tk.Frame(root)
    menu_frame.pack()

    add_button = tk.Button(menu_frame, text="Add Task", command=add_task_callback)
    add_button.grid(row=0, column=0, padx=10, pady=10)

    remove_button = tk.Button(menu_frame, text="Remove Task", command=remove_task_callback)
    remove_button.grid(row=6, column=0, padx=10, pady=10)

    list_button = tk.Button(menu_frame, text="List Tasks", command=list_tasks_callback)
    list_button.grid(row=12, column=0, padx=10, pady=10)

    img1 = tk.PhotoImage(file="todolist2.png")
    image_label1 = tk.Label(root, image=img1)
    image_label1.pack()

    exit_button = tk.Button(menu_frame, text="Exit", command=root.quit)
    exit_button.grid(row=18, column=0, padx=10, pady=10)
    
    root.mainloop()

if _name_ == "_main_":
    main()