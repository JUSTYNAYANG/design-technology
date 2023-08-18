def bmi(w, h):
    BMI = w / h ** 2
    BMI = round(BMI, 2)
    return(str(BMI))

def starwars(n, w, h, q):
    answer = (f"{n}\n"
              f"----------\n"
              f"weight: {w}kg\n"
              f"height: {h}m\n"
              f"bmi: {bmi(w, h)}\n"
              f"Quote: '{q}'\n")
    return(print(answer))

starwars("Yoda", 13, 0.66, "No! Try not. Do. Or do not. There is no try.")
starwars("Luke Skywalker", 77, 1.8, "You Failed, Your Highness")
starwars("Princess Leia", 47, 1.5, "Aren't you a little short for a stormtrooper?")
starwars("Chewbacca", 110, 2.3, "RRWWWGG")
starwars("Rey Skywalker", 54, 1.65, "I Can Do This, I Can Do This.")
starwars("Darth Sidious", 75, 1.82, "There is no mercy.")
starwars("Darth Vader", 89, 1.8, "If You're Not With Me, Then You're My Enemy!")
starwars("Jabba the Hutt", 1361, 1.75 , "I want an incredible battle.")










