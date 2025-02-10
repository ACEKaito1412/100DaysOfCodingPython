print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want?  S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extraCheese = input("Do you want extra cheese? Y or N: ")


bill = 0;
if size == "S":
    bill += 15;
elif size == "M":
    bill += 20
else:
    bill += 25

if pepperoni == "Y":
    bill += 2

if extraCheese == "Y":
    bill += 1

print(f"Your final bill is {bill}")