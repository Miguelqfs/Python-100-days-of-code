from art import logo
import random

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def final_score():
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

computer_cards = []
player_cards = []

while play == 'y':
    print(logo)

    for _ in range(2):
        computer_cards.append(deal_card())
        player_cards.append(deal_card())


    computer_score = sum(computer_cards)
    player_score = sum(player_cards)

    print(f"\tYour cards: {player_cards}, current score: {player_score}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    if computer_score == 21:
        print("BlackJack! The dealer has scored 21")
    elif player_score == 21:
        print("BlackJack! You scored 21")

    while input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        player_cards.append(deal_card())
        player_score = sum(player_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_cards[0]}")



    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    print("\n" * 20)