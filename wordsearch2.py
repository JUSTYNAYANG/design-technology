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


grid = generategrid(18)
printgrid(grid)


def insert(word, row, col, dir):
    lword = list(word.lower())
    if dir == "right":
        for i in range(len(lword)):
            grid[row][col+i] = lword[i]
    elif dir == "left":
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row][col - i] = lword[i]
    elif dir == "down":
        for i in range(len(lword)):
            grid[row + i][col] = lword[i]
    elif dir == "up":
        lword = lword[::-1]
        for i in range(len(lword)):
            grid[row - i][col] = lword[i]
    # elif dir == "upleft":
    #     for i in range(len(lword)):
    #         grid[row - i][col-i] = lword[i]
    # elif dir == "upright":
    #     for i in range(len(lword)):
    #         grid[row - i][col+i] = lword[i]
    # elif dir == "downleft":
    #     for i in range(len(lword)):
    #         grid[row + i][col-i] = lword[i]
    # elif dir == "downright":
    #     for i in range(len(lword)):
    #         grid[row + i][col+i] = lword[i]

print("\n")

insert("kiwi", 1, 0, "right")
insert("leave", 1, 15, "left")
insert("dash", 5, 4, "down")
insert("up", 6, 1, "up")
# insert("um", 7, 10, "upleft")
# insert("rule", 10, 3, "upright")
# insert("drop", 5, 15, "downleft")
# insert("kiwi", 11, 10, "downright")

printgrid(grid)
