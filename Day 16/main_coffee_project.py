from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like: ({options})")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)












# menu.name = "latte"
# print(menu.name)
#
# menu.cost = 1.5
# print(menu.cost)
#
# menu.ingredients = {"water": 100, "coffee": 16}
# print(f"{menu.ingredients["water"]}ml")

# money_machine.make_payment(1)