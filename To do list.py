print("====== TO DO LIST ======")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(count, ".", task)
                count += 1

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available to update.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(count, ".", task)
                count += 1

            num = int(input("Enter task number: "))

            if num >= 1 and num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num - 1] = new_task
                print("Task updated.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            count = 1
            for task in tasks:
                print(count, ".", task)
                count += 1

            num = int(input("Enter task number to delete: "))

            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted.")
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thank you for using To Do List.")
        break

    else:
        print("Please enter a valid choice.")