letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
          't', 'u', 'v', 'w', 'x', 'y', 'z']
def generategrid(size):
    import random
    wordsquare = []
    for i in range(size):
        wordsquare.append([])
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(size):
        for j in range(size):
            wordsquare[i].append(letter[random.randint(0, 24)])

    return wordsquare

def printgrid(wordsquare):
    for item in wordsquare:
        print("  ".join(item))


def inputprintgrid(wordsquare):
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 1
    print("    ", end = " ")
    for i in range(len(wordsquare[0])):
        print(letter[i], end="  ")
    print("\n     "+ "_"*(len(wordsquare[0])*3))
    for item in wordsquare:
        if count <10:
            print(" " + str(count) + " |", end=" ")
        else:
            print(str(count) + " |", end=" ")
        print("  ".join(item))
        count += 1

def isValid(wor, row, col, dir):
    if dir == "right":
        if len(wor)+col > size:
            return False
        else:
            return True
    elif dir == "left":
        if col-len(wor) < 0:
            return False
        else:
            return True
    elif dir == "down":
        if row + len(wor) > size:
            return False
        else:
            return True
    elif dir == "up":
        if row - len(wor) < 0:
            return False
        else:
            return True


size = 18
grid = generategrid(size)
printgrid(grid)
print("\n")
inputprintgrid(grid)
print("\n")

def insert(word, row, col, dir):
    lword = list(word.lower())
    if "right" in dir:
        for i in range(len(lword)):
            grid[row][col+i] = lword[i]
    elif "left" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row][col - i] = lword[i]
    elif "down" in dir:
        for i in range(len(lword)):
            grid[row + i][col] = lword[i]
    elif "up" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row - i][col] = lword[i]

# insert("kiwi", 1, 0, "right")
# insert("leave", 1, 15, "left")
# insert("dash", 5, 4, "down")
# insert("up", 6, 1, "up")

# printgrid(grid)
more = 1
while more == 1:
    wor = input("What word would you like to input?\n --> ").lower()
    dir = input("Please enter the direction. (left, right, up, down)\n --> ").lower()
    start = list(input("Please enter starting point. \n --> ").lower())
    for i in range(size):
        co = 0
        for j in letter:
            if j in start:
                start.remove(j)
                col = co
                break
            co += 1
        row = int("".join(start))-1
    if isValid(wor, row, col, dir):
        insert(wor, row, col, dir)
    else:
        print("Sorry, that was an invalid entry. Please try again")
        continue



    inputprintgrid(grid)
    more = int(input("Would you like to add more word(s)? (1 = yes, 0 = no)\n --> "))

