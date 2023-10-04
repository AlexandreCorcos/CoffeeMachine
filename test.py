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
    "money": 0.0
}


# money = float(0)
not_off = True


def report(water, milk, coffee, money):
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: £{money}")


def main_coffee(water=0, milk=0, coffee=0, money=0):
    a_res_water = resources["water"] - water
    a_res_milk = resources["milk"] - milk
    a_res_coffee = resources["coffee"] - coffee
    a_res_money = resources["money"] + money

    if a_res_water < 0:
        print("Sorry there is not enough water.")
    elif a_res_milk < 0:
        print("Sorry there is not enough Milk.")
    elif a_res_coffee < 0:
        print("Sorry there is not enough Coffee.")

    resources["water"] = a_res_water
    resources["milk"] = a_res_milk
    resources["coffee"] = a_res_coffee
    resources["money"] = a_res_money

    report(resources["water"], resources["milk"], resources["coffee"], resources["money"])


while not_off:
    prompt = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if prompt == "off":
        not_off = False
    elif prompt == "report":
        report(resources["water"], resources["milk"], resources["coffee"], resources["money"])
    elif prompt == "espresso":
        main_coffee(water=MENU["espresso"]["ingredients"]["water"],
                    coffee=MENU["espresso"]["ingredients"]["coffee"],
                    money=MENU["espresso"]["cost"])
    elif prompt == "latte":
        main_coffee(water=MENU["latte"]["ingredients"]["water"],
                    milk=MENU["latte"]["ingredients"]["milk"],
                    coffee=MENU["latte"]["ingredients"]["coffee"],
                    money=float(MENU["latte"]["cost"]))
    elif prompt == "cappuccino":
        main_coffee(water=MENU["cappuccino"]["ingredients"]["water"],
                    milk=MENU["cappuccino"]["ingredients"]["milk"],
                    coffee=MENU["cappuccino"]["ingredients"]["coffee"],
                    money=float(MENU["cappuccino"]["cost"]))
