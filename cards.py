from random import *

num = randint(1, 52)

if num <= 13:
    suit = "spades"
elif num <= 26:
    suit = "hearts"
elif num <= 39:
    suit = "clubs"
else:
    suit = "diamonds"

card = str(num% 13)


rounds = 0
print(" Welcome of Guess the Card!  You have a total of 5 chances to guess the card.")
# print(f"{card} of {suit}")
while True:
    if rounds < 6:
        c = 0
        d = 0
        a = input("\nPlease guess the card: ")
        a = a.lower()
        a = a.split()

        if a[0] < card:
            print("Your card number is too small.")
        elif a[0] > card:
            print("Your card number is too large. ")
        else:
            print("Your card number is correct ")
            d = 1

        if a[2] != suit:
            print("You guessed the wrong suit")
        else:
            print("Your suit is right")
            c = 1
        rounds += 1
        if d and c:
            print("You have guessed the right card!!")
            break

    else:
        print("\nYou have taken too many tries. The game ends here.")
        break