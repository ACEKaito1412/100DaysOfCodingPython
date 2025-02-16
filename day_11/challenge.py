import random

#infinite cards:
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_card = []
comp_card = []
def giveCard():
    return random.choice(cards)

def givePlayerCards():
    player_card.append(giveCard())
    comp_card.append(giveCard())
    player_card.append(giveCard())
    comp_card.append(giveCard())

def showResults():
    print(f"Your final hand: {player_card}, score: {sum(player_card)}")
    print(f"Computer's final hand: {comp_card}, score: {sum(comp_card)}")

state = True

gameStart = True
while gameStart:
    ans = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if ans.lower() == "y":
        gameStart = True
        state = True

        while state:
            if(len(player_card) == 0):
                givePlayerCards()
            

            player_total = sum(player_card)
            comp_total = sum(comp_card)
            print(f"Your cards: {player_card}, current score: {player_total}")
            print(f"Computer's first card: {comp_card[0]}")

            ans = input("Type 'y' to get another card, type 'n' to pass: ")
            if ans.lower() == "n":
                while comp_total < 17:
                    comp_card.append(giveCard())
                    comp_total = sum(comp_card)
                
                showResults()

                if player_total > 21:
                    print("Comp win")
                elif comp_total > 21:
                    print("You win")
                elif player_total > comp_total:
                    print("You win")

                comp_card.clear()
                player_card.clear()
                state = False
            elif ans.lower() == "y":
                player_card.append(giveCard())

                player_total = sum(player_card)

                if player_total > 21:
                    showResults()
                    print("You lose")
                    comp_card.clear()
                    player_card.clear()
                    state = False

    else:
        gameStart = False
