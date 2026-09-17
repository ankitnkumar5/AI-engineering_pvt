#---------------------------------------Simple Calculator-------------------------------------------------------------------

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def calculator():
    print("Select Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ").strip()

        if choice.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    calculator()
    
    
    
    
#---------------------------------------CLI Todo List App-------------------------------------------------------------------
    
import json
import os

FILENAME = "todos.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("\nYour todo list is empty!")
        return

    print("\n--- YOUR TODO LIST ---")
    for idx, task in enumerate(tasks, start=1):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{idx}. {status} {task['title']}")


def add_task(tasks):
    title = input("Enter task description: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")


def mark_completed(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter number of task to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    show_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter number of task to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Pick a number from 1 to 5.")


if __name__ == "__main__":
    main()
    


#-----------------------------Number gussing game---------------------------------------------
import random

target = random.randint(1, 100)
attempts = 5

print("Guess the number between 1 and 100!")
while attempts > 0:
    guess = int(input(f"({attempts} attempts left) Enter guess: "))
    if guess == target:
        print("You won!")
        break
    elif guess < target:
        print("Too low.")
    else:
        print("Too high.")
    attempts -= 1