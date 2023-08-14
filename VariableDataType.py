name = "Mr.Pilon"
age = 38
print(f"Hi my name is {name}. I am {age} years old.")
print("Hi my name is {}. I am {} years old.".format(name, age))

#int, float, bool
intro = "Once upon a time there was a living ice cream. Of course, the ice cream was not always alive."
object = True
alive = ", like every other icecream it started out as an object.  Luckily for this icecream, it soon gain \nconsciousness."
time = "On April"
day = 1
year = 2055
awaken = ", the living icecream woke up to find that"
ate = 0.1
gone = ("of its body \n"
        "was gone. Oh what a horror! Fortunately the ice cream could not feel pain. Thus, the ice cream lived \n"
        "happily every after, exploring the new world it was now in.")

theend = "\n╱╭╮╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮"\
         "\n╭╯╰┫┃╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃"\
         "\n╰╮╭┫╰━┳━━╮╭━━┳━╮╭━╯┃"\
         "\n╱┃┃┃╭╮┃┃━┫┃┃━┫╭╮┫╭╮┃"\
         "\n╱┃╰┫┃┃┃┃━┫┃┃━┫┃┃┃╰╯┃"\
         "\n╱╰━┻╯╰┻━━╯╰━━┻╯╰┻━━╯"

print(f"{intro} {object}\n{alive} On April {day} of the year {year}{awaken} {ate} {gone} {theend}")

print("\nOnce upon a time there was a living ice cream. Of course, the ice cream was not always alive."
      "{} \n, like every other icecream it started out as an object.  Luckily for this icecream, it soon gain "
      "\nconsciousness. On April {} of the year {}, the living icecream woke up to find that {} of its body"
      "\nwas gone. Oh what a horror! Fortunately the ice cream could not feel pain. Thus, the ice cream lived"
      "\nhappily every after, exploring the new world it was now in. {}".format(object, day, year, ate, theend))



