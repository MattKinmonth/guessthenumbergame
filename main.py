# function to set difficulty
# functionality for user to guess number
# function to check user's guess against answer

import random
from art import logo

print(logo)

USER_TURNS_EASY = 10
USER_TURNS_HARD = 5
turns = 0


def difficulty():
    level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
    if level == "easy":
        return USER_TURNS_EASY
    else:
        return USER_TURNS_HARD


def check_answer(user_guess, answer, turns):
    """Checks answer against guess. Returns number of guesses remaining,"""
    if user_guess == answer:
        print(f"The answer was {answer}! Could you BE any smarter?")
    elif user_guess > answer:
        print("Too high.")
        return turns - 1
    elif user_guess < answer:
        print("Too low.")
        return turns - 1


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    end_of_game = False
    answer = random.randint(1, 100)
    # print(answer)
    turns = difficulty()
    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("\nGuess a number: "))
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses. The answer was {answer}. You lose!")
            return

game()






