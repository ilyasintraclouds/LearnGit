tasks = []
FILE_NAME = "tasks.txt"

def add_task(task):
    tasks.append({"task": task, "done": False})
    with open(FILE_NAME, "a") as f:
        f.write(task + "\n")
        
def list_tasks():
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i + 1}. {t['task']} [{status}]")

def mark_done(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Mark Done\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            idx = int(input("Task number: ")) - 1
            mark_done(idx)
        elif choice == "4":
            break