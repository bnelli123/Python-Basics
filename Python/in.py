l1 = [2,3,4,5,2,3,4,5]

#Remove Duplicates
l2 = []
for num in l1:
    if num not in l2:
        l2.append(num)

print(l2)