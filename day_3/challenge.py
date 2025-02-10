print("""
\/       \\
  ___  _@@       @@_  ___
 (___)(_)         (_)(___)
 //|| ||           || ||\\
""")
print("There was an ant name anthony who has a friend antonio\n" +
      "they have live in a small borrow with there colony\n" +
      "One day antonio went missing, and anthony wanted to find him.\n" +
      "Please help anthony find his friend.")

answer = input("Do you want to help anthony? y or n :")
gameState = True
if(answer == "y" or answer == "Y"):
    answer = input("You walk for a while and found a sweet sugar. \na: Call a member \nb: continue walking\n:")

    if(answer == "b" or answer == "B"):
        answer = input("You continue walking, and found a kid playing with his parents.\n"+
        "They seem at a little picknick.\na: look around and bite the kid. \nb: go near the basket. \n:")

        if(answer == "b" or answer == "B" ):
            answer = input("You found antonio eying the huge apple." +
            "\na: Talk and eat with antonio \nb: You help Antonio go back already. " + 
            "\nc: You put an apple on his back.\n:")

            if(answer == "a" or answer == "A"):
                print("You chatted to much and got drunk on the grapes and accidenttaly roled over an apple.")
            elif(answer == "b" or answer == "B"):
                print("You went back home safety with antonio. You see antonio live the day."+
                      "\nYou win.");
            else:
                print("You actually try to put apple on antonio's back.")
                gameState = False
        else:
            print("You've bitten a kid, your looking for death, you died. The other day.")
    else:
        print("You took too long to find a member of your collony.")
        gameState = False
else:
    gameState == False


if gameState == False:
    print("Other member of your collony sees his body with a huge apple at its back. Antonio died.")
    print("Game Over!!")