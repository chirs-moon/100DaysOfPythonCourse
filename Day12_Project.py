# Day 12 project from 100 Days of Code: The Complete Python Pro Bootcamp course

import random as ra

logo = '''
  / _ \\_   _  ___  ___ ___  /__   \\ |__   ___    /\\ \\ \\_   _ _ __ ___ | |__   ___ _ __ 
 / /_\\/ | | |/ _ \\/ __/ __|   / /\\/ '_ \\ / _ \\  /  \\/ / | | | '_ ' _ \\| '_ \\ / _ \\ '__|
/ /_\\| |_| |  __/\\__ \\__ \\  / /  | | | |  __/ / /\\  /| |_| | | | | | | |_) |  __/ |   
\\____/ \\__,_|\\___||___/___/  \\/   |_| |_|\\___| \\_\\ \\/  \\__,_|_| |_| |_|_.__/ \\___|_|   
'''

# Functions


def guess_fun():
    global ANSWER
    global LIVES
    guess = int(input("Make a gues: "))
    if guess < ANSWER:
        print("Too low.")
        print(f"You have {LIVES} attempts remaining to guess the number.")
        LIVES -= 1
    elif guess > ANSWER:
        print("Too high.")
        LIVES -= 1
        print(f"You have {LIVES} attempts remaining to guess the number.")
    else:
        print(f"You got it! The answer was {ANSWER}.")
        return True


# Start of the game
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

ANSWER = ra.randint(1, 100)

print(f"Pssst, the correct answer is {ANSWER}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    LIVES = 10
elif difficulty == "hard":
    LIVES = 5
else:
    print("Wrong input!")
    print("Easy difficulty automatically selected.")
    LIVES = 10

print(f"You have {LIVES} attempts")
x = False

while LIVES > 0 and x is not True:
    x = guess_fun()
