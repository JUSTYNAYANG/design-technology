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

    b = " of ".join(a)
    a.clear()

    return b


dealer = []
player1 = []
player2 = []
player3 = []

dealer.append(drawcard())
dealer.append(drawcard())
player1.append(drawcard())
player1.append(drawcard())
player2.append(drawcard())
player2.append(drawcard())
player3.append(drawcard())
player3.append(drawcard())
def cardoutput(b, c):
    print(c)
    print("------------")
    for i in b:
        print(i)
    print("------------\n")


cardoutput(dealer, "Dealer")
cardoutput(player1, "Player 1")
cardoutput(player2, "Player 2")
cardoutput(player3, "Player 3")



