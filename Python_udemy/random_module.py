from random import *
for i in range(10):
    print(random())


#uniform

for i in range(10):
    print(uniform(2, 10))


#randint
for i in range(10):
    print(randint(1,10)) #inclusive 1, 10

#rand-range
for i in range(10): 
    print(randrange(1,20,2))

for i in range(10):
    print(randrange(10)) #Prints random value from 0-9

#choice() --> Generate a random object from a sequence
fruits = ["Apple", "Mango", "Orange", "Banana", "Watermelon"]
for i in range(len(fruits)):
    print(choice(fruits))


#String is also sequence like list
A="Bala"
print(list(A))
