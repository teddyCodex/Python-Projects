from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    Coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    
    while True:
        print('\n')
        user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
        
        if user_choice == 'off':
            exit()
        if user_choice == 'report':
            Coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(user_choice)
            if Coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        Coffee_maker.make_coffee(drink)

if __name__ == '__main__':
    main()