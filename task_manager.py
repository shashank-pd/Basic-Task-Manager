import datetime
import json

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"{self.title} (Due: {self.due_date}) - {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def view_tasks(self):
        return self.tasks

    def mark_task_complete(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                task.mark_complete()

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            tasks_data = [
                {'title': task.title, 'due_date': task.due_date, 'completed': task.completed}
                for task in self.tasks
            ]
            json.dump(tasks_data, file)

    def load_tasks(self, filename):
        with open(filename, 'r') as file:
            tasks_data = json.load(file)
            self.tasks = [
                Task(data['title'], data['due_date']) for data in tasks_data
            ]
            for task, data in zip(self.tasks, tasks_data):
                if data['completed']:
                    task.mark_complete()

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, due_date)
            task_manager.add_task(task)
        elif choice == '2':
            title = input("Enter task title to delete: ")
            task_manager.delete_task(title)
        elif choice == '3':
            tasks = task_manager.view_tasks()
            for task in tasks:
                print(task)
        elif choice == '4':
            title = input("Enter task title to mark as complete: ")
            task_manager.mark_task_complete(title)
        elif choice == '5':
            filename = input("Enter filename to save tasks: ")
            task_manager.save_tasks(filename)
        elif choice == '6':
            filename = input("Enter filename to load tasks: ")
            task_manager.load_tasks(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
