from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
item = MenuItem
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
machine_running = True

while machine_running:
    options = drink_menu.get_items()
    chosen_drink = input(f"What would you like? ({options}): ").lower()
    if chosen_drink == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif chosen_drink == "off":
        machine_running = False
    elif drink_menu.find_drink(chosen_drink) is None:
        continue
    else:
        menu_drink = drink_menu.find_drink(chosen_drink)
        enough_ingredients = my_coffee_machine.is_resource_sufficient(menu_drink)
        if enough_ingredients:
            cost = menu_drink.cost
            print(f"Please enter ${cost}.")
            if my_money_machine.make_payment(cost):
                my_coffee_machine.make_coffee(menu_drink)
            else:
                continue
        else:
            continue
