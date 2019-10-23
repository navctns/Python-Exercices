import math
print("----Solving quadratic equations-----")
a,b,c=eval(input("Enter a,b,c in order(separate by commas:"))
sol1,sol2=(-b+math.sqrt(b*b-4*a*c))/2*a,(-b-math.sqrt(b*b-4*a*c))/2*a
print("solutions:",sol1,"\n",sol2)
