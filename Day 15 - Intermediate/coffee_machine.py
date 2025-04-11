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
    "money": 0.0,
}

def check_resources(coffee_type):
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        return 0
    if MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        return 1
    if coffee_type != "espresso":
        if MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
            return 2
    return 3

def calculate_money(qua, di, ni, pen):
    total = (pen * 0.01) + (ni * 0.05) + (di * 0.1) + (qua * 0.25)
    return total

def subtract_ingredients(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]

while True:
    entrada = input("How would you like? (espresso/latte/cappuccino): ").lower()

    if entrada == "off":
        break

    if entrada == "report":
        print(f"Water: {resources["water"]}ml\n"
              f"Milk: {resources["milk"]}ml\n"
              f"Coffee: {resources["coffee"]}g\n"
              f"Money: ${resources["money"]}")
        continue

    match check_resources(entrada):
        case 0:
            print("Sorry, there's not enough water.")
            continue
        case 1:
            print("Sorry, there's not enough coffee.")
            continue
        case 2:
            print("Sorry, there's not enough milk.")
            continue
        case 3:
            print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    money = calculate_money(quarters, dimes, nickles, pennies)
    price = MENU[entrada]["cost"]

    if money < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        resources["money"] += price
        subtract_ingredients(entrada)
        change = money - price

        print(f"Here is ${change} in change.")
        print(f"Here is your {entrada} ☕ Enjoy!")