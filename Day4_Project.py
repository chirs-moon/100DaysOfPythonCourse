import random

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
player_input = int(input())

computer = random.randint(0, 2)
print(computer)

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

symbol = [rock, paper, scissors]

print(symbol[player_input])
print(symbol[computer])

if player_input == computer:
    print("Draw!")
elif player_input == 1 and computer == 0:
    print("You Win!")
elif player_input == 2 and computer == 1:
    print("You Win!")
else:
    print("You Lose!")
