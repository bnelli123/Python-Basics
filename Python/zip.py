a = (1,2,3)
b = ("x","y","z")
print(zip(a,b))

matrix=[(1, 'x'), (2, 'y'), (3, 'z')]
print(list(zip(*matrix)))

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

a, b = zip(*pairs)
print(list(a))

# 👉 zip() returns an iterator
# 👉 Iterators are consumed once