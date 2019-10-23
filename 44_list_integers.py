#44.	Take 10 integer inputs from user and store them in a list and print
#them on screen.
list_1=[]
print("Enter ten integers:")
for i in range(10):
    num=int(input(":"))
    list_1.append(num)

print(list_1)
print(type(list_1))

"""
Enter ten integers:
:25
:12
:4
:56
:78
:48
:55
:22
:55
:88
[25, 12, 4, 56, 78, 48, 55, 22, 55, 88]
"""
