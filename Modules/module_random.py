import random
l1 = [i for i in range(1,11)]
l2 = [2,3,4,5,6]
print(random.randint(1,100))
print(random.random())
print(random.choice([i for i in range(1,100)]))
random.shuffle(l2)
print(l2)