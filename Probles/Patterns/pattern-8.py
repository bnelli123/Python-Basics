'''
1 2 3 4
1 2 3
1 2
1
'''
n = 4 #i=0,1,2,3

for i in range(n): #i=0,1,2,3
    for j in range(n-i): #i=0 => j=0,1,2,3, i=1, j=0,1,2
        print(j+1, end=" ")

    print()