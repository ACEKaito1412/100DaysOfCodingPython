"""
    random module
    creating your own module
    most use random function is random.random 
    generate float between 0 -> 1
    data structures for a list
    adding item, extend
    index out of range
    nested list
"""

import random

# heads and tail generator

state = False
while(state):
    n = input("Start: a: heads or b: tail c: exit \n:")
    x = random.randint(0, 1)

    if n.lower() == "a" and x == 0:
        print("Its head you win")
    elif n.lower() == "b" and x == 1:
        print("Its tails you lose")
    elif n.lower() == "c":
        state = False        
    else:
        s ="heads" if x == 0 else "tails"
        print(f"You lose its {s}")


# using list

myFriends = ["Jerry", "Romeo" , "JR" , "Robert"]

x = random.randint(0, len(myFriends)-1)

print(myFriends[x])