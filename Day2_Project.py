# Day 2 project from 100 Days of Code: The Complete Python Pro Bootcamp course

# This is a program greeting
print("Welcome to the bill-splitting calculator.")

# Here the program asks the user for three inputs and defines the data types of inputs
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15"))
people = int(input("How many people to split the bill?"))

# Here the program calculates the amount each person should pay
total = bill + (bill * (tip / 100))
per_person = round(total / people, 2)

# Here we are changing the float to a string displaying two decimal places
per_person = "{:.2f}".format(per_person)

print(f"Each person should pay: ${per_person}")
