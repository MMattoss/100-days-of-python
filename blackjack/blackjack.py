import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
dealer_cards = []
playerSum = 0
dealerSum = 0

def dealCards():
    global playerSum
    global dealerSum

    player_cards.append(cards[random.randint(0,12)])
    dealer_cards.append(cards[random.randint(0,12)])

    print(f"Your cards: {player_cards}")
    print(f"Dealer card: {dealer_cards[0]}")

    playerSum = sum(player_cards)

    dealerSum = sum(dealer_cards)

    
    if playerSum > 21:
        print(f"You lost! :( \nYour cards: {player_cards} Total: {playerSum}\n")

    else:
        newDeal = input("Do you wish to keep going? (y/n)\n")

        if newDeal == "y" or newDeal == "Y":
            dealCards()

        else:
            if dealerSum < 17:
                dealer_cards.append(cards[random.randint(0,12)])
                dealerSum = sum(dealer_cards)
            if playerSum > dealerSum:
                print(f"You lost! :( \nYour cards: {player_cards} Your total: {playerSum} \nDealer cards: {dealer_cards} Dealer total: {dealerSum}\n")
            elif playerSum == dealerSum:
                print(f"It's a tie! \nYour cards: {player_cards} Your total: {playerSum} \nDealer cards: {dealer_cards} Dealer total: {dealerSum}\n")
            else:
                print(f"You won!!! \nYour cards: {player_cards} Your total: {playerSum} \nDealer cards: {dealer_cards} Dealer total: {dealerSum}\n")
                repeat = input("Do you wish to play again? (y/n)")
                if repeat == "y" or repeat == "Y":
                    player_cards.clear()
                    dealer_cards.clear()
                    playerSum = 0
                    dealerSum = 0
                    dealCards()
                else:
                    print("Thanks for playing!")

            
dealCards()