'''
*
* *
* * *
* * * *
* * *
* *
*
'''
n=4
for i in range(n):
    print(" *" * (i+1) + ' ' * (n - i -1))
for i in range(n-1):
    print(" *" * (n - 1 -i) + ' ' * (i+1))
