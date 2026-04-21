'''
A B C D
 A B C
  A B
   A
'''
n=4

for i in range(n):
    print(' ' * i, end='')
    for j in range(n-i):
        print(chr(65+j), end=' ')
    print()