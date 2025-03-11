# 🌟 Exercise 8 : Star Wars Quiz

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def take_quiz():
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for item in data:
        question = item["question"]
        correct_answer = item["answer"]
        user_answer = input(question + " ")

        if user_answer.strip().lower() == correct_answer.lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({
                "question": question,
                "user_answer": user_answer,
                "correct_answer": correct_answer
            })
    
    return correct_answers, incorrect_answers, wrong_answers

def display_results(correct, incorrect, wrong_answers):
    print(f"\nYou answered {correct} questions correctly and {incorrect} incorrectly.")
    
    if incorrect > 3:
        print("\nYou had more than 3 wrong answers, would you like to try again?")
    else:
        if incorrect > 0:
            print("\nHere are the questions you answered wrong:")
            for item in wrong_answers:
                print(f"Question: {item['question']}")
                print(f"Your answer: {item['user_answer']}")
                print(f"Correct answer: {item['correct_answer']}")
        else:
            print("\nGreat job! You answered all questions correctly.")

def main():
    correct, incorrect, wrong_answers = take_quiz()
    display_results(correct, incorrect, wrong_answers)
    
    if incorrect > 3:
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again == "yes":
            main()
        else:
            print("\nThanks for playing! May the Force be with you!")

main()
