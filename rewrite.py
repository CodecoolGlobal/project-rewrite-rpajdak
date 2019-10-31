x = input("Number 1 ")
y = input("Number 1 ")
def min(x,y):
    less = 0
    numbers = [x,y]
    for num in numbers:
        if x > y:
            less = y
        else:
            less = x
    print(less)
min(x,y)

x = input("Number 1 ")
y = input("Number 1 ")

def max(x,y):
    greater = 0
    numbers = [x,y]
    for num in numbers:
        if x > y:
            greater = x
        else:
            greater = y
    print(greater)
max(x,y)

iterable = input(("Podaj stringa: "))
def len(iterable):
    lenght = 0
    for sign in iterable:
        lenght +=1
    print(lenght)

len(iterable)

x = input("Number #1: ")
y = input("Number #2: ")   

def multiply(x,y):
    suma = 0
    counter = 1
    while counter <= y:
        suma += x
        counter +=1
    print(suma) 
    return suma

multiply(20,4)

def power(x,y):
    suma = x
    counter = 1
    if (y == 0):
        suma = 1
        print(suma)
        return suma
    else:
        while counter <= y:
            suma = suma * x
            counter +=1
    
    print(suma)    
    return suma

power(2,10)

def wynik(x,y):
    a = x // y
    print("wbudowana fukcja: ",a)

wynik(-1, -2)


def costam(x,y):
    counter = 1
    number = x-y
    if x == y:
        counter = 1
        print(counter)
    elif x < y:
        counter = 0
        print("linia 84 ", counter)
    else :
        while number >= y:
            number = number-y
            counter += 1 
            print("tu jest blad")
    print("linia 90 ", counter)

costam(-2,-6)
