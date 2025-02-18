
# global scope
player_health = 10

def drink_potion():
    # Local scope
    player_potion = 2

    player_health += 10

# print(player_potion) cant acces the variable


def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
            
    return True


print(int(75 ** 0.5) + 1)
