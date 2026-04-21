l = [1,2,4,5,7,8]

def sqr(n):
    return n * n

print(list(map(sqr,l)))

#%%
print(list(map(lambda n:n*n, l)))


#%%
l1 = [1,2,3,4]
l2 = [5,6,7,8]

product = list(map(lambda x,y: x*y, l1, l2))
print(product)