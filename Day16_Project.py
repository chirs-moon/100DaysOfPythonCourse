from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


while True:
    user_input = input(f"What would you like? ({menu.get_items()}): ")
    if user_input == "off":
        print("Turning off")
        break
    elif user_input == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        type = menu.find_drink(user_input)
        if coffeemaker.is_resource_sufficient(type):
            if moneymachine.make_payment(type.cost):
                coffeemaker.make_coffee(type)
