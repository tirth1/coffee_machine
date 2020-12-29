import os
from data import MENU, resources


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f'Water: {water}')
    print(f'Milk: {milk}')
    print(f'Coffee: {coffee}')


def order_espresso():
    resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
    print("Here is your espresso...Enjoy!")


def order_latte():
    resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
    print("Here is your latte...Enjoy!")


def order_cappuccino():
    resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["milk"]
    print("Here is your cappuccino...Enjoy!")


def check_resources(coffee_type):
    if resources["water"] >= MENU[coffee_type]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_type]["ingredients"]["coffee"]:
        if coffee_type == "espresso":
            return True

        if resources["milk"] >= MENU[coffee_type]["ingredients"]["milk"]:
            return True
        else:
            print("Sorry there is not enough resources available.")
            return False
    print("Sorry there is not enough resources available.")
    return False


def inset_coins(coffee_type):
    print("\nPlease insert coins.\n")
    quarters = float(input("How many quarters?:  "))
    dimes = float(input("How many dimes?:  "))
    nickles = float(input("How many nickles?:  "))
    pennies = float(input("How many pennies?:  "))

    total = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    if total > MENU[coffee_type]["cost"]:
        change = round(total - MENU[coffee_type]["cost"], 2)
        print(f"\nHere is ${change} in change.\n")
    elif total < MENU[coffee_type]["cost"]:
        print("\nSorry there is not enough money. Money refunded.")
        return False

    return True
