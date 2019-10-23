#47.	Using range (1,51), make two list, one containing all even numbers and
#other containing all odd numbers.

#list_even=[i for i in range(1,51) if i%2==0]
#print(list_even)
#a,b=[lambda i,j: for i,j in range(1,51) if i%2==0 elif i%2==1]
list_odd=[]
list_even=[]
for i in range(1,51):
    if i%2==0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_even)
print(list_odd)

"""
OUTPUT:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
"""
