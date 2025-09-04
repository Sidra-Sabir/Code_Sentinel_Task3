import json
import os

file_name = "tasks.json"

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            return json.load(f)
    return []
    
def save_tasks(tasks):
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
            print("tasks.json file saved successfully!")

tasks = load_tasks()

while True:
    print("...To-Do List...")
    print("1. View your Task")
    print("2. Add your Task")
    print("3. Remove your Task")
    print("4. Exit")

    choice = input("Enter your choice here: ")

    if choice == "1":
         if not tasks:
            print("No task occur")
         else:
            print("your tasks: ")
            for i, t in enumerate(tasks, 1):
                print(f"{i}.{t}")

    elif choice == "2":
        task = input("Enter your new task here: ")
        tasks.append(task)   #append function used to add element in the last of list 
        save_tasks(tasks)
        print("Task added")
       
    elif choice == "3":
        if not tasks:
            print("No task occur")
        else:
            for i, t in enumerate(tasks, 1): #enumerate() function shows index and value both
                print(f"{i}.{t}")
            number = int(input("Enter task number to remove: "))
            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"Task Remove , {removed}")
            else:
                     print("You entered a invalid task number")   
    elif choice == "4":
        print("Exit")
        break
    else:
         print("invalid data")