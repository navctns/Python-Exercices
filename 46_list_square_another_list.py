#46.	You are given with a list of integer elements. Make a new list which
#will store square of elements of previous list.
list_1=[]
m=int(input("give the size of the list to have:"))
print("Give numbers to add to list")
for i in range(m):
    n=eval(input(":"))
    list_1.append(n)   
    #if str(n)=='':
     #     break

list_2=[x**2 for x in list_1]
print(list_1)
print(list_2)

"""
OUTPUT:

give the size of the list to have:5
Give numbers to add to list
:1
:2
:3
:4
:5
[1, 2, 3, 4, 5]
[1, 4, 9, 16, 25]
"""
