pineapplerice = True
coffeesnowbee = True
croissantleaf = True
pastaicecream = True

data = {"pineapplerice": "4543", "coffeesnowbee": "6433","croissantleaf": "942","pastaicecream": "5353"}


for i in range(3):
    try:
        if i == 2:
            u = input("Please input your username: ")
            p = input("Please input your password: ")

            if u and p == data[u]:
                print("access granted")
            else:
                print("access denied")
                break
        else:
            u = input("Please input your username: ")
            p = input("Please input your password: ")

            if u and p == data[u]:
                print("access granted")
                break
            else:
                print("access denied, try again")
    except:
        print("access denied, try again")

while True:
    if u == "pineapplerice" or u == "coffeesnowbee" or u == "croissantleaf":
        m = input("\nWhat information do you want to access?\n "
                  "(air_capabilities, naval_capabilities, special_units): ")
        if m == "air_capabilities":
            print("\nAircrafts available:\n"
                  "------------\n"
                  "F-16 Fighting Falcons: 20 \n"
                  "F-22 Raptor: 18\n"
                  "SR-71 Blackbird: 35\n"
                  "F-5N Tiger II: 23\n"
                  "F-15 Eagle: 34")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        elif m == "naval_capabilities":
            print("\nNaval Ships available:\n"
                  "------------\n"
                  "Battleship: 20 \n")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        elif m == "special_units":
            print("\nspecial")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        else:
            print("\ninput not found, please try again")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break
    elif u == "pastaicecream":
        m = input("\nWhat information do you want to access?\n "
                  "(air_capabilities, naval_capabilities, special_units, black_ops): ")
        if m == "air_capabilities":
            print("\nAircrafts available:\n"
                  "------------\n"
                  "F-16 Fighting Falcons: 20 \n"
                  "F-22 Raptor: 18\n"
                  "SR-71 Blackbird: 35\n"
                  "F-5N Tiger II: 23\n"
                  "F-15 Eagle: 34")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        elif m == "naval_capabilities":
            print("\nNaval Ships available:\n"
                  "------------\n"
                  "Battleship: 20 \n")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        elif m == "special_units":
            print("\nspecial")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        elif m == "black_ops":
            print("\nHigh level ;p")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break

        else:
            print("\ninput not found, please try again")

            c = input("\nDo you want to continue? ")
            if c == "yes":
                continue
            elif c == "no":
                break
    else:
        exit()
print("\nThank you for your service.")
