from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    print(f"Current resources: ")
    coffee_maker.report()
    order_name = input(f"Welcome! Select your drink ({menu.get_items()}): ")
    order = menu.find_drink(order_name)
    money_machine.report()
    if coffee_maker.is_resource_sufficient(order):
        payment = money_machine.make_payment(float(order.cost))
        if payment:
            coffee_maker.make_coffee(order)
            repeat = input("Do you want another drink? (y/n) ")
            if repeat != "y":
                is_on = False
            else:
                continue