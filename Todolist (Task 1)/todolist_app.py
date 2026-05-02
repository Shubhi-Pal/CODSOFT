my_list = []

def display_items():
    if len(my_list) == 0:
        print("Nothing to show!")
    else:
        print("\nYour Tasks:")
        count = 1
        for item in my_list:
            print(str(count) + " -> " + item)
            count += 1

def insert_item():
    new_item = input("Write your task: ")
    if new_item != "":
        my_list.append(new_item)
        print("Added successfully!")
    else:
        print("Empty task not allowed!")

def remove_item():
    display_items()
    try:
        index = int(input("Which task number you want to remove? "))
        deleted_item = my_list.pop(index - 1)
        print("Removed:", deleted_item)
    except:
        print("Something went wrong!")

def edit_item():
    display_items()
    try:
        index = int(input("Enter task number to update: "))
        updated_text = input("Enter new text: ")
        my_list[index - 1] = updated_text
        print("Task updated!")
    except:
        print("Invalid input!")

def start_app():
    while True:
        print("\n--- TO-DO MENU ---")
        print("1. Show all tasks")
        print("2. Add new task")
        print("3. Delete task")
        print("4. Update task")
        print("5. Exit")

        option = input("Select option: ")

        if option == "1":
            display_items()
        elif option == "2":
            insert_item()
        elif option == "3":
            remove_item()
        elif option == "4":
            edit_item()
        elif option == "5":
            print("Closing app...")
            break
        else:
            print("Wrong choice!")

start_app()