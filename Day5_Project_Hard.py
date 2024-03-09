# Day 5 project from 100 Days of Code: The Complete Python Pro Bootcamp course - Hard version
import random

print("Welcome to the PyPassword Generator!")
letters_in = int(input("How many letter you like in your password?\n"))
symbols_in = int(input("How many symbols would you like?\n"))
numbers_in = int(input("How many numbers would you like?\n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

password = []

for x in range(0, letters_in):
    z = random.randint(0, len(letters) - 1)
    password.append(letters[z])

for x in range(0, symbols_in):
    z = random.randint(0, len(symbols) - 1)
    password.append(symbols[z])

for x in range(0, numbers_in):
    z = random.randint(0, len(numbers) - 1)
    password.append(numbers[z])

password = random.sample(password, len(password))

password = "".join(password)

print(f"Here is your password: {password}")
