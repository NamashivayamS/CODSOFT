# To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i}. {task['title']} [{status}]")

def add_task():
    title = input("Enter the task title: ")
    tasks.append({"title": title, "completed": False})
    print(f"Task '{title}' added to your to-do list.")

def update_task():
    show_tasks()
    task_number = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_number < len(tasks):
        new_title = input("Enter the new title: ")
        tasks[task_number]['title'] = new_title
        print(f"Task {task_number + 1} updated to '{new_title}'.")
    else:
        print("Invalid task number.")

def mark_task_as_done():
    show_tasks()
    task_number = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print(f"Task {task_number + 1} marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    show_tasks()
    task_number = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_number < len(tasks):
        deleted_task = tasks.pop(task_number)
        print(f"Task '{deleted_task['title']}' deleted from your to-do list.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Done")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            mark_task_as_done()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
