from random import randint
color = ["\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
ENDC = "\033[m"

letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
          't', 'u', 'v', 'w', 'x', 'y', 'z']
wordlist = []
wordplace = []
worddir = []
def generategrid(size):
    import random
    wordsquare = []
    for i in range(size):
        wordsquare.append([])
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
              't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in range(size):
        for j in range(size):
            wordsquare[i].append(["\033[37m",letter[random.randint(0, 24)]])

    return wordsquare


def printgrid(wordsquare):
    for i in wordsquare:
        for j in i:
            print(j[0], j[1], ENDC, end="")
        print("")



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
        for j in item:
            print(j[0], j[1], ENDC, end="")
        print(" ")
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
            grid[row][col+i][1] = lword[i]
    elif "left" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row][col - i][1] = lword[i]
    elif "down" in dir:
        for i in range(len(lword)):
            grid[row + i][col][1] = lword[i]
    elif "up" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row - i][col][1] = lword[i]

# insert("kiwi", 1, 0, "right")
# insert("leave", 1, 15, "left")
# insert("dash", 5, 4, "down")
# insert("up", 6, 1, "up")

# printgrid(grid)
more = 1
while more == 1:
    wor = input("What word would you like to input?\n --> ").lower()
    start = input("Please enter starting point. \n --> ").lower()
    dir = input("Please enter the direction. (left, right, up, down)\n --> ").lower()
    r = list(start)
    for i in range(size):
        co = 0
        for j in letter:
            if j in r:
                r.remove(j)
                col = co
                break
            co += 1
        row = int("".join(r))-1
    if isValid(wor, row, col, dir):
        insert(wor, row, col, dir)
        wordlist.append(wor)
        wordplace.append(start)
        worddir.append(dir)
    else:
        print("Sorry, that was an invalid entry. Please try again")
        continue

    inputprintgrid(grid)
    more = int(input("Would you like to add more word(s)? (1 = yes, 0 = no)\n --> "))

def check(word, row, col, dir):
    lword = list(word.lower())
    if "right" in dir:
        for i in range(len(lword)):
            if lword[i] == grid[row][col+i][1]:
                return True
            else:
                return False
    elif "left" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            if lword[i] == grid[row][col - i][1]:
                return True
            else:
                return False
    elif "down" in dir:
        for i in range(len(lword)):
            if lword[i] == grid[row + i][col][1]:
                return True
            else:
                return False
    elif "up" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            if lword[i] == grid[row - i][col][1]:
                return True
            else:
                return False
def colorword(word, row, col, dir):
    clr = color[randint(0, 4)]
    lword = list(word.lower())
    if "right" in dir:
        for i in range(len(lword)):
            grid[row][col + i][0] = clr
    elif "left" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row][col - i][0] = clr
    elif "down" in dir:
        for i in range(len(lword)):
            grid[row + i][col][0] = clr
    elif "up" in dir:
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row - i][col][0] = clr



while wordlist != []:
    worr = input("What word did you find?\n --> ").lower()
    startt = input("What is its starting point? \n --> ").lower()
    dirr = input("What Direction? (left, right, up, down)\n --> ").lower()
    rr = list(startt)
    coo = 0
    for j in letter:
        if j in rr:
            rr.remove(j)
            break
        else:
            coo += 1
    roww = int("".join(rr))-1
    if worr in wordlist:
        if check(worr, roww, coo, dirr):
                print("Found it!")
                colorword(worr, roww, coo, dirr)
                inputprintgrid(grid)
                wordlist.remove(worr)
        else:
            print("Right word, wrong start or direction, please try again ")
    else:
        print("This is not even a word you are supposed to look for!!!")



