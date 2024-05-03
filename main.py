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
    "money" : 0
}
'''
print(resources["water"])
pry = MENU["espresso"]["ingredients"]["water"]
print(pry)

'''

nickles = 0.05
quarters = 0.25
dimes = 0.1
pennies = 0.01


should_continue = True
user_choice = input("What would you like to order ? Espresso-latte-cappuccino:").lower()
def check_sufficiency():
    if  user_choice == "espresso":
        if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            process_coins()
    elif user_choice == "latte" or "cappuccino":
        if resources["water"] < MENU[user_choice]["ingredients"]["water"]:
            print("Sorry there is not enough water.")
        elif resources["milk"] < MENU[user_choice]["ingredients"]["milk"]:
            print("Sorry there is not enough milk.")
        elif resources["coffee"] < MENU[user_choice]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            process_coins()

    elif user_choice == "report":
        print(resources)
    else:
        return user_choice


def process_coins():
    quarters_piece= int(input("How many quarters ?"))
    quarters_dimes = int(input("How many dimes?"))
    quarters_nickles = int(input("How many nickles ?"))
    quarters_pennies = int(input("How many pennies ?"))
    total_sum = quarters_piece * quarters + quarters_dimes * quarters + quarters_nickles * nickles + quarters_pennies * pennies

    if total_sum > MENU [user_choice]["cost"]:
        if user_choice == "espresso":
            print(f"Water: {resources["water"] - MENU[user_choice]["ingredients"]["water"]} ml")
            print(f"Coffee: {resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]}g")
            print(f"Money: {MENU[user_choice]["cost"]}$")
            print(f"Here is {total_sum - MENU[user_choice]["cost"]} $ dollars in change.Here is your {user_choice}. Enjoy!")
        elif user_choice == "latte" or "cappuccino":
            print(f"Milk: {resources["milk"] - MENU[user_choice]["ingredients"]["milk"]}ml ")
            print(f"Milk: {resources["milk"] - MENU[user_choice]["ingredients"]["milk"]}ml ")
            print(f"Coffee: {resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]}g")
            print(f"Money: {MENU [user_choice]["cost"]}$")
            print(f"Here is {total_sum- MENU [user_choice]["cost"]} $ dollars in change.Here is your {user_choice}. Enjoy!")

    elif total_sum < MENU [user_choice]["cost"]:
        print("Sorry that's not enough money. Money refunded.")

while should_continue == True:
    check_sufficiency()
else:
    should_continue = False







