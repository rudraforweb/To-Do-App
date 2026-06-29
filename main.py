print("Welcome to To Do List v0.1")
task_list = []

while True:
    print("""
        MENU:
        1. Add Task
        2. View Tasks
        3. Mark Task as Complete
        4. Exit
        """)
    option = input("Please select an option (1-4): ")
    if option == "1":
        task = input("Enter the task you want to add: ")
        task_list.append(task)
        print(f"Task '{task}' has been added.")
    elif option == "2":
        if not task_list:
            print("No tasks inputed!")
        else:
            print("Here are your tasks:")
            for index, value in enumerate(task_list):
                print(f"{index + 1}. {value}")
    elif option == "3":
        task_id = input("Enter task ID to mark as complete:")
        task_list.pop(int(task_id) - 1)
        print(f"Task ID '{task_id}' has been removed and marked as complete.")
    elif option == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option")