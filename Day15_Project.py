# Day 15 project from 100 Days of Code: The Complete Python Pro Bootcamp course

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk:  {resources['milk']}ml")
    print(f"Coffe: {resources['coffee']}g")
    print(f"Money: ${profit}")


def product():
    if user_input == "espresso":
        return MENU['espresso']
    elif user_input == "latte":
        return MENU['latte']
    elif user_input == "cappuccino":
        return MENU['cappuccino']
    else:
        print("Wrong input!")


def enough():
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    return True


def money():
    print("Please insert coins.")
    total_f = int(input("how many quarters?: ")) * 0.25
    total_f += int(input("how many dimes?: ")) * 0.1
    total_f += int(input("how many nickles?: ")) * 0.05
    total_f += int(input("how many pennies?: ")) * 0.01
    return total_f


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print("Turning off")
        break
    elif user_input == "report":
        report()
    else:
        product_selected = product()
        order_ingredients = product_selected['ingredients']
        if enough() is True:
            total = money()
            if total >= product_selected['cost']:
                change = round(total - product_selected['cost'], 2)
                if change > 0:
                    print(f"Here is ${change} in change.")
                profit += round(total - change, 2)
                for item in order_ingredients:
                    resources[item] -= order_ingredients[item]
                print(f"Here is your {user_input}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
