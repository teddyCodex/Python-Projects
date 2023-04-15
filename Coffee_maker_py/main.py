from backend import menu
from backend import resources
from backend import coins


# function to check resources
def check_resources(coffee_choice):
    water_needed = menu[coffee_choice]['ingredients']['water']
    milk_needed = menu[coffee_choice]['ingredients']['milk']
    coffee_needed = menu[coffee_choice]['ingredients']['coffee']
    if water_needed > resources['water']:
        print("Sorry. Not enough water")
    elif milk_needed > resources['milk']:
        print("Sorry. Not enough milk")
    elif coffee_needed > resources['coffee']:
        print("Sorry. Not enough coffee")
    else:
        return water_needed, milk_needed, coffee_needed


def deplete_resources(water_needed, milk_needed, coffee_needed):
    resources['water'] -= water_needed
    resources['milk'] -= milk_needed
    resources['coffee'] -= coffee_needed


def check_coins(quarters, dimes, nickels, pennies):
    total_quarters = quarters * coins['quarter']
    total_dimes = dimes * coins['dime']
    total_nickels = nickels * coins['nickel']
    total_pennies = pennies * coins['penny']
    return total_quarters + total_dimes + total_nickels + total_pennies


def amount_needed(coffee_choice):
    return menu[coffee_choice]['cost']


def collect_coins():
    print('Please insert coins.')
    quarters = input('How many quarters?: ')
    dimes = input('How many dimes?: ')
    nickels = input('How many nickels?: ')
    pennies = input('How many pennies?: ')
    if not (quarters.isdigit() and dimes.isdigit() and nickels.isdigit() and pennies.isdigit()):
        print("Invalid input. Please enter only numbers.")
        return collect_coins()
    return quarters, dimes, nickels, pennies


def coffee_engine():
    make_coffee = check_resources(user_choice)
    if make_coffee is None:
        return
    else:
        deplete_resources(make_coffee[0], make_coffee[1], make_coffee[2])
        coins_collected = collect_coins()
        coins_total = check_coins(int(coins_collected[0]), int(coins_collected[1]), int(coins_collected[2]), int(coins_collected[3]))
        if amount_needed(user_choice) > coins_total:
            print("Not enough money. Coins refunded")
        else:
            balance = coins_total - amount_needed(user_choice)
            if 'money' in resources:
                resources['money'] += amount_needed(user_choice)
            else:
                resources['money'] = amount_needed(user_choice)
            print(f"\nHere's your Balance: ${balance:.2f}. Enjoy your {user_choice} ☕️\n")


def generate_report():
    print("\n*** SUMMARY REPORT ***")
    if 'money' not in resources:
        resources['money'] = 0
    for resource, amount in resources.items():
        if resource == 'water' or resource == 'milk':
            print(f"{resource.capitalize()}: {amount}ml")
        elif resource == 'coffee':
            print(f"{resource.capitalize()}: {amount}g")
        else:
            print(f"{resource.capitalize()}: ${amount}")
    print('\n')


coffee_maker = 'on'

while coffee_maker == 'on':
    # display prices of the available coffee options
    for item_name, item_info in menu.items():
        print(f"{item_name.capitalize()} at ${item_info['cost']:.2f} ")

    # ask user to choose from available options
    user_choice = input("\nWhat would you like?: ").lower()
    if user_choice == 'report':
        generate_report()
    elif user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        coffee_engine()
    elif user_choice == 'off':
        quit()
    else:
        print('Invalid Input')
