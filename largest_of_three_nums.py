#largest of 3 numbers
a,b,c=eval(input("Enter three numbers,(separate by commas :"))
#on multiple assignments always use eval()
print("a=",a,"\nb=",b,"\nc=",c)
if a>b:
    if b>c:
        print(a," is the largest number")
elif c>b:
    print(c," is the largest number")
else:
    print(b,"is the largest number")
    

"""
Output:

Enter three numbers,(separate by commas :5,3,1
5  is the largest number

Enter three numbers,(separate by commas :3,5,1
5 is the largest number

Enter three numbers,(separate by commas :1,3,5
5  is the largest number

Enter three numbers,(separate by commas :18,26,30
30  is the largest number

Enter three numbers,(separate by commas :18,26,30
a= 18 
b= 26 
c= 30
30  is the largest number

Enter three numbers,(separate by commas :30,26,18
a= 30 
b= 26 
c= 18
30  is the largest number

Enter three numbers,(separate by commas :18,30,26
a= 18 
b= 30 
c= 26
30 is the largest number

"""