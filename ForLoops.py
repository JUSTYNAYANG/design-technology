#Challenge 1
def countdown(num):
    for i in range(num, 0, -1):
        print(i)

countdown(10)

print("\n")
def countup(num):
    for i in range(0, num):
        print(i)
countup(10)

#Challenge 2

def cuo(num): #countupodd
    for i in range(1, num, 2):
            print(i)
def cdo(num): #countdownodd
    if num%2 == 1:
        pass
    else:
        num-= 1
    for i in range(num, 1, -2):
            print(i)
def cue(num): #countupeven
    for i in range(0, num, 2):
            print(i)
def cde(num): #countdowneven
    if num%2 == 1:
        num-=1
    else:
        pass
    for i in range(num, 0, -2):
            print(i)

cuo(16)
print("\n")
cdo(16)
print("\n")
cue(15)
print("\n")
cde(15)

Challenge 3
def countupPrime(num):
    for j in range(2, num):
        n = 0
        for i in range(2, j):
            if j % i == 0:
                n = 1
        if n == 0:
            print(j)

def countdownPrime(num):
    for j in range(num, 1, -1):
        prime = True
        for i in range(2, j):
            if j % i == 0:
                prime = False
        if prime:
            print(j)

countdownPrime(100)

