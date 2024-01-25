from machine_data import MENU, resources


def get_order():
    user_order = int(input(f"1. Espresso {MENU['espresso']['cost']}"
                           f"\n2. Latte {MENU['latte']['cost']}"
                           f"\n3. Capuccino {MENU['capuccino']['cost']}"
                           f"\n4. Report of the remaining ingredients"
                           f"\nChoose an option: "))
    return user_order


def get_coins():
    pennies = int(input("How many pennies do you want to insert? "))
    nickels = int(input("How many nickels do you want to insert? "))
    dimes = int(input("How many dimes do you want to insert? "))
    quarters = int(input("How many quarters do you want to insert? "))

    total_pennies = pennies * 0.01
    total_nickels = nickels * 0.05
    total_dimes = dimes * 0.1
    total_quarters = quarters * 0.25
    total = total_pennies + total_nickels + total_dimes + total_quarters

    return total


def select_coffee(order):
    if order == 1:
        order_data = MENU["espresso"]
        return order_data, "espresso"
    elif order == 2:
        order_data = MENU["latte"]
        return order_data, "latte"
    elif order == 3:
        order_data = MENU["capuccino"]
        return order_data, "capuccino"
    elif order == 4:
        print(f"\nRemaining ingredients:"
              f"\nWater: {resources['water']}"
              f"\nMilk: {resources['milk']}"
              f"\nCoffee: {resources['coffee']}\n")
        get_order()


def calculate_change(total_paid, coffee_price):
    if total_paid > coffee_price:
        change = total_paid - coffee_price
        return change
    elif total_paid < coffee_price:
        return False
    else:
        return True


def calculate_resources(coffee_ingredients, remaining_resources):
    if "milk" in coffee_ingredients:
        milk_needed = coffee_ingredients["milk"]
        water_needed = coffee_ingredients["water"]
        coffee_needed = coffee_ingredients["coffee"]

        milk_remaining = remaining_resources["milk"]
        water_remaining = remaining_resources["water"]
        coffee_remaining = remaining_resources["coffee"]

        if milk_needed > milk_remaining:
            return {"ingredients_needed": coffee_ingredients,
                    "remaining_resources": remaining_resources,
                    "ableToMake": False}
        else:
            milk_remaining = milk_remaining - milk_needed
            water_remaining = water_remaining - water_needed
            coffee_remaining = coffee_remaining - coffee_needed
            return {"milk": milk_remaining,
                    "water": water_remaining,
                    "coffee": coffee_remaining,
                    "ableToMake": True}
    else:
        water_needed = coffee_ingredients["water"]
        coffee_needed = coffee_ingredients["coffee"]

        water_remaining = remaining_resources["water"]
        coffee_remaining = remaining_resources["coffee"]

        if water_needed > water_remaining:
            return {"ingredients_needed": coffee_ingredients,
                    "remaining_resources": remaining_resources,
                    "ableToMake": False}

        if coffee_needed > coffee_remaining:
            return {"ingredients_needed": coffee_ingredients,
                    "remaining_resources": remaining_resources,
                    "ableToMake": False}

        water_remaining = water_remaining - water_needed
        coffee_remaining = coffee_remaining - coffee_needed

        return {"milk": remaining_resources['milk'],
                "water": water_remaining,
                "coffee": coffee_remaining,
                "ableToMake": True}


def make_coffee(ingredients_count):
    selected_coffee, coffee_name = select_coffee(get_order())
    total_coins = get_coins()
    enough_resources = calculate_resources(selected_coffee['ingredients'], ingredients_count)

    if enough_resources['ableToMake']:
        change = calculate_change(total_coins, selected_coffee['cost'])
        ingredients_count
        if isinstance(change, float):

            print(f"Here is your {coffee_name}")
            print(f"Here is your change: {change}")
            print(f"Remaining ingredients:"
                  f"\nMilk: {remaining_ingredients['milk']}"
                  f"\nWater: {remaining_ingredients['water']}"
                  f"\nCoffee: {remaining_ingredients['coffee']}")
            more_coffee = input("Do you want to buy anything else (y/n)?")
            if more_coffee == "y":

        elif change is True:
            remaining_ingredients['milk'] = enough_resources['milk']
            remaining_ingredients['water'] = enough_resources['water']
            remaining_ingredients['coffee'] = enough_resources['coffee']
            print(f"Here is your {coffee_name}")
            print(f"No change.")
            print(f"Remaining ingredients:"
                  f"\nMilk: {remaining_ingredients['milk']}"
                  f"\nWater: {remaining_ingredients['water']}"
                  f"\nCoffee: {remaining_ingredients['coffee']}")
        else:
            print("Not enough money.")
            more_coins = input()


def decrease_ingredients(ingredients_count):



def main():
    remaining_ingredients = resources


    while True:


main()