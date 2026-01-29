from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu = Menu()
my_coffee = CoffeeMaker()
is_on = True

while is_on:
    choice = input(f"Which drink would you like? ({menu.get_items()}) ").lower()
    if choice == "report":
        my_coffee.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(choice)
        if my_coffee.is_resource_sufficient(drink) == True:
            if money_machine.make_payment(drink.cost):
                my_coffee.make_coffee(drink)
        else:
            break
