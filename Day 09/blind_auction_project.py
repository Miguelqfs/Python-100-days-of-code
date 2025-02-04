# Ask the user for input
# Save data into dictionary {name: price}
# Whether if new bids need to be added
# Compare bids in dictionary
from ctypes import windll

import art

print(art.logo)

bids = {}
highest_bid = -1
winner = ""

while True:
    name = input("Type your name: ")
    price = int(input("Type your bid: $"))

    bids[name] = price

    again = input("Are there any other user who wants to bid? 'yes or 'no'. ")

    if again == 'yes':
        print("\n" * 20)
    else:
        for key in bids:
            if bids[key] > highest_bid:
                winner = key
        print(f"\nThe winner was {winner} with a bid of ${bids[winner]}")
        break