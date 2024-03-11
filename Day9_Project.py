# Day 9 project from 100 Days of Code: The Complete Python Pro Bootcamp course

import replit

logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

rep = ""

users = {}

while rep != "no":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    users[name] = bid
    rep = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    replit.clear()

if rep == "no":
    winner_name = ""
    winner_amount = 0

    for key, value in users.items():
        bid_amount = value
        if winner_amount < bid_amount:
            winner_name = key
            winner_amount = value

    print(f"The winner is {winner_name} with a bid of ${winner_amount}.")
