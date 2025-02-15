import os

logo = """
     +------{
    [_]
    _-_
"""
bidder_list = {}
def findBidWinner():
    name = ""
    price = 0.0
    for key in bidder_list:
        if  bidder_list[key] > price:
            price = bidder_list[key]
            name = key
    
    print(f"Winner of bid is {name} with price of {price}")

state = True
while state:
    print(logo)
    in_name = input("What is your name? \n:")
    in_price = float(input("What is your bid? \n:"))

    bidder_list[in_name] = in_price

    ans = input("Are there any offer? y or n \n:")

    if ans.lower() == "n":
        state = False
        findBidWinner()
    else:
        os.system("cls")


