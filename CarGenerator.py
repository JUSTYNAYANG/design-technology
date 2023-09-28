from random import randint
from array import array

carBrand = ["Porsche", "BMW", "Toyota", "Mercedes Benz", "Volkswagen", "Ford"]

randomCars = []
for i in range(100):
    a = randint(0, 5)
    randomCars.append(carBrand[a])

#print all cars
def printAll():
    for i in randomCars:
        print(i)

#count number of cars for brand
def numOfBrand(brandname, clist):
    return clist.count(brandname)

# list.sort()
def PopularBrand():
    cars = []
    for i in range(6):
        cars.append([(numOfBrand(carBrand[i], randomCars)), carBrand[i]])
    cars.sort()
    print(cars)
    return cars[5][1]

def leastPopularBrand():
    cars = []
    for i in range(6):
        cars.append([(numOfBrand(carBrand[i], randomCars)), carBrand[i]])
    cars.sort()
    return cars[0][1]

printAll()
print("\n")
print(PopularBrand())
print("\n")
print(leastPopularBrand())
print()


def numCarsDifference(b1, b2):
    if numOfBrand(b1, randomCars) >= numOfBrand(b2, randomCars):
        a = int(numOfBrand(b1, randomCars)) - int(numOfBrand(b2, randomCars))
        b = f"There are {a} more {b1} than {b2}."
    else:
        a = int(numOfBrand(b2, randomCars)) - int(numOfBrand(b1, randomCars))
        b = f"There are {a} more {b2} than {b1}."
    return b


print(numCarsDifference("Toyota", "Mercedes Benz"))

print(numCarsDifference("Volkswagen", "Porsche"))






