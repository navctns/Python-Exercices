#fibonacci

i=0
j=1
ch=int(input("Length of fibonacci series:"))
for k in range(0,ch):
    print(i)
    #print(j)
    i,j=j,i+j
    #j=i+j
    #print(i,i+j)
    
"""
OUTPUT:

Length of fibonacci series:8
0
1
1
2
3
5
8
13

"""