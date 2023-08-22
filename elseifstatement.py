#taste
taste = "sweet"

if taste == "bitter":
    print("Agh, it's so bitter!")
elif taste == "sour":
    print("sourrrr...Jasmine will like it")
elif taste == "spicy":
    print("hot, spicy, GIVE ME WATER, NO MILK")
elif taste == "sweet":
    print("sweet, blue sugar high~")
else:
    print("what is this?")

#Do you want to be a Millionare?

money = 0
print("What is the rarest M&M color?\n "
      "A: Blue "
      "B: Yellow "
      "C: Brown "
      "D: Red ")
a1= input()
if a1 == "C" or "c":
    money += 1
    print(f"Congratulations, you are correct, you now have ${money}!")
else:
    money = 0
    print(f"That is incorrect.")

#Complete Version
def question(q, a, m):
    print(q)
    b = input()
    if b == a:
        m += 100
        if m == 1000:
            print(f"You have WON the GAME!")
        else:
            print(f"Congratulations, you are correct, you now have ${m}!")

    else:
        print(f"That is incorrect. The correct answer is {a}")
        print("\n GAME OVER")
        exit()


print("Please input CAPITALIZED Answers\n")

question("\nWhat is the rarest M&M color?\n "
         "A: Blue "
         "B: Yellow "
         "C: Brown "
         "D: Red ", "C", 0)

question("\nHow many of Snow White’s seven dwarfs have names ending in the letter Y?\n "
         "A: 5 "
         "B: 8 "
         "C: 2 "
         "D: 4 ", "A", 100)

question("\nWhat is the tallest breed of dog in the world?\n "
         "A: Golden Retriever "
         "B: Great Dane "
         "C: Siberian Husky "
         "D: Poodle", "B", 200)

question("\nHow many ribs are in a human body?\n "
         "A: 25 "
         "B: 24 "
         "C: 22 "
         "D: 28", "B", 300)

question("\nWhich planet is the hottest in the solar system?\n "
         "A: Mercury "
         "B: Mars "
         "C: Venus "
         "D: Saturn", "C", 400)

question("\nWho invented scissors?\n "
         "A: Leonardo Da Vinci "
         "B: Thomas Edison "
         "C: Benjamin Franklin "
         "D: Alexander Graham Bell", "A", 500)

question("\nWhat is the most common letter in the English alphabet?\n "
         "A: A "
         "B: N "
         "C: I "
         "D: E", "D", 600)

question("\nWhat is the first element on the Periodic Table?\n "
         "A: Helium "
         "B: Hydrogen "
         "C: Lithium "
         "D: Oxygen", "B", 700)

question("\nWhat’s the brightest star in the sky?\n "
         "A: Altair "
         "B: Draco "
         "C: Vega "
         "D: Sirius", "D", 800)

question("\nWhich insect can indicate the air temperature?\n "
         "A: Cricket "
         "B: Flea "
         "C: Butterfly "
         "D: Bee", "A", 900)