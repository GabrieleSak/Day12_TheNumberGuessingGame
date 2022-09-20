import random

from art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
NUMBER = random.randint(1, 100)
# print(f"Pssst, answer is {NUMBER}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    ATTEMPTS_LEFT = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    ATTEMPTS_LEFT = 5
    print("You have 5 attempts remaining to guess the number.")


def number_check(user_guess):
    global ATTEMPTS_LEFT
    if user_guess == NUMBER:
        print(f"You got it! The answer was {NUMBER}")
        ATTEMPTS_LEFT = 0
    elif user_guess < NUMBER:
        print("Too low.")
        print("Guess again.")
        ATTEMPTS_LEFT -= 1
        print(f"You have {ATTEMPTS_LEFT} attempts remaining to guess the number.")
    else:
        print("Too high.")
        print("Guess again.")
        ATTEMPTS_LEFT -= 1
        print(f"You have {ATTEMPTS_LEFT} attempts remaining to guess the number.")


while ATTEMPTS_LEFT > 0:
    guess = int(input("Make a guess: "))
    number_check(guess)
