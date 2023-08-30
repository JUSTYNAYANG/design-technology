# >< signs
max_speed = int(input("What is the maximium speed of your car? "))
if max_speed < 180:
    print("It is an old car.")
elif max_speed < 200:
    print("This is a family car.")
elif max_speed < 250:
    print("Wow! A luxury car.")
else:
    print("Vroom, sports car!")


#movie entry
print("This is the line to see the movie 'Super Zombie Massacre'.")
movie = input("What is your favorite movie genre? \n"
              "(action, adventure, comedy, drama, fantasy, horror, romance, science fiction) \n ")

age = int(input("What is your age? "))

if age < 7:
    print("You're joking right? Let me go get you some Teletubbies vids!")
elif age < 14:
    print("Nice try kiddie, the horror of this movie is not for the innocent-minded!")
elif age < 18:
    print("Ah you thought you could sneak in here didn't you, young blood? Better go get your mommy or daddy!")
else:
    if movie.lower() == "action":
        print("Welcome to the massacre. Do you want to watch another movie\n"
              "that has more action? 'Men in Black' seems to be a better choice\n"
              "as men with suits try to save the world from alien invasion.")
    elif movie.lower() == "adventure":
        print("Welcome to the massacre.  For more adventure movies, \n"
              "Guardians of the Galaxy' is a pretty good movie.  Lucky\n"
              "for you, it is now in the cinemas too!")
    elif movie.lower() == "comedy":
        print("Welcome to the massacre. You do know that this movie isn't\n"
              "that funny right?  'The Monkey King' would be a much funnier\n"
              "option.")
    elif movie.lower() == "drama":
        print("Welcome to the massacre.  By the way, 'Marry my Dead Body' is also \n"
              "in the cinema. Would you like to watch that instead?")
    elif movie.lower() == "fantasy":
        print("Welcome to the massacre. Heads up, this fantasy is pretty gruesome\n"
              "'Luca' seems to be a better option, a fantastical story of the journey\n"
              "between a sea monster and a human.  'Luca' is also playing, do you want\n"
              "to watch this instead?")
    elif movie.lower() == "romance":
        print("Welcome to the massacre.  But... are your sure your don't want something more \n"
              "romantic?  The movie 'Elemental' is also in the cinema this month. ")
    else:
        print("Welcome to the massacre. Try your best to survive.")

#tuple recommendation
movie1= ("Men in Black", "action")
if movie1[1] == "action":
    print("'Men in Black' seems to be a good action movie for you! ")
else:
    ("Enjoy your day!")
