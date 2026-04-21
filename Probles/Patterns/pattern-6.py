'''
A
B B
C C C
D D D D
'''
n = 4 #i=0,1,2,3
for i in range(n):
    print((str(chr(65 + i)) + " ") * int(i+1))