'''
    D
   D C
  D C B
 D C B A
'''
n = 4 #i=0,1,2,3 #spaces=n-i-1
for i in range(n): #i=0,1,2,3
    print(' ' * (n - i -1), end='')
    for j in range(i+1):
        print(chr(64 + n -j), end=' ')
    print()
