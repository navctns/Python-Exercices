#40.	Write a program to find the first and the last occurrence of the letter
#'o' and character ',' in "Hello, World".

str1="Hello, World"
print(str1)
ino_f=str1.find('o')
inc_f=str1.find(',')
ino_last=None
inc_last=None
#str[::-1] is to reverse the string
if str1.count('o')>1:
    ino_last=len(str1)-str1[::-1].find('o')
if str1.count(",")>1:
    inc_last=len(str1)-str1[::-1].find(',')    
print("first occurance of 'o':{}\nLast occurance:{}\nfirst occurance of ',':{}\n Last occurance:{}".format(ino_f,ino_last,inc_f,inc_last))

"""
OUTPUT:

Hello, World
first occurance of 'o':4
Last occurance:9
first occurance of ',':5
 Last occurance:None
"""

      
