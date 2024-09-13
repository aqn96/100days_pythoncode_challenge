from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


is_on = True

while is_on:
    options = menu.get_items()
    action = input(f"What would you like dear customer? {options}:\n")
   
    if action == "off":
        print("You have found the secret code word! Turning off now.")
        is_on = False
    elif action == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(action)
        ans = coffee_maker.is_resource_sufficient(drink)
        if ans:
            success = money_machine.make_payment(drink.cost)
            if success:
                coffee_maker.make_coffee(drink)




