import art
import data
import random


state = True
score = 0
print(art.logo)
while state:
    a = random.choice(data.data)
    b = random.choice(data.data)
    print(f"Compare A: {a['name']}, {a['description']}")
    print(art.vs)
    print(f"Compare B: {b['name']}, {b['description']}")
    choice = input("Who has more followers? Type 'a' or 'b': ")

    if choice.lower() == "a":
        if a['follower_count'] > b['follower_count']:
            score += 1
        else:
            state = False
    else:
        if b['follower_count'] > a['follower_count']:
            score += 1
        else:
            state = False

    if(state == False):
        print(f"Score: {score}")


    
