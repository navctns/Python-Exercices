# -*- coding: utf-8 -*-
"""

@author: kalyani venugopal

"""
'''STRING OPERATION'''

#indexing and slicing

str = 'welcome to python'

print('str = ', str)

#first character
print('str[0] = ', str[0])

#indexerror
print('str[18] = ', str[18]) #string not contain 18 places

#type error
print('str[a] = ', str[a])
print('str[2.2] = ', str[2.2])

#7th character 
print('str[7]) = ',str[7])

#last character
print('str[-1] = ', str[-1])

#second last
print('str[-2] = ', str[-2])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

#Deleting or changing a string

string = 'hello' #we are trying to replace o with l
string[4] = 'l' #will get error
print(string)


string = 'Python' #this is how we can replace string completly
print(string)

del string[1] #you cannot delete the a character in string

del string
print(string) #but can delete entire string 


#concantation of strings

str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# iterating through strings

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


s = "hello world"
print(s.find("o"))   #will return the index of the word

#membership operation in strings

print('a' in 'program')

print('at' not in 'battle')

#enumeration and length

a = 1,2,3,4,5
list(a)

b = "a",'c','d','e'
list(b)

str = 'welcome to python'
enum = list(enumerate(str))   #enumerate the string
print(enum)

coun = str.count("e")
print(coun)

split = list(str.split())  #split the string
print(split)

#capitalize
print(str.capitalize())

print(str.upper())

print(len(str))  #length

#format() method to format strings

# default(implicit) order

default_order = "{}, {} and {}".format('John','Sean',"kalyani")
print(default_order)


# order using positional argument - positional order 

positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print(positional_order)

po = " i have three friends {1}, {0} and {2}".format('John','Bill','Sean')
print(po)

# order using keyword argument- keyword order

keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print(keyword_order)

#to print name likes color
a = input('enter a name: ')
b = input('enter color: ')
n = "{} likes {}".format(a,b)
print(n)
bin(7)

# formatting integers
"Binary representation of {0} is {0:b}".format(12)


"Binary representation of {2} is {2:b}".format(12,3,4,8)

"Hexadecimal representation of {0} is {0:x}".format(15)

# formatting floats
"Exponent representation of {0} is {0:e}".format(1566.345)

"Exponent representation of {0} and {1} is {0:e} and {1:e} respectively".format(1566.345,100)

# round off
"{0} rounded to 3 decimal place is {0:.3f}".format(1/3)

"pi rounded to 7 decimal place is {0:.7f}".format(22/7)

 # string alignment
 
 
 "{:<10}".format("left")
 "{:>10}".format("right")
 "{:^10}".format("centre")
 
 
 a = "{:<30}".format("hello")
print(a)
b ="{:>30}".format("hello")
print(b)
c = "{:^30}".format("hello")
print(c)
 

"|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')

#common python string method

"PYTHON PrOgRaMer".lower()
"python prOGramer".upper()

"This will split 10 words into a list".split()
"mango".split()
"m ango".split("n")


' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
"".join(['i','have',10,'rupees']) #will show error as int in str
"".join(['i ',' ','have ','10','rupees'])

'Happy New Year'.find('New')
'hello'.find('l')

'Happy New Year'.replace('Happy','Brilliant')


#########################################################################################

        


  

















