FILENAME = "todo.txt"
def load_tasks():
    try:
        with open(FILENAME, 'r') as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        file.writelines(task + "\n" for task in tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        print("\nOptions: [A]dd  [R]emove  [Q]uit")
        choice = input("Choose an option: ").strip().upper()

        if choice == "A":
            task = input("Enter task: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "R":
            num = int(input("Enter task number to remove: "))
            if 0 < num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
        elif choice == "Q":
            break

main()
