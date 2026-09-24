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