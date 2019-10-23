#41.	Write a program that takes your full name as input and displays the
#abbreviations of the first and middle names except the last name which is
#displayed as it is. For example, if your name is Robert Brett Roser, then
#the output should be R.B.Roser.

name=input("Enter your full name:")
split=name.split()
#print(split)
for i in range(len(split)-1):
    print(split[i][0].upper(),end=".")
print(split[-1].capitalize())

"""
OUTPUT:
Enter your full name:Guido van Rossum
G.V.Rossum
"""
