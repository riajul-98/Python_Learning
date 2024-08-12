MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

machine_on = True


# coins: penny (1 cent), nickel (5 cents), dime (10 cents), quarter (25 cents)

def make_drink(drink):
    drink_ingredients = MENU[drink]['ingredients']
    for item in drink_ingredients:
        quantity = drink_ingredients[item]
        resource[item] -= quantity


while machine_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 1: print report of how much resources are left and how much money in the machine
    if user_choice == 'off':
        print("Coffee machine shutting down...")
        print("Have a good day!")
        machine_on = False
        break
    if user_choice == "report":
        print(f"Water: {resource['water']}ml\nMilk: {resource['milk']}ml\nCoffee: {resource['coffee']}g\nMoney: "
              f"${resource['money']}")

    # TODO 2: Check if resources are sufficient

    # TODO 3: Make drink

    if user_choice in MENU:
        can_make_drink = True
        for ingredient in MENU[user_choice]['ingredients']:
            amount_needed = MENU[user_choice]['ingredients'][ingredient]
            if amount_needed > resource[ingredient]:
                print(f"Sorry, not enough {ingredient}")
                can_make_drink = False
                break

        if can_make_drink:
            print(f"Please enter ${MENU[user_choice]['cost']}")
            quarters = int(input("How many quarters do you wish to enter? "))
            dimes = int(input("How many dimes do you wish to enter? "))
            nickels = int(input("How many nickels do you wish to enter? "))
            pennies = int(input("How many pennies do you wish to enter? "))

            total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
            if total < MENU[user_choice]['cost']:
                print("Insufficient funds.")
            elif total == MENU[user_choice]['cost']:
                make_drink(user_choice)
                print(f"Here is your {user_choice}.")
                resource['money'] += MENU[user_choice]['cost']
            else:
                make_drink(user_choice)
                change = round(total - MENU[user_choice]['cost'], 2)
                print(f"Here is your {user_choice} and ${change} change.")
                resource['money'] += MENU[user_choice]['cost']

        # TODO 4: Check if transaction is successful

        # TODO 5: Make coffee
