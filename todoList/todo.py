tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

    except FileNotFoundError:
        pass

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("task not found")

def view_tasks():
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks in your list")

def save_tasks():
    with open("tasks.txt", "w") as file:
        if tasks:
            for task in tasks:
                file.write(task + '\n')
        

load_tasks()

while True:
    
    print("options: 1. Add task 2. Remove task 3. View tasks 4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        task = input("Input a task: ")
        add_task(task)
        save_tasks()
        print(f'Task "{task}" added')

    elif choice == '2':
        task = input("Input task to remove: ")
        remove_task(task)
        save_tasks()
        print(f'Task "{task}" removed')

    elif choice == '3':
        print("Here are your tasks")
        view_tasks()

    elif choice == '4':
        print("Todo list closed, bye")
        break
