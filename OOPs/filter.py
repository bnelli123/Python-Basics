l = [0,1,2,3,4,5,6,7,8,9,10]
l1 = []
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

for i in l:
    if isEven(i) == True:
        l1.append(i)

print(l1)

#%%
l1 = [i for i in range(1,11)]
l2 = [i for i in range(11,21)]

print(list(filter(lambda x: x%2 == 0, l1)))
words = ["apple", "bat", "car", "elephant"]
print(list(filter(lambda s: len(s) > 4, words)))


