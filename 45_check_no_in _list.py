#45.	Take 10 integer inputs from user and store them in a list.
#Again, ask user to give a number. Now, tell user whether that number is present
#in list or not.

list_1=[]
print("Enter ten integers:")
for i in range(10):
    num=int(input(":"))
    list_1.append(num)

#print(list_1)
#print(type(list_1))

while True:
    n=int(input("Give a number:"))
    if n in list_1:
        print(n," is in the list")
    else:
        print(n," is not in the list")
    ch=int(input("Do you want to check for another number:\n1.Yes\n2.No"))
    if ch==1:
        pass
    elif ch==2:
        break

"""
OUTPUT:

Enter ten integers:
:4
:45
:78
:55
:66
:77
:88
:99
:100
:125
Give a number:78
78  is in the list
Do you want to check for another number:
1.Yes
2.No1
Give a number:2
2  is not in the list
Do you want to check for another number:
1.Yes
2.No
"""
        
