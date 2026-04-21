#%%
with open('text.txt', 'r+') as f:
    for line in f:
        print(line.strip())

#%%
count_1 = 0
with open('text.txt', 'r') as f:
    for line in f:
        words = line.strip().split()
        print(words)
        for word in words:
            if word == "Yendada":
                count_1 = count_1 + 1
print(count_1)
#%%
l1 = [1,2,1,2,3,4,1,2,1]
print(l1.count(1))