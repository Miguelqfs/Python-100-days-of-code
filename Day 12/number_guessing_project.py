import random
from art import logo

print(logo)
number = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    vidas = 10
else:
    vidas = 5

while vidas:
    print(f"You have {vidas} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    vidas -= 1
    if vidas == 0:
        print("You've run out of guesses. Refresh the page to run again.")
        break
    if guess > number:
        print("Too High.\nGuess again.")
    if guess < number:
        print("Too low.\nGuess again.")