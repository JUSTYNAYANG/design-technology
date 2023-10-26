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


player1 = [13, 5, 17]
player2 = [12, 11, 21]
player3 = [24, 14]

print(playerPoints(player1))
print(isBust(player1))
print(is21(player1))
print(playerPoints(player2))
print(isBust(player2))
print(is21(player2))
print(playerPoints(player3))
print(isBust(player3))
print(is21(player3))
