import random


rock = """  
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
moves = [rock,paper,scissor]

choice = int(input("What do you choose? \n0: rock | 1: paper | 2: scissor\n:"))
n = random.randint(0, len(moves) -1)

print(moves[choice])
print(f"Computer chose: \n{moves[n]}")

if n == choice:
    print("Its a draw")
elif n == 0 and choice == 1:
    print("You win!!")
elif n == 0 and choice == 2:
    print("You lose!!")
elif n == 1 and choice == 0:
    print("You lose!!")
elif n == 1 and choice == 2:
    print("You win!!")
elif n == 2 and choice == 0:
    print("You win!!")
elif n == 2 and choice == 1:
    print("You lose!!")