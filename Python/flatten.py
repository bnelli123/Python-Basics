matrix = [[1, 2], [3, 4], [5, 6]]
flattened = []
for row in matrix:
    for item in row:
        flattened.append(item)
        print(flattened)

print(flattened)