"""
    namespaces and scope
    - local scope - can be accessable only inside the function
    - global scope - variable define outside the function
"""

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


print(is_prime(73))
print(is_prime(75))
