wanted_list = []
yn = 1

def outlawlist():
    for i in wanted_list:
        print(f"\n{i[0]} {i[1]} or better known as '{i[2]}' is wanted for \n"
              f"{i[3]}. \n{i[4][0]}"
              f" has been sentenced by the order of law to be\n"
              f"{i[5]}\nThe prize for {i[4][1]} arrest is {i[6]}.")

while yn == 1:
    b = []
    b.append(input("\nPlease input the first name of the outlaw: "))
    b.append(input("\nPlease input the last name of the outlaw: "))
    b.append(input("\nPlease input the alias of the outlaw: "))
    b.append(input("\nPlease input the crime of the outlaw: "))
    b.append(input("\nPlease input the pronoun of the outlaw (eg.She/her): ").split("/"))
    b.append(input("\nPlease input their sentence: "))
    b.append(input("\nPlease input their bounty: "))

    wanted_list.append(b)
    yn = int(input("\nDo you want to add another outlaw to the list? (1: yes, 2: no) "))


outlawlist()