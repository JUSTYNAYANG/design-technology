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


grid = generategrid(24)
printgrid(grid)

