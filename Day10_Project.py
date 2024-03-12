# Day 10 project from 100 Days of Code: The Complete Python Pro Bootcamp course

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \\     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \\_|  | || |    / /\\ \\    | || |    | |       | || |  / .'   \\_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \\   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \\ `.___.'\\  | || | _/ /    \\ \\_ | || |   _| |__/ |  | || |  \\ `.___.'\\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


def pow(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "**": pow
}
print(logo)
n1_input = float(input("What's the first number: "))
for op in operations:
    print(op)
op_input = input("Pick an operation: ")
n2_input = float(input("What's the second number: "))

result = operations[op_input]
answer = result(n1_input, n2_input)

print(f"{n1_input}{op_input}{n2_input}={answer}")

again = input("Do you want to perform another operation? Type 'yes' or 'no'. ").lower()
while again != "no":
    n3_input = float(input("What's the next number: "))
    op_input = input("Pick an operation: ")
    result = operations[op_input]
    prev = answer
    answer = result(answer, n3_input)
    print(f"{prev}{op_input}{n3_input}={answer}")
    again = input("Do you want to perform another operation? Type 'yes' or 'no'. ").lower()
