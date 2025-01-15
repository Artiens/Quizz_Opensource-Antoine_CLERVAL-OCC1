def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    while True:
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer < 1 or user_answer > len(options):
                print("Invalid input. Please select a valid option.")
                continue
            # Check if the selected answer number corresponds to the correct answer
            if options[user_answer - 1] == correct_answer:
                return True
            else:
                return False
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except IndexError:
            print("Invalid option. Please enter a valid number between 1 and 4.")

def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Rome", "Berlin"],
            "correct_answer": "Paris"
        },
        {
            "question": "Which programming language is this quiz written in?",
            "options": ["Python", "Java", "C++", "Ruby"],
            "correct_answer": "Python"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_answer": "4"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"],
            "correct_answer": "Shakespeare"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!")
    print("Answer the following questions to win.")
    print()

    for q in questions:
        if ask_question(q['question'], q['options'], q['correct_answer']):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['correct_answer']}\n")
    
    print(f"Your final score is: {score} out of {len(questions)}")
    
    if score == len(questions):
        print("Congratulations, you won the game!")
    else:
        print("Better luck next time!")


# Run the game
quiz_game()
