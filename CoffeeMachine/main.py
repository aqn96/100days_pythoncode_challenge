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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print(logo)

active_state = True

def print_report():
    print(resources)

def enough_supply(drink):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    if drink != "espresso":
        if water < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif milk < MENU[drink]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not coffee")

    if drink == "espresso":
        if water < MENU[drink]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif coffee < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry there is not coffee")

def process_coin():


def check_transaction():



    coffee = input("What would you like customer? (espresso/latte/cappuccino)\n")