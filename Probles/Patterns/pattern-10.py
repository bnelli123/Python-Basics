'''
    D
   C C
  B B B
 A A A A
'''
n=4 #i=0,1,2,3
for i in range(1, n+1):
    print(' ' * (n-i) + str(chr(65+n-i)) * i )