logo ="""
CALCULATOR
"""

def add(fn, sn):
    return fn + sn

def subtract(fn, sn):
    return fn - sn

def multiply(fn, sn):
    return fn * sn

def divide(fn, sn):
    return fn / sn

state = True
first_n = 0
sec_n = 0
ans = 0
calculate = ""
while state:
    print(logo)
    if calculate.lower() != "y":
        first_n = int(input("Whats the first number? : "))
    else:
        first_n = ans

    print("+\n-\n*\n/\n")
    operation = input("Pick an operation: ")
    sec_n = int(input("What's the next number? : "))

    if operation == "+":
        ans = add(first_n, sec_n)
    elif operation == "-":
        ans = subtract(first_n, sec_n)
    elif operation == "*":
        ans = multiply(first_n, sec_n)
    elif operation == "/":
        ans = divide(first_n, sec_n)
    else:
        operation = "+"
        ans = add(first_n, sec_n)

    print(f"{first_n} {operation} {sec_n} = {ans}")
    calculate = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calcualtion: ")
    