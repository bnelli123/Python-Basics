import math

l =[2,4,9,16,25,34]
print(list(map(lambda x: math.sqrt(x), l)))
print(list(map(lambda x: math.factorial(x), l)))
print(dir(math))
print(help(math.sqrt))