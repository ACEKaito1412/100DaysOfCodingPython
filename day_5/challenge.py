import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator")
nrLetters = int(input("How many letters would you like in your password: "))
nrSymbols = int(input("How many symbols would you like in your password: "))
nrNumbers = int(input("How many numbers would you like in your password: "))

randPass = []

for n in range(0, nrLetters):
    randPass.extend(random.choice(letters))

for n in range(0, nrSymbols):
    randPass.extend(random.choice(symbols))

for n in range(0, nrNumbers):
    randPass.extend(random.choice(numbers))

password = ""
nLenght = len(randPass);
print(nLenght)
for n in range(0, nLenght):
    choice = random.choice(randPass)
    password += choice
    randPass.remove(choice)
    nLenght = len(randPass);

print(password)