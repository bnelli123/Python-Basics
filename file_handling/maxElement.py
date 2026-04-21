l1 = [10, 12, 99, 500, 23, 233]
# l1.sort()
# print(l1)
# print(l1[-1])

# l1 = sorted(l1)
# print(l1)

max_val = l1[0]

for element in l1:
    if element > max_val:
        max_val = element

print(max_val)

min_val = l1[0]

for i in l1:
    if i < min_val:
        min_val = i

print(min_val)

#sum

total = 0

for i in l1:
    total = total + i
print(total)

#avg
avg = total/len(l1)
print(avg)

