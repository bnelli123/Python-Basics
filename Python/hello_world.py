# print("Hello World")
s="Hello World"
# print(len(s))
print(s[::3])

a=10
b=3

print(a,b)
a, b = b, a

print(a,b)

a = [1,2,3,4,5]
a[2]=6
print(type(a))

# b = (1,2,3,4,5)
# b[2]=11
# print(b)

print(len("1"))

my_list = [10, 20, 30, 40, 50, 60]
print(my_list[1:4])
#[20, 30, 40]
print(my_list[:3])
#[10,20,30]
print(my_list[2:])
#[30, 40, 50, 60]
print(my_list[::2])
#[10, 30, 50]


# Positive:   0   1   2   3   4   5
#             10  20  30  40  50  60

# Negative:  -6  -5  -4  -3  -2  -1

#List comprehension
#[expression for item in iterable]
numbers = [1, 2, 3, 4]
squares = []

for x in numbers:
    squares.append(x*x)
print(squares)

squares2 = [x*x for x in numbers]
print(squares2)

numbers = [1, 2, 3, 4, 5, 6]
sqaures3 = [x-1 for x in numbers if x % 2 == 0]
print(sqaures3)

result = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(result)

word = "hello"
letters = [ch.upper() for ch in word]
print(letters)

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for num in matrix]
print(flat)
flat2 = [num for num in matrix]

nums = [1, 2, 3]

result = [(x, y) for x in nums for y in nums if x != y]
print(result)