'''

Highly ethical functioning coffee machine that has choice of 3 coffee. It will take a desire coffee from user
and process if it can make the product with it's limited resources. Once it confirms that it will prompt
the customer to insert/pay through coins. Calculate the coins into money and return any extra funds.
If the customer has insufficient coins it will return the money (very ethical). Once payment is process,
it will make the coffee and update it's internal report logs to show remaining resources and total funds
it has collected. Bonus: secret codes off: will shut down machine and report: will give report.
A more complex take on a simple coffee machine project.

'''

from art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1500,
    "milk": 1250,
    "coffee": 500,
}

print(logo)

active_state = True
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
total_money = 0.0

def print_report():
    global water, milk, coffee
    for x in resources:
        if x == 'water':
            print(f"{x.title()}: {water}ml")
        if x == 'milk':
            print(f"{x.title()}: {milk}ml")
        if x == 'coffee':
            print(f"{x.title()}: {coffee}g")
    print(f"Money: ${total_money}")

def enough_supply(drink):
    global water, milk, coffee
    if drink != "espresso":
        if water < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif milk < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not coffee")
            return False

    if drink == 'espresso':
        if water < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not coffee")
            return False
    return True

def process_coin(quart, dimes, nickels, pennies):
    return .25*quart + .10*dimes + .05*nickels + .01*pennies

def check_transaction(drink, money_insert):
    global total_money
    if money_insert < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded...")
        return False
    total_money += money_insert
    if money_insert > MENU[drink]["cost"]:
        change = money_insert - MENU[drink]["cost"]
        total_money -= change
        print(f"Here is ${change} dollars in change.")
        return True
    return True

def make_coffee(drink):
    global milk, water, coffee
    if drink != 'espresso':
        waterD = MENU[drink]['ingredients']['water']
        milkD = MENU[drink]['ingredients']['milk']
        coffeeD = MENU[drink]['ingredients']['coffee']
        water -= waterD
        milk -= milkD
        coffee -= coffeeD
    if drink == 'espresso':
        waterD = MENU[drink]['ingredients']['water']
        coffeeD =  MENU[drink]['ingredients']['coffee']
        water -= waterD
        coffee -= coffeeD


def coffee_machine():
    action = input("What would you like customer? (espresso/latte/cappuccino)\n")
    if action == 'off':
        print("You found the secret code! The machine is shutting down now")
        global active_state
        active_state = False
        return None
    elif action == 'report':
        print_report()
        coffee_machine()
    elif action != 'espresso' and action != 'latte' and action != 'cappuccino':
        print("Not a valid command sir/madame. Please enter a valid command.")
        coffee_machine()
    else:
        ready = enough_supply(action)
        if ready:
            all_coins = input("Please enter the amount of money in format (quarter dime nickels pennies):")
            if all_coins == 'off':
                print("You found the secret code! The machine is shutting down now")
                active_state = False
                return None
            while all_coins == 'report':
                print_report()
                all_coins = input("Please enter the amount of money in format (quarter dime nickels pennies):")
            try:
                lstCoin = all_coins.split()
                quart = lstCoin[0]
                dime = lstCoin[1]
                nick = lstCoin[2]
                penn = lstCoin[3]
                moneyIn = process_coin(int(quart),int(dime),int(nick),int(penn))
                approve = check_transaction(action, moneyIn)
                if approve:
                    make_coffee(action)
                    print(f"Here is your {action}. Enjoy!")
            except IndexError:
                print("ERROR: Invalid input please try again.")
                print("Machine starting from beginning again")
                coffee_machine()

while active_state:
    coffee_machine()
