class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        self.tasks.append(Task(title, description, False))
        print("Task added!")

    def mark_as_completed(self, index):
        if index < 0 or index > len(self.tasks):
            print("Invalid index!")
            return
        self.tasks[index].completed = True
        print("Task marked as completed!")

    def display_tasks_list(self):
        for t in self.tasks:
            print(t.to_string())
    
    def exit(self):
        print("Exiting.")
        exit()

class Task:
    def __init__(self, title, description, completed):
        self.title = title
        self.description = description
        self.completed = completed

    def to_string(self):
        return "===\nTitle: {0}\nDescription: {1}\nCompleted: {2}".format(self.title, self.description, "Yes" if self.completed else "No")


task_manager = TaskManager()
while True:
    print("Task Manager:")
    print("1. Add task")
    print("2. Mark task as completed")
    print("3. Display task list")
    print("4. Exit task manager")

    choice = int(input("Enter choice: "))
    if choice == 1:
        title = input("Enter title: ")
        description = input("Enter description: ")
        task_manager.add_task(title, description)

    elif choice == 2:
        index = int(input("Enter title: "))
        task_manager.mark_as_completed(index)

    elif choice == 3:
        task_manager.display_tasks_list()

    elif choice == 4:
        task_manager.exit()

    else:
        print("Invalid choice.")

    print("\n")

