#46. 🎲 Number Guessing Game

import random

secret_number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))

if guess < secret_number:
    print(f"❌ Your guess {guess} is too low.")
elif guess > secret_number:
    print(f"❌ Your guess {guess} is too high.")
else:
    print(f"🎉 Correct! The secret number was {secret_number}.")
