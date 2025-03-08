#  create a fucntion that can accept any amount of number and outpul all the sume

def add(*args):
    total = 0
    for n in args:
        total += n
    
    return total



print(add(1,2,3,4,5,6,7,8,9,10))