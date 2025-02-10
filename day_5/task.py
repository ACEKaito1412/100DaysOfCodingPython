"""
    using loops: for loops
    helpful function sum(), max()
    using range function
"""

scores = [1,2,3,4,5,10]

print(max(scores))

max = 0
for score in scores:
    if(score > max):
        max = score

print(max)

sum = 0
for number in range(1, 101):
    sum += number

print(sum)

for number in range(1, 101):
    s = ""
    
    if number % 3 == 0 and number % 5 == 0:
        s = "FizzBuzz"
    elif number % 3 == 0:
        s = "Fizz"
    elif number % 5 == 0:
        s = "Buzz"
    else:
        s = str(number)
    
    print(s)