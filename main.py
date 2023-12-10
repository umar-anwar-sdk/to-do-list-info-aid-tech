import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Task:
    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        # Set background image
        background_image = Image.open("background.png")  # Replace with your image file
        background_image = background_image.resize((300, 300))  # Set the desired width and height
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(master, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        # Apply a style for buttons
        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 12, 'bold'))

        # Task entry fields
        self.title_label = tk.Label(master, text="Title:")
        self.title_label.grid(row=0, column=0, padx=10, pady=10)
        self.title_entry = tk.Entry(master)
        self.title_entry.grid(row=0, column=1, padx=10, pady=10)

        self.description_label = tk.Label(master, text="Description:")
        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.description_entry = tk.Entry(master)
        self.description_entry.grid(row=1, column=1, padx=10, pady=10)

        # Task listbox
        self.task_listbox = tk.Listbox(master, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Buttons
        self.add_button = ttk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)

        self.delete_button = ttk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=1, padx=10, pady=10)

        self.view_button = ttk.Button(master, text="View Tasks", command=self.view_tasks)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.save_button = ttk.Button(master, text="Save Tasks", command=self.save_tasks)
        self.save_button.grid(row=5, column=0, padx=10, pady=10)

        self.load_button = ttk.Button(master, text="Load Tasks", command=self.load_tasks)
        self.load_button.grid(row=5, column=1, padx=10, pady=10)

        self.task_list = []

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()

        if title and description:
            task = Task(title, description, "Incomplete")
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, f"{task.title} - {task.description}")
            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Please enter both title and description.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()

        if selected_index:
            del self.task_list[selected_index[0]]
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showinfo("Error", "Please select a task to delete.")

    def view_tasks(self):
        task_details = "\n".join([f"{task.title} - {task.description} - {task.status}" for task in self.task_list])
        messagebox.showinfo("Tasks", task_details)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.task_list:
                file.write(f"{task.title},{task.description},{task.status}\n")

        messagebox.showinfo("Save", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                lines = file.readlines()
                self.task_list = [Task(*line.strip().split(',')) for line in lines]
                self.task_listbox.delete(0, tk.END)
                for task in self.task_list:
                    self.task_listbox.insert(tk.END, f"{task.title} - {task.description}")
            messagebox.showinfo("Load", "Tasks loaded successfully.")
        except FileNotFoundError:
            messagebox.showinfo("File Not Found", "No saved tasks found.")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")  # Adjust the window size as needed
    app = ToDoListApp(root)
    root.mainloop()
