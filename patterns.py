# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in arr:
#     for num in row:
#         print(num, end=" ")
#     print("")

while True:
    try:
        user = int(input(f"What size would you like? "))
        pattern = input(f"What pattern would you like? (A~F) ").capitalize()

        #Pattern A: all 1s
        if pattern == "A":
            for i in range(user):
                for j in range(user):
                    print(1, end=" ")
                print("")

            print("")

        #Pattern B: all 0s
        elif pattern == "B":
            for i in range(user):
                for j in range(user):
                    print(0, end=" ")
                print("")

            print("")

        #Pattern C: outside 1s
        elif pattern == "C":
            for i in range(user):
                if i == 0 or i == user-1:
                    for j in range(user):
                        print(1, end=" ")
                    print("")
                else:
                    for j in range(user):
                        if j == 0 or j == user-1:
                            print(1, end=" ")
                        else:
                            print(0, end=" ")
                    print("")

            print("")

        #Pattern D: outside 0s
        elif pattern == "D":
            for i in range(user):
                if i == 0 or i == user-1:
                    for j in range(user):
                        print(0, end=" ")
                    print("")
                else:
                    for j in range(user):
                        if j == 0 or j == user-1:
                            print(0, end=" ")
                        else:
                            print(1, end=" ")
                    print("")

            print("")

        #Pattern E: all 1s
        elif pattern == "E":
            if user % 2 == 1:
                for i in range(user):
                    if i == int(user/2-0.5):
                        for j in range(user):
                            print(1, end=" ")
                        print("")
                    else:
                        for j in range(user):
                            if j == int(user/2-0.5):
                                print(1, end=" ")
                            else:
                                print(0, end=" ")
                        print("")

            print("")

        #Pattern F: Diagonals
        elif pattern == "F":
            for i in range(user):
                if i%2 == 0:
                    for j in range(user):
                        if j%2 == 0:
                            print(1, end=" ")
                        else:
                            print(0, end=" ")
                    print("")
                else:
                    for j in range(user):
                        if j % 2 == 0:
                            print(0, end=" ")
                        else:
                            print(1, end=" ")
                    print("")

            print("")
    except:
        break