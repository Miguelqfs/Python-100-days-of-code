import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
else:
    print(scissors)

bot = random.randint(0,2)

if bot == 0:
    print(f"Computer chose:\n{rock}")
elif bot == 1:
    print(f"Computer chose:\n{paper}")
else:
    print(f"Computer chose:\n{scissors}")