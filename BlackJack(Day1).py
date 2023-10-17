carddeck = []
a = []
for i in range(52):
    carddeck.append(i+1)

import random

random.shuffle(carddeck)

def drawcard():
    card = carddeck.pop(0)
    cn = card%13
    if cn == 11:
        a.append("Jack")
    elif cn == 12:
        a.append("Queen")
    elif cn == 13:
        a.append("King")
    else:
        a.append(str(cn))

    if card < 14:
        a.append("Hearts")
    elif card < 27:
        a.append("Diamonds")
    elif card < 40:
        a.append("Clubs")
    else:
        a.append("Spades")

    print(" of ".join(a))
    a.clear()

def cardoutput(b):
    print(b)
    print("------------")
    drawcard()
    drawcard()
    print("------------\n")

cardoutput("Dealer")
cardoutput("Player 1")
cardoutput("Player 2")
cardoutput("Player 3")