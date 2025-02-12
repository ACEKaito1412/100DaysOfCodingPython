import random
import hangmanArt

LIFE = 5
wordList = ["build", "house", "science"]
word = random.choice(wordList)
ans = []
for i in range(0, len(word)):
    ans.extend(" ")

def checker(guess):
    for i in range(0, len(word)):
        if word[i] == guess:
            ans[i] = guess
    

def fitter():
    answered = ""
    s = ""
    for i in ans:
        if i == " ":
            answered += "_ "
            s += "_"
        else:
            answered += f"{i} "
            s += i
    
    print(answered)
    if s == word:
        return True
    else:
        return False

def displayHangman(nLife):
    print(hangmanArt.hangman[nLife])

print("Your word to guess is: ")
print(f"_ " * len(word))

state = True
lives = LIFE
while(state):
    print(f"Lives: {lives} / {LIFE}")
    guess = input("Guess: ")
    if(guess in word):
        print("ok")
        checker(guess)
        if(lives != LIFE):
            lives += 1
    else:
        print("not ok")
        lives -= 1

    displayHangman(lives)

    if(lives == 0):
        print("Game is over")
        state = False

    if(fitter()):
        print("You've won")
        state = False

