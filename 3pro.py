"""3️⃣ To-Do List Application
Features:
✔ Add task
✔ Remove task
✔ Save tasks
✔ Load tasks

Concepts:
File handling
Lists
Exception handling"""

"""
Ye ek complete To-Do List Application hai Python me. Isme:

✅ Add task
✅ Remove task
✅ Save tasks (file me)
✅ Load tasks (file se)
✅ Exception handling
✅ Lists + File handling"""

import json


FILE_NAME = "tasks.json"


def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks available!")

    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def remove_task(tasks):
    show_tasks(tasks)

    try:
        number = int(input("Enter task number to remove: "))

        removed = tasks.pop(number - 1)

        save_tasks(tasks)

        print(f"Removed: {removed}")

    except (ValueError, IndexError):
        print("Invalid task number!")


def main():

    tasks = load_tasks()

    while True:

        print("\n--- TO DO APP ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")


        choice = input("Choose option: ")


        if choice == "1":
            show_tasks(tasks)


        elif choice == "2":
            add_task(tasks)


        elif choice == "3":
            remove_task(tasks)


        elif choice == "4":
            print("Goodbye!")
            break


        else:
            print("Invalid choice!")


main()


