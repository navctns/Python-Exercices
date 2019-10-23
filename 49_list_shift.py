#49.	Write a program to shift every element of a list to circularly right. E.g.-
#INPUT : 1 2 3 4 5
#OUTPUT : 5 1 2 3 4
#Input a list
list_1=[]
l=int(input("Enter size of list:"))
print("Enter Elements in list")
for i in range(l):
    item=eval(input(":"))
    list_1.append(item)
print(list_1)
length=len(list_1)
#t=list[0]
#list_shift=[]
"""
for i in range(-length,1): 
   #t=list_1[i+1]
   list_1[i+1]=list_1[i]
 """
#this is the final code
# the end element is stored to a temporary variable
#list index is iterated through end -2 to -length-1
#then the end element is stored to -length index element(first element index=0)
t=list_1[-1]
for i in range(-2,-length-1,-1):
    list_1[i+1]=list_1[i]

list_1[-length]=t
print(list_1)
    
