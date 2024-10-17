import os

class Task:
    def __init__(self, id, name, description, due_date):
        self.id = id
        self.name = name
        self.description = description
        self.due_date = due_date

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nDescription: {self.description}\nDue Date: {self.due_date}"


class TaskManager:
    def __init__(self, filename):
        self.tasks = []
        self.filename = filename
        self.id_counter = 1
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    id, name, description, due_date = line.strip().split(',')
                    self.tasks.append(Task(int(id), name, description, due_date))
                    self.id_counter = max(self.id_counter, int(id) + 1)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.id},{task.name},{task.description},{task.due_date}\n")

    def create_task(self):
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        due_date = input("Enter task due date: ")
        task = Task(self.id_counter, name, description, due_date)
        self.tasks.append(task)
        self.id_counter += 1
        self.save_tasks()
        print("Task created successfully.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)
                print("--------------------")

    def update_task(self):
        task_id = int(input("Enter task ID to update: "))
        for task in self.tasks:
            if task.id == task_id:
                task.name = input("Enter new task name: ")
                task.description = input("Enter new task description: ")
                task.due_date = input("Enter new task due date: ")
                self.save_tasks()
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self):
        task_id = int(input("Enter task ID to delete: "))
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print("Task deleted successfully.")
                return
        print("Task not found.")


def main():
    filename = "tasks.txt"
    task_manager = TaskManager(filename)
    while True:
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task_manager.create_task()
        elif choice == "2":
            task_manager.read_tasks()
        elif choice == "3":
            task_manager.update_task()
        elif choice == "4":
            task_manager.delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
