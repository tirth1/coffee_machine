from time import sleep
from coffeemachine import screen_clear, report, order_espresso, order_latte, order_cappuccino, check_resources, inset_coins


if __name__ == '__main__':
    nextOrder = True
    while nextOrder:
        sleep(1)
        screen_clear()
        order = input("What would you like? espresso/latte/cappuccino:  ")
        if order == "off":
            nextOrder = False
        elif order == "report":
            report()

        elif order == "espresso":
            if check_resources("espresso"):
                if inset_coins("espresso"):
                    order_espresso()

        elif order == "latte":
            if check_resources("latte"):
                if inset_coins("latte"):
                    order_latte()

        elif order == "cappuccino":
            if check_resources("cappuccino"):
                if inset_coins("cappuccino"):
                    order_cappuccino()
                    order_cappuccino()
