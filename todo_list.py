# todo_list.py

def load_tasks():
    try:
        with open("todo.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

tasks = load_tasks()

print("1. View tasks")
print("2. Add task")
choice = input("Choose an option: ")

if choice == "1":
    print("\nYour tasks:")
    for t in tasks:
        print("- " + t)
elif choice == "2":
    new = input("Enter new task: ")
    tasks.append(new)
    save_tasks(tasks)
    print("Task added!")
