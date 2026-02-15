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

def make_coffee(menu_dict, res_dict, option):


        if option == "report":
            for key, value in res_dict.items():
                print(f"{key}: {value}")
            return res_dict

        new_resourses = {}

        if option == "espresso":
            new_resourses["water"] = res_dict["water"] - menu_dict[option]["ingredients"]["water"]
            new_resourses["coffee"] = res_dict["coffee"] - menu_dict[option]["ingredients"]["coffee"]
        else:
            new_resourses["water"] = res_dict["water"] - menu_dict[option]["ingredients"]["water"]
            new_resourses["milk"] = res_dict["milk"] - menu_dict[option]["ingredients"]["milk"]
            new_resourses["coffee"] = res_dict["coffee"] - menu_dict[option]["ingredients"]["coffee"]

        cost = menu_dict[option]["cost"]

        return  new_resourses,cost

def check_resources(menu_dict, res_dict, option):
    ingredients = menu_dict[option]["ingredients"]
    for item, amount in ingredients.items():
        if res_dict.get(item, 0) < amount:
            print(f"There not enough resources for {item}.")
            return False
    return True


def check_payment(quarters, dimes, nickels, pennies, drink_cost):

    total_paid = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

    if total_paid >= drink_cost:
        change = total_paid - drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print(f"Sorry, that's not enough money. Money refunded.")
        return False

game_over = False
while not game_over:

        what_coffee = input("What kind of coffee would you like?(espresso,latte,cappuccino").lower()
        if what_coffee == "report":
            make_coffee(MENU, resources, what_coffee)
        else:
            if not check_resources(MENU, resources, what_coffee):
                continue
            print("Please insert coins")
            quarter = int(input("How many quarters:"))
            dimes = int(input("How many dimes:"))
            nickles = int(input("How many nickles:"))
            pennies = int(input("How many pennies:"))

            _, drink_cost = make_coffee(MENU, resources, what_coffee)

            if check_payment(quarter, dimes, nickles, pennies, drink_cost):
                resources,_ = make_coffee(MENU, resources, what_coffee)
                print(f"Here is your {what_coffee} Enjoy!")
        one_more = input("Do you want one more coffee? 'Y' or 'N'").lower()
        if one_more != "y":
            game_over = True



