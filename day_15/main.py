
recipe = {
    'espresso' : {'water' : 50, 'coffee' : 18, 'milk' : 0, 'price' : 1.50},
    'latte' : {'water' : 200, 'coffee' : 24, 'milk' : 150, 'price' : 2.50},
    'cappuccino' : {'water' : 250, 'coffee' : 24, 'milk' : 100, 'price' : 3.00},
}

resources = {
    'water' : 300,
    'milk' : 200,
    'coffee' : 100,
    'cash' : 0
}

# penny 1 cent = 0.01, nickel 5 cents 0.05, dime 10 cents: 0.10 quarter: 0.25

def checkResources(recipeName):
    order = recipe[recipeName]

    for item in resources:
        if item != 'cash':
            if order[item] <= resources[item]:
                continue
            else:
                print(f"Sorry not enough {item}.")
                return False

    return True

def printResources():
    for item in resources:
        print(f"{item.capitalize()} : {resources[item]}")

def createOrder(recipeName):
    order = recipe[recipeName]

    for item in resources:
        if item != 'cash':
            if order[item] <= resources[item]:
                resources[item] -= order[item]

    print(f"Here is your {recipeName}. Enjoy!!")

def depositAmount(n):
    resources['cash'] += n 

state = True
while state:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        printResources()
    elif choice == 'off':
        state = False
    elif checkResources(choice):
        print("Please insert coins.")
        quarter = int(input("How many quarters? : "))
        dime = int(input("How many dimes? : "))
        nickle = int(input("How many nickles? : "))
        pennie = int(input("How many pennies? : "))

        total = (pennie * 0.01) + (nickle * 0.05) + (dime * 0.10) + (quarter * 0.25)
        price = recipe[choice]['price']
        if total < price:
            print("Not enough coins: Refunded")
        else:
            if(total > price):
                changes = round(total - price, 2)
                print(f"Here is your change: {changes}")
            
            depositAmount(price)
            createOrder(choice)
    

