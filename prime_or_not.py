#to check prime numbers
num=int(input("Enter number:"))
if num==2:
    print(num, " is Prime")
elif num==0:
    print(num, " is Not Prime")
else:
    f=1
    for i in range(2,int(num/2)+1):
        if num%i==0:
            print(num," is Not Prime")
            f=0
            break
    if f!=0:
        print(num ," is Prime")
   
"""
output:

Enter number:0
0  is Not Prime

Enter number:2
2  is Prime

Enter number:3
3  is Prime

Enter number:4
4  is Not Prime

Enter number:5
5  is Prime

Enter number:7
7  is Prime

Enter number:8
8  is Not Prime

Enter number:10
10  is Not Prime

Enter number:13
13  is Prime

Enter number:17
17  is Prime

"""
