x = 0
r = 1
carddeck = []
blackjack = []
money = [1000, 1000, 1000]


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

def printMoney():
    for i in range(len(money)):
        print(f"Player {i+1}: ${money[i]}")
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


def payout(bet):
    for i in player:
        if isBust(dealer):
            if isBust(i):
                money[player.index(i)] -= int(bet[player.index(i)])
            else:
                if len(i) == 2 and is21(i):
                    money[player.index(i)] += int(bet[player.index(i)])*1.5
                else:
                    money[player.index(i)] += int(bet[player.index(i)])
        elif is21(dealer):
            money[player.index(i)] -= int(bet[player.index(i)])
        else:
            if len(i) == 2 and is21(i):
                money[player.index(i)] += int(bet[player.index(i)]) * 1.5
            else:
                if isBust(i):
                    money[player.index(i)] -= int(bet[player.index(i)])
                elif playerPoints(i) > playerPoints(dealer):
                    money[player.index(i)] += int(bet[player.index(i)])
                elif playerPoints(i) == playerPoints(dealer):
                    pass
                else:
                    money[player.index(i)] -= int(bet[player.index(i)])

def isBroke(hand):
    if money[player.index(hand)] == 0:
        return True
    else:
        return False

def isValidBet(hand, betAmount):
    if int(betAmount) > money[player.index(hand)]:
        return False
    else:
        return True


print("Welcome to Black Jack!")


while x != 3 and r == 1:
    player1 = []
    player2 = []
    player3 = []
    dealer = []
    player = [player1, player2, player3]
    bet = []
    for i in player:
        if isBroke(i):
            player.remove(i)
            x += 1
    for i in range(3):
        bet.append(int(input(f"Player {i + 1}, how much do you want to bet? ")))
        while isValidBet(player[i], bet[i]) == False:
            print(f"Your previous bet is not valid, you only have ${money[i]}.")
            bet[i] = int(input(f"Player {i + 1}, how much do you want to bet? "))


    for i in player:
        i.append(drawcard())
        i.append(drawcard())

    dealer.append(drawcard())
    dealer.append(drawcard())
    printCard(player1, "Player 1")
    printCard(player2, "Player 2")
    printCard(player3, "Player 3")
    printCard(dealer, "Dealer")
    printMoney()

    for i in player:
        if is21(i):
            print(f"\nPlayer {player.index(i) + 1} BLACKJACK!!! ")
            blackjack.append(player.index(i))

    for i in player:
        while (not isBust(i) and not is21(i)):
            o = input(f"\nPlayer {player.index(i) + 1}, Do you want to draw another card? (stand or hit) ")

            if o == "stand":
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
                    printCard(i, f"Player {player.index(i) + 1}")

    while (not isBust(dealer) and not is21(dealer)):
        if playerPoints(dealer) < 16:
            dealer.append(drawcard())
            u = determineCard(dealer[-1])
            print(f"\nDealer drew..... {u}")
            if isBust(i):
                print(f"The dealer busted!\n"
                      f"Dealer had a total of {playerPoints(i)} points.")
                break
            elif is21(i):
                print(f"Oh my, the dealer got 21 points in total!")
                break
        else:
            print("\n")
            printCard(dealer, "Dealer")
            break

    payout(bet)
    printMoney()

    r = int(input(f"Do you want to continue the game? (1:yes, 2:no) "))
