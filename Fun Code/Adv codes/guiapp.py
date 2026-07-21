import tkinter as tk

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)

root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack()

root.mainloop()
