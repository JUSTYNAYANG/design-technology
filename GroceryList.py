# GroceryList = ["tomato", "blueberry", "StrawberryMilk"]
#
# print(GroceryList[0])
# print(GroceryList[2])
# GroceryList.append("AppleJuice")
# print(GroceryList)
# GroceryList.remove("StrawberryMilk")
# print(GroceryList.pop(2) + " was removed.")
# for i in GroceryList:
#     print(i)

# g = ["Banana", "Cake", "Apple", "Milk", "Ice Cream", "Lettuce", "French Fries", "Carrot", "Fish"]
# print("Healthy Food\n ----------")
# print(g[0])
# print(g[2])
# print(g[3])
# print(g[5])
# print(g[7])
# print(g[8])
#
# print("\nUnhealthy Food\n ----------")
# print(g[1])
# print(g[4])
# print(g[6])
#
# b = []
# b.append(g.pop(1))
# b.append(g.pop(3))
# b.append(g.pop(4))
#
# g.append("Watermelon")
# g.append("Potato")
# g.append("Cabbage")
#
# print("\nModified Healthy Grocery List: \n---------------")
#
# for i in range(len(g)):
#     print(f"{str(i+1)}.   {g[i]}")
#
# print("\nBad Bad List: \n---------------")
#
# for i in range(len(b)):
#     print(f"{str(i+1)}.   {b[i]}")


g = ["Banana", "Apple", "Milk", "Lettuce", "Carrot", "Fish"]
c = ["Cake", "Ice Cream", "French Fries"]

print("The current healthy grocery list is:")
for i in range(len(g)):
    print(f"{str(i+1)}.   {g[i]}")

print("\nThe current unhealthy grocery list is:")
for i in range(len(c)):
    print(f"{str(i+1)}.   {c[i]}")

while True:
    a = input("\nWhat else should be added to the list? (if none, input 'exit') ")
    if a.lower() != "exit":
        b = input("Is this item healthy or unhealthy? ")
        if b.lower() == "healthy":
            g.append(a)
        else:
            c.append(a)

        print("The current healthy grocery list is:")
        for i in range(len(g)):
            print(f"{str(i + 1)}.   {g[i]}")

        print("\nThe current unhealthy grocery list is:")
        for i in range(len(c)):
            print(f"{str(i + 1)}.   {c[i]}")

    else:
        break

