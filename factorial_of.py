#FACTORIAL OF A NUMBER
num=int(input("Enter number:"))
fact=1
if (num==0)|(num==1):
    print ("Factorial: 1")
else:
    
    for i in range(num,0,-1):
        fact=fact*i
    print("Factorial:",fact)

"""
OUTPUT:

Enter number:0
Factorial: 1

Enter number:1
Factorial: 1

Enter number:5
Factorial: 120

Enter number:10
Factorial: 3628800

"""