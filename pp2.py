import tkinter as tk
from tkinter import simpledialog

class TaskManager:
    def create_task_manager(filename):
        task_manager = TaskManager()
        task_manager.tasks = []
        task_manager.filename = filename
        task_manager.load_tasks()
        return task_manager

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def edit_task(self, index, description):
        if index < len(self.tasks):
            self.tasks[index].description = description
            self.save_tasks()
        else:
            print("Invalid task index")

    def delete_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Invalid task index")

    def mark_task_as_complete(self, index):
        if index < len(self.tasks):
            self.tasks[index].mark_as_complete()
            self.save_tasks()
        else:
            print("Invalid task index")

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description},{task.completed}\n")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    description, completed = line.strip().split(",")
                    task = Task(description)
                    task.completed = completed == "True"
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

class Task:
    def __new__(cls, description):
        task = super(Task, cls).__new__(cls)
        task.description = description
        task.completed = False
        return task

    def mark_as_complete(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.description} - {status}"

class TaskManagerGUI:
    @classmethod
    def create_task_manager_gui(cls, filename):
        task_manager_gui = cls()
        task_manager_gui.task_manager = TaskManager.create_task_manager(filename)
        task_manager_gui.window = tk.Tk()
        task_manager_gui.window.title("Task Manager")
        task_manager_gui.window.geometry("500x500")
        

        

        task_manager_gui.task_listbox = tk.Listbox(task_manager_gui.window, width=40)
        task_manager_gui.task_listbox.pack()

        task_manager_gui.add_button = tk.Button(task_manager_gui.window, text="Add Task", command=task_manager_gui.add_task_callback)
        task_manager_gui.add_button.pack()

        task_manager_gui.edit_button = tk.Button(task_manager_gui.window, text="Edit Task", command=task_manager_gui.edit_task_callback)
        task_manager_gui.edit_button.pack()

        task_manager_gui.delete_button = tk.Button(task_manager_gui.window, text="Delete Task", command=task_manager_gui.delete_task_callback)
        task_manager_gui.delete_button.pack()

        task_manager_gui.mark_complete_button = tk.Button(task_manager_gui.window, text="Mark Task as Complete", command=task_manager_gui.mark_task_as_complete_callback)
        task_manager_gui.mark_complete_button.pack()

        task_manager_gui.display_tasks()

        return task_manager_gui

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def add_task_callback(self):
        description = simpledialog.askstring("Add Task", "Enter task description")
        if description:
            self.task_manager.add_task(description)
            self.display_tasks()

    def edit_task_callback(self):
        index = simpledialog.askinteger("Edit Task", "Enter task index")
        if index:
            description = simpledialog.askstring("Edit Task", "Enter new task description")
            if description:
                self.task_manager.edit_task(index - 1, description)
                self.display_tasks()

    def delete_task_callback(self):
        index = simpledialog.askinteger("Delete Task", "Enter task index")
        if index:
            self.task_manager.delete_task(index - 1)
            self.display_tasks()

    def mark_task_as_complete_callback(self):
        index = simpledialog.askinteger("Mark Task as Complete", "Enter task index")
        if index:
            self.task_manager.mark_task_as_complete(index - 1)
            self.display_tasks()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    task_manager_gui = TaskManagerGUI.create_task_manager_gui("tasks.txt")
    task_manager_gui.run()