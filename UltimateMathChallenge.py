import time
from random import *

Continue = True
point = 0
high_score = 0
streak = 0

while Continue:
    if streak <= 10:
        x = randint(1,100)
        y = randint(1,100)
    else:
        x = randint(1, 1000)
        y = randint(1, 1000)
    start = time.time()
    a = input(f'\n What is {x} + {y}? \n'
              f'--> ')
    end = time.time()
    if end-start > 60:
        print(f"\nYou took too long! Better luck next time.\n"
              f"_______")
        print(f" Game over, you finished with {point} points.")
        if point > high_score:
            high_score = point
        print(f"High Score = {high_score}\n")

        userentry = input("Do you want to continue? ")
        if userentry.lower() != "yes":
            Continue = False
        else:
            streak = 0
            point = 0

    if int(a) == x+y:
        point += 1
        streak += 1
        print(f"Correct! You now have {point} points\n"
              f"_______")
    else:
        print(f"\nWrong! The answer is {x+y}\n"
              f"_______")
        print(f" Game over, you finished with {point} points.")
        if point > high_score:
            high_score = point
        print(f"High Score = {high_score}\n")

        userentry = input("Do you want to continue? ")
        if userentry.lower() != "yes":
            Continue = False
        else:
            streak = 0
            point = 0