#42.	Write a program to check if a given string is a Palindrome.
#A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

str1=input("Enter a string:")
if str1==str1[::-1]:
    print(str1,"is a Palindrome")
else:
    print(str1,"is Not a Palindrome")
"""
OUTPUT:

Enter a string:malayalam
malayalam is a Palindrome

Enter a string:forest
forest is Not a Palindrome

Enter a string:level
level is a Palindrome
"""
