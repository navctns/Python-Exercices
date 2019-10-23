#19. Program to Check if a Number is Positive, Negative or 0

num=float(input("Enter the number:"))
if num<0:
    print("Number is Negative")
elif num>0:
    print("Number is Positive")
else:
    print("Number is Zero")
    
    
"""
output:

Enter the number:-5.3
Number is Negative

Enter the number:-3
Number is Negative

Enter the number:0.5
Number is Positive

Enter the number:1
Number is Positive

Enter the number:0.0
Number is Zero


"""