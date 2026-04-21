'''
A
A B
A B C
A B C D
A B C
A B
A
'''
n=4
for i in range(n): #i=0,1,2,3
    for j in range(i+1): #j=0, j=0,1
        print(chr(65+j), end=' ')
    print()
for k in range(n-1):  #k=0,1,2
    for l in range(n-k-1): #l=0,1,2; l=0,1, l=0
        print(chr(65 + l), end=' ')
    print()