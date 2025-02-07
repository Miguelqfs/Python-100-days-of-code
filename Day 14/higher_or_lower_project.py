import random
import art
from game_data import data

game_over = 0
score = 0
person_b = random.choice(data)

while not game_over:
    print("\n" * 20)
    print(art.logo)

    if score >= 1:
        print(f"You're right! Current score: {score}.")

    person_a = person_b
    person_b = random.choice(data)

    while person_a == person_b:
        person_b = random.choice(data)

    print(f"Compare A: {person_a['name']}, a {person_a['description']}, from {person_a['country']}.")
    print(art.vs)
    print(f"Against B: {person_b['name']}, a {person_b['description']}, from {person_b['country']}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == "a":
        if person_a['follower_count'] > person_b['follower_count']:
            score += 1
            person_b = person_a
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = 1
    elif guess == "b":
        if person_b['follower_count'] > person_a['follower_count']:
            score += 1
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = 1