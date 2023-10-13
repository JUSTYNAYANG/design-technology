band = ["Tomorrow x Together", "Seventeen", "BTS"]

def printband(bd):
    print("-.-.-.-.-.-.-.-.-.-.-.-.\n"
          "School of Bands:\n"
          "-----")
    for i in bd:
        print(i)
    print("-.-.-.-.-.-.-.-.-.-.-.-.")

while True:
    print("______________________________________________________________\n"
          "1- enter a new band \n"
          "2- print out list of favorite bands\n"
          "3- search if a band is already on the list\n"
          "4- delete a band from the list\n"
          "5 - exit\n")
    r = input("What do you want to do? ")
    if r == "1":
        a = input("What band do you want to add to the list? ")
        if a in band:
            print("This band is already included.")
        else:
            band.append(a)
            print(f"{a} is added to the list.")
    elif r == "2":
            printband(band)
    elif r == "3":
        a = input("What band are you looking for? ")
        if a in band:
            print("Yes, this band is on the list")
        else:
            band.append(a)
            print("No, this band is not yet in the list")
    elif r == "4":
        a = input("What band do you want to remove? ")
        if a in band:
            band.remove(a)
            print(f"{a} is removed from the list.")
        else:
            print("This band is not on the list.")
    elif r == "5":
        print("Until the next time.\n"
              "______________________________________________________________")
        break