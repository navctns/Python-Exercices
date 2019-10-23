#32.	Program to print average values of n numbers
n=int(input("Enter the range:"))
print("Enter the numbers")
s=0
for i in range(n):
   s+=int(input(":"))
print("Average:",s/n)
#print("avg=",(n+1)/2)
#n*(n+1)/2*n
