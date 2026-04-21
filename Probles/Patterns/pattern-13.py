'''
   *
  * *
 * * *
* * * *

 * * *
  * *
   *
'''
n = 4

for i in range(n):
    #Spaces=n-i-1
    #stars = i+1
    print(' ' * (n - i - 1) + (i + 1) * " *")

for i in range(n-1):
    print(' ' * (i + 1) + " *" * (n - 1 - i))