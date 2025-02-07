import json
import os
from datetime import datetime

TASKS_FILE = "D:/Python_programs/Assignment/tasks.json"


class TaskManagementSystem:
    def __init__(self):
        self.tasks = self.load_files()

    def load_files(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description, deadline):
        """"Add a Task"""
        try:
            datetime.strptime(deadline,"%Y-%m-%d")
            task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "deadline": deadline,
            "status": "pending",
            }       
        except ValueError:
            print("Please Enter Date in Correct format ")
            return
  
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self, status=None):
        filtered_tasks = self.tasks if status is None else [t for t in self.tasks if t["status"] == status]
        if not filtered_tasks:
            print("No tasks found.")
            return

        print("\nTask List:")
        for task in filtered_tasks:
            print(f"{task['id']}. {task['description']} | Deadline: {task['deadline']} | Status: {task['status']}")
        print()


    def update_task(self, task_id, new_description=None, new_status=None):
        """Update a task's description or status."""
        for task in self.tasks:
            if task["id"] == task_id:
                if new_description:
                    task["description"] = new_description
                if new_status:
                    task["status"] = new_status
                self.save_tasks()
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        """first check the task_id exists or not and then Delete a task by its ID."""
        task_exists = any(task["id"] == task_id for task in self.tasks)
        if not task_exists:
            print(f"Task {task_id} does not exists Please check by opting Option 2")
            return
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        self.save_tasks()
        print("Task deleted successfully!")

    def menu(self):
        """Display the menu along with user input."""
        while True:
            print("\nTask Manager")
            print("1. Add a Task")
            print("2. View All Tasks")
            print("3. View Pending Tasks")
            print("4. View Completed Tasks")
            print("5. Update a Task")
            print("6. Delete a Task")
            print("7. Exit")

            choice = input("Select an option from menu: ")

            if choice == "1":
                description = input("Enter task description: ")
                deadline = input("Enter deadline (YYYY-MM-DD): ")
                if not description or not deadline: 
                    print("Enter tasks correctly!!")
                else:
                    self.add_task(description, deadline)
    
            elif choice == "2":
                self.view_tasks()

            elif choice == "3":
                self.view_tasks(status="pending")

            elif choice == "4":
                self.view_tasks(status="completed")

            elif choice == "5":
                try:
                    task_id = int(input("Enter task ID to update: "))
                    new_description = (input("Enter new description: "))
                    new_status = input("Enter new status (pending/completed, press Enter to skip): ").lower()
                    self.update_task(task_id, new_description or None, new_status or None)

                except:
                    print("Please Enter correct task id and description to update?")

            elif choice == "6":
                try:
                    task_id = int(input("Enter task ID to delete: "))
                    self.delete_task(task_id)
                except:
                    print("Kindly Enter correct ID need to be deleted")

            elif choice == "7":
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    TaskManagementSystem().menu()
