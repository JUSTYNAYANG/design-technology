from colorama import Fore, Style

def bmi(w, h):
    m = w / h ** 2
    m = round(m, 2)
    return m

def starwars(n, w, h, q):
    b = bmi(w, h)
    if b < 15:
        c = "very severely underweight"
        d = Fore.YELLOW + "#"
        lw = Style.RESET_ALL + "You need to gain " + str(abs(b - 18.5 * h) + "kg."

    elif b < 16:
        c = "severely underweight"
        d = Fore.YELLOW + "##"
        lw = Style.RESET_ALL + "You need to gain " + str(abs(b - 18.5 * h) + "kg."

    elif b < 18.5:
        c = "underweight"
        d = Fore.YELLOW + "###"
        lw = Style.RESET_ALL + "You need to gain " + str(abs(b - 18.5 * h) + "kg."

    elif b < 25:
        c = "normal/healthy weight"
        d = Fore.GREEN + "####"
        lw = Style.RESET_ALL + "Your BMI is in a good range."

    elif b < 30:
        c = "overweight"
        d = Fore.RED + "#####"
        lw = Style.RESET_ALL + "You need to lose " + str(abs(b - 18.5 * h) + "kg."

    elif b < 35:
        c = "moderately obese"
        d = Fore.RED + "######"
        lw = Style.RESET_ALL + "You need to lose " + str(abs(b - 18.5 * h) + "kg."

    elif b < 40:
        c = "severely obese"
        d = Fore.RED + "#######"
        lw = Style.RESET_ALL + "You need to lose " + str(abs(b - 18.5 * h) + "kg."

    else:
        c = "very severely obese"
        d = Fore.RED + "########"
        lw = Style.RESET_ALL + "You need to lose " + str(abs(b - 18.5 * h) + "kg."

    e = Style.RESET_ALL + "########"

    answer = (f"{n}\n"
              f"----------\n"
              f"weight: {w}kg\n"
              f"height: {h}m\n"
              f"bmi: {str(b)} ({c})\n"
              f"{d}\n"
              f"{e}\n"
              f"{lw}"
              f"Quote: '{q}'\n")
    return print(answer)

starwars("Yoda", 13, 0.66, "No! Try not. Do. Or do not. There is no try.")
starwars("Luke Skywalker", 77, 1.8, "You Failed, Your Highness")
starwars("Princess Leia", 47, 1.5, "Aren't you a little short for a stormtrooper?")
starwars("Chewbacca", 110, 2.3, "RRWWWGG")
starwars("Rey Skywalker", 54, 1.65, "I Can Do This, I Can Do This.")
starwars("Darth Sidious", 75, 1.82, "There is no mercy.")
starwars("Darth Vader", 89, 1.8, "If You're Not With Me, Then You're My Enemy!")
starwars("Jabba the Hutt", 1361, 1.75 , "I want an incredible battle.")
