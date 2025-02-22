from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



# penny 1 cent = 0.01, nickel 5 cents 0.05, dime 10 cents: 0.10 quarter: 0.25

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

state = True
while state:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        state = False
    elif coffee_maker.is_resource_sufficient(menu.find_drink(choice)):
        item = menu.find_drink(choice)

        if money_machine.make_payment(item.cost):
            coffee_maker.make_coffee(item)
    

