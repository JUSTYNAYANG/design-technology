carddeck = []
for i in range(52):
    carddeck.append(i+1)

import random

random.shuffle(carddeck)


def drawcard():
    return carddeck.pop(0)


def determineCard(i):
    a = []
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

    b =  " of ".join(a)
    return b
def printCard(b, c):
    print(c)
    print("------------")
    for i in b:
        b = determineCard(i)
        print(b)
    print("------------\n")


    return b


player1 = []
player2 = []
player3 = []
dealer = []


player1.append(drawcard())
player1.append(drawcard())
player2.append(drawcard())
player2.append(drawcard())
player3.append(drawcard())
player3.append(drawcard())
dealer.append(drawcard())
dealer.append(drawcard())

print("Welcome to Black Jack!  Here are your cards:")

print(player1)
printCard(player1, "Player 1")
print(player2)
printCard(player2, "Player 2")
print(player3)
printCard(player3, "Player 3")
print(dealer)
printCard(dealer, "Dealer")



def playerPoints(hand):
    sum = 0
    ace = 0
    for i in hand:
        cn = i%13
        if cn == 11:
            sum += 10
        elif cn == 12:
            sum += 10
        elif cn == 0:
            sum += 10
        elif cn == 1:
            ace += 1
            sum += 1
        else:
            sum += cn
    for i in range(ace):
        if sum-1 + 11 <= 21:
            sum += 10
    return sum


def isBust(hand):
    if playerPoints(hand) > 21:
        #is bust
        return True
    else:
        return False

def is21(hand):
    if playerPoints(hand) == 21:
        #is 21
        return True
    else:
        return False

player = [player1, player2, player3, dealer]

for i in player:
    while (not isBust(i) and not is21(i)):
        if i == dealer:
            o = input(f"Dealer, Do you want to draw another card? (stand or hit) ")
        else:
            o = input(f"Player {player.index(i) + 1}, Do you want to draw another card? (stand or hit) ")

        if o == "stand":
            if i == dealer:
                printCard(i, f"Dealer")
            else:
                printCard(i, f"Player {player.index(i) + 1}")
            break
        elif o == "hit":
            i.append(drawcard())
            u = determineCard(i[-1])
            print(f"You drew..... {u}")
            if isBust(i):
                print(f"Too bad, you busted!\n"
                      f"You have a total of {playerPoints(i)} points.")
                break
            elif is21(i):
                print(f"Congratulations! !\n"
                      f"You have a total of 21 points! ")
                break
            else:
                if i == dealer:
                    printCard(i, f"Dealer")
                else:
                    printCard(i, f"Player {player.index(i) + 1}")







