carddeck = []
a = []
for i in range(52):
    carddeck.append(i+1)

import random

random.shuffle(carddeck)


def drawcard():
    return carddeck.pop(0)


def printCard(b, c):
    print(c)
    print("------------")
    for i in b:
        cn = i % 13
        if cn == 11:
            a.append("Jack")
        elif cn == 12:
            a.append("Queen")
        elif cn == 0:
            a.append("King")
        elif cn == 1:
            a.append("Ace")
        else:
            a.append(str(cn))

        if i < 14:
            a.append("Hearts")
        elif i < 27:
            a.append("Diamonds")
        elif i < 40:
            a.append("Clubs")
        else:
            a.append("Spades")

        b = " of ".join(a)
        a.clear()
        print(b)
    print("------------\n")


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

print(dealer)
printCard(dealer, "Dealer")
print(player1)
printCard(player1, "Player 1")
print(player2)
printCard(player2, "Player 2")
print(player3)
printCard(player3, "Player 3")



def playerPoints(hand):
    sum = 0
    for i in hand:
        cn = i%13
        if cn == 11:
            sum += 10
        elif cn == 12:
            sum += 10
        elif cn == 0:
            sum += 10
        elif cn == 1:
            if sum + 11 > 21:
                sum += 1
            else:
                sum += 11
        else:
            sum += cn
    return sum

# trial = [13,6]
# print(playerPoints(trial))

print(playerPoints(dealer))
print(playerPoints(player1))
print(playerPoints(player2))
print(playerPoints(player3))
