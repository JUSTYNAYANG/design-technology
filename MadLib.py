from colorama import Fore, Style


a = Fore.CYAN + input("Please type in a noun(living thing): ")
b = Fore.CYAN + input("Please type in a adjective: ")
c = Fore.CYAN + input("Please type in a noun: ")
d = Fore.CYAN + input("Please type in a superlative: ")
e = Fore.CYAN + input("Please type in a adjective: ")
f = Fore.CYAN + input("Please type in a adjective: ")
g = Fore.CYAN + input("Please type in a verb(-ing): ")
h = Fore.CYAN + input("Please type in a verb (past tense): ")
i = Fore.CYAN + input("Please type in a noun: ")
j = Fore.CYAN + input("Please type in a verb (past tense): ")
k = Fore.CYAN + input("Please type in a adjective: ")
l = Fore.CYAN + input("Please type in a verb(-ing): ")
m = Fore.CYAN + input("Please type in a adjective: ")
n = Fore.CYAN + input("Please type in a adjective: ")


aa = Style.RESET_ALL + "Once upon a time, in a land far away, there lived a "
bb = Style.RESET_ALL + ".  The land was "
bc = Style.RESET_ALL + " and there was \nno "
cc = (Style.RESET_ALL + ". Oh!  Good heavens! What should we do?  Of course, the kingdom did not know what \n"
      "they were missing.  It was until one day, when the ")
dd = Style.RESET_ALL + " traveler in the world stumbled upon\n the land did the people become aware of the "
de = Style.RESET_ALL + " goods they were missing.  So everyone "
ee = Style.RESET_ALL + " to\n plead the traveler to bring back more of these "
ff = Style.RESET_ALL + "treasures. The traveler listened and he\n"
fg = Style.RESET_ALL + (" his way back home to gather more items to go back. Unfortunately, when he got back "
                        "he \n found that a ")
gg = Style.RESET_ALL + " had "
hh = Style.RESET_ALL + " his house.  Everything was destroyed! So the "
ii = Style.RESET_ALL + " traveler had to return\n "
ij = Style.RESET_ALL + " empty handed. The "
ijj = Style.RESET_ALL + (" people of the kingdom still smiled despite hearing the news. They said\n "
                         "to the sorry traveler: 'All is well.  We might no longer have access to these ")
jj = Style.RESET_ALL + " goods, but life \nwill still go on"

# print(f"Once upon a time, in a land far away, there lived a {a}.  The land was {b} and there was \n"
#       f"no {c}. Oh!  Good heavens! What should we do?  Of course, the kingdom did not know what \n"
#       f"they were missing.  It was until one day, when the {d} traveler in the world stumbled upon\n"
#       f"the land did the people become aware of the {e} goods they were missing.  So everyone {f} to\n"
#       f"plead the traveler to bring back more of these {g} treasures. The traveler listened and he\n"
#       f"{h} his way back home to gather more items to go back.  Unfortunately, when he got back he \n"
#       f"found that a {i} had {j} his house.  Everything was destroyed! So the {k} traveler had to return\n"
#       f"{l} empty handed. The {m} people of the kingdom still smiled despite hearing the news. They said\n"
#       f"to the sorry traveler: 'All is well.  We might no longer have access to these {n} goods, but life\n"
#       f"will still go on'")

print(f"{aa}{a}{bb}{b}{bc}{c}{cc}{d}{dd}{e}{de}{f}{ee}{g}{ff}{h}{fg}{i}{gg}{j}{hh}{k}{ii}{l}{ij}{m}{ijj}{n}{jj}")