#33.	Calculate the sum of digits of a number input
print("---sum of digits of numbers---")
num=input("Enter the number:")
print(type(num))
#print("sum of digits :", [sum(int(s)) for s in num])
s=0
for i in num:
    s+=int(i)
print("sum of digits:",s)
