# try:
#     a, b = map(int, input().split())
#     c = 30 if a > b else 40
#     print(c)
# except ValueError:
#     print("Enter numbers only")

l = [1,2,3,3,4,5,6,5]
print(l.count(5))
print(type(l))
print(type(5))

if type(5) == int:
    print("int")