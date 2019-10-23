#Armstrong number
print("--Check for armstrong number--")
num=input("Enter number to check:")
len_num=len(num)
#num=int(num)
ch=0
for i in range(len_num):
    
    ch+=int(num[i])**3
if ch==int(num):
    print(num," is an Amstrong number")
else:
    print(num, "is not an amstrong number")
    
"""
OUTPUT:

Enter number to check:12
12 is not an amstrong number

Enter number to check:370
370  is an Amstrong number

Enter number to check:153
153  is an Amstrong number

Enter number to check:407
407  is an Amstrong number

Enter number to check:0
0  is an Amstrong number

Enter number to check:1
1  is an Amstrong number

Enter number to check:65
65 is not an amstrong number

"""