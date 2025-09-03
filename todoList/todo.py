tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, checked = line.strip().split(",")
                tasks.append({"task": task.strip(), "checked": checked.strip().lower() == "true"})

    except FileNotFoundError:
        pass

load_tasks()


def add_task(task):
    tasks.append({"task": task, "checked": False})
    

def remove_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            tasks.remove(task)

def toggle_task(task_name):
    for task in tasks:
        if task["task"] == task_name:
            task["checked"] = not task["checked"]

def view_tasks():
    if tasks:
        
        for idx, task in enumerate(tasks, 1):
            status ="✓" if task["checked"] else  "▸"
            print(f'{idx}. {task["task"]} [{status}]')
    else:
        print("-------------------------")
        print("No tasks in your list")
        print("-------------------------")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f'{task["task"]} , {task["checked"]}' + '\n')
    

# load_tasks()

while True:

    print("options: 1. Add 2. toggle check  3. Remove task 4. View tasks 5. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        task = input("Input a task: ")
        add_task(task)
        save_tasks()
        print("-------------------------")
        print(f'Task "{task}" added')
        print("-------------------------")

    elif choice == '2':
        task_name = input("Input task to update: ")
        toggle_task(task_name)
        save_tasks()
        print("-------------------------")
        print(f'Task "{task_name}" updated')
        print("-------------------------")

    elif choice == '3':
        task_name = input("Input task to remove: ")
        remove_task(task_name)
        save_tasks()
        print(f'Task "{task_name}" removed')

    elif choice == '4':
        print("-------------------------")
        print("Here are your tasks")
        print("-------------------------")
        view_tasks()

    elif choice == '5':
        print("-------------------------")
        print("Todo list closed, bye")
        print("-------------------------")
        break
