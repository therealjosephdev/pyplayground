# Challenge: To-Do List Manager ✅

tasks = []

print("Welcome to the To-Do List Manager!")
print("-----------------------------------")
print("1. Add a task")
print("2. Remove a task")
print("3. View tasks")
print("4. Clear tasks")
print("5. Exit")
print()

while True:
    choice = input("Enter a choice: ").strip().lower()
    
    if choice == "1":
        task = input("Enter the task to add: ").strip()
        if task in tasks:
            print(f"Task '{task}' is already in the list!")
        else:
            tasks.append(task)
            print(f"Task added: {task}")
        
    elif choice == "2":
        if not tasks:
            print("Your to-do list is empty! Nothing to remove.")
        else:
            task_to_remove = input("Enter the task to remove: ").strip()
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"Task removed: {task_to_remove}")
            else:
                print(f"Task '{task_to_remove}' not found in the list.")
        
    elif choice == "3":
        if not tasks:
            print("Your to-do list is empty!")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif choice == "4":
        tasks.clear()
        print("All tasks cleared!")
        
    elif choice == "5":
        print("Goodbye!")
        break
    
    else:
        print("Invalid command. Please type 1 (Add a task), 2 (Remove a task), 3 (View tasks), 4 (Clear tasks), or 5 (Exit).")