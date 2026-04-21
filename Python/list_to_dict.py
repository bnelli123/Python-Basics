#%%
l1 = ['A', 'BALA', 2, 43, 'DUCK']
pri_data = dict(enumerate(l1, 1))
print(pri_data)

#%%
initial_data = {1: 'A', 2: 'BALA', 3: 2, 4: 43, 5: 'DUCK'}
print(type(initial_data))
initial_data.pop(1)
print(dict)

del initial_data[2]
print(initial_data)

initial_data['friend'] = "Gova"
print(initial_data)

#%%
l1 = [1,2,3,4]
l2 = ['A', 'B', 'C', 'D']
data = dict(zip(l1, l2))
print(data)

#%%
l1 = [1,2,3,4]
l2 = ['A', 'B', 'C', 'D']
data = dict(zip(l1, l2))

for item in data.values():
    print(item)