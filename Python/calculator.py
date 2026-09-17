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
    
    
    
    #----------------------------Flashcard Quiz App---------------------------------
    import json
import random
import os

FILENAME = "flashcards.json"

def load_flashcards():
    """Loads flashcards from a JSON file if it exists."""
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Could not parse flashcards file. Starting fresh.")
            return {}
    # Default set of flashcards if no file exists yet
    return {
        "What is the keyword to define a function in Python?": "def",
        "Which data structure uses key-value pairs?": "dictionary",
        "What module is used to work with JSON in Python?": "json",
        "What is the output of 3 ** 2 in Python?": "9"
    }

def save_flashcards(cards):
    """Saves the current flashcards dictionary to a JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(cards, file, indent=4)

def add_flashcard(cards):
    """Allows the user to add a new question and answer."""
    question = input("\nEnter the question: ").strip()
    if not question:
        print("Question cannot be empty.")
        return
    answer = input("Enter the answer: ").strip().lower()
    
    cards[question] = answer
    save_flashcards(cards)
    print("Flashcard added and saved successfully!")

def view_flashcards(cards):
    """Displays all current questions and answers."""
    if not cards:
        print("\nNo flashcards available.")
        return
    print("\n--- CURRENT FLASHCARDS ---")
    for idx, (question, answer) in enumerate(cards.items(), 1):
        print(f"{idx}. Q: {question} | A: {answer}")

def start_quiz(cards):
    """Runs a randomized quiz session with scoring."""
    if not cards:
        print("\nNo flashcards to quiz on! Add some first.")
        return

    questions = list(cards.keys())
    random.shuffle(questions)
    
    score = 0
    total = len(questions)

    print(f"\n--- QUIZ START ({total} Questions) ---")
    print("Type your answer and press Enter. (Answers are case-insensitive)\n")

    for idx, question in enumerate(questions, 1):
        user_answer = input(f"Q{idx}: {question}\nYour Answer: ").strip().lower()
        correct_answer = cards[question].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {cards[question]}\n")

    percentage = (score / total) * 100
    print(f"--- QUIZ COMPLETE ---")
    print(f"Your Score: {score}/{total} ({percentage:.1f}%)\n")

def main():
    cards = load_flashcards()
    
    while True:
        print("=== FLASHCARD QUIZ APP ===")
        print("1. Start Quiz")
        print("2. Add New Flashcard")
        print("3. View All Flashcards")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            start_quiz(cards)
        elif choice == '2':
            add_flashcard(cards)
        elif choice == '3':
            view_flashcards(cards)
        elif choice == '4':
            print("Thanks for studying! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()