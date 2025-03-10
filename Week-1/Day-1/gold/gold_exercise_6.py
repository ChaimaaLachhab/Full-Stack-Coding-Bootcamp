import random

# Exercise 6: Random Number Guessing Game
wins = 0
losses = 0

while True:
    user_guess = input("\nGuess a number between 1 and 9 (or type 'quit' to exit): ")
    if user_guess.lower() == "quit":
        print(f"Games won: {wins}, Games lost: {losses}")
        break

    user_guess = int(user_guess)
    random_number = random.randint(1, 9)

    if user_guess == random_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time! The number was {random_number}.")
        losses += 1
