tasks = [] 

def addTask():
    task = input("Enter task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def viewTask():
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

def deleteTask():
    viewTask()
    if len(tasks) > 0:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print("Removed task:", removed)
        except:
            print("Invalid number, try again.")
if __name__ == "__main__":
### create a loop to run the file

    print("WELCOME TO THE TO-DO LIST MENU")    
    while True:
        print("\n")
        print("Please Select one of the following options")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done (Delete)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            addTask()
            
        elif choice == '2':
            viewTask()
            
        elif choice == '3':
            deleteTask()
            
        elif choice == '4':
            break

        else:
            print("Invalid choice! Please enter 1-4.")

    print("Exiting To-Do List... Goodbye!")
