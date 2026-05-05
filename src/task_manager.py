tasks = []
FILE_NAME = "tasks.txt"

def add_task(task):
    tasks.append({"task": task, "done": False})
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")
        
def list_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                print(f"{i + 1}. {line.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Done\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
            else:
                print("Task cannot be empty")
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            idx = int(input("Task number: ")) - 1
            mark_done(idx)
        elif choice == "4":
            break