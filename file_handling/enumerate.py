l1 = [12, 10, 14, 15]
for i, num in enumerate(l1):
    print(str(i) +" ----> "+ str(num))

fruits = ["apple", "banana", "cherry"]

fruits[0] = "grapes"
print(fruits)

print(list(zip(l1, fruits)))
del l1[0]
print(l1)

string = "Hello World, I am Muthu "
string = string.split()
print(string)

a = [4,5,6]
a.append(7)
print(a) # [4,5,6,7]

b = [4,5,6]
b.extend([7,8])
print(b)