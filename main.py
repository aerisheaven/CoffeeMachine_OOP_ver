from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_menu = Menu()
coffee_resources = CoffeeMaker()
coffee_money = MoneyMachine()


def take_order():
    order = input(f"What would you like? ({Menu.get_items(coffee_menu)}): ")
    if order == "off":
        return 0
    elif order == "report":
        coffee_resources.report()
        coffee_money.report()
        take_order()
    else:
        drink = Menu.find_drink(coffee_menu, order)
        if drink is None:
            take_order()
        elif CoffeeMaker.is_resource_sufficient(coffee_resources, drink):
            if MoneyMachine.make_payment(coffee_money, drink.cost):
                CoffeeMaker.make_coffee(coffee_resources, drink)
                take_order()
            else:
                take_order()


take_order()
