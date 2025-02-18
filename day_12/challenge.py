import random

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10
attempts = 0
secret_number = 0

game_state = True

print("Welcome to number the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
secret_number = random.randint(1, 100)
print(f"Secret: {secret_number}")
choice = input("Choose a difficulty: 'easy' or 'hard': ")

if choice.lower()  == "easy":
    attempts = EASY_ATTEMPTS
else:
    attempts = HARD_ATTEMPTS


while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == secret_number:
        print("You Win!!")
        attempts = 0
    elif guess > secret_number:
        print("To High")
        attempts -= 1
    elif guess < secret_number:
        print("To Low")
        attempts -= 1
