import random

from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def number_check(user_guess, number, attempts_left):
    if attempts_left == 1:
        print("You've run out of guesses, you lose.")
        return attempts_left - 1
    elif user_guess == number:
        print(f"You got it! The answer was {number}")
        attempts_left = 0
        return attempts_left
    elif user_guess < number:
        print("Too low.")
        print("Guess again.")
        print(f"You have {attempts_left - 1} attempts remaining to guess the number.")
        return attempts_left - 1
    else:
        print("Too high.")
        print("Guess again.")
        print(f"You have {attempts_left - 1} attempts remaining to guess the number.")
        return attempts_left - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        print(f"You have {EASY_LEVEL_TURNS} attempts remaining to guess the number.")
        return EASY_LEVEL_TURNS
    else:
        print(f"You have {HARD_LEVEL_TURNS} attempts remaining to guess the number.")
        return HARD_LEVEL_TURNS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)
    print(f"Pssst, answer is {number}")

    attempts_left = set_difficulty()

    while attempts_left > 0:
        guess = int(input("Make a guess: "))
        attempts_left = number_check(guess, number, attempts_left)

game()
