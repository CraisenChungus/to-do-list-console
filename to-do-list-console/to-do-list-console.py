print("Welcome to To-Do!")
listoftasks = []

def show_tasks():
    if listoftasks:
        print("Your tasks:")
        for i, task in enumerate(listoftasks, start=1):
            print(f"{i}. {task}")
    else:
        print("List of tasks is empty.")

while True:
    try:
        command = input("Enter command (add/show/delete/deleteall/exit): ").lower()

        match command:
            case "add":
                task = input("Describe the task: ")
                listoftasks.append(task)
                show_tasks()

            case "show":
                show_tasks()

            case "delete":
                if not listoftasks:
                    print("List of tasks is empty.")
                    continue
                index = int(input("No. of task: "))
                if 1 <= index <= len(listoftasks):
                    listoftasks.pop(index - 1)
                else:
                    print("Wrong No. of task.")
                show_tasks()

            case "deleteall":
                listoftasks.clear()
                print("All task were deleted.")

            case "exit":
                print("Thanks for you visit!")
                break

            case _:
                print("Wrong command.")

    except ValueError:
        print("Please, enter valid data.")