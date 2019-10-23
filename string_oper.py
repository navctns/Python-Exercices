"""String operations"""

str_1='welcome to python'
print("str_1=",str_1)
print(str_1[0])
print(str_1[7])
#print(str_1[17]) #shows index out of range
#print('str[a]=',str_1[a])
print("str_1[-1]:",str_1[-1])
print("str_1[-2]:",str_1[-2])#reverse indexing

#slicing
print("str_1[8:]",str_1[8:])
print("str_1[0:7]:",str_1[0:7])

str_2='programming'
#del str_2[3]#TypeError: 'str' object doesn't support item deletion
del str_2#works
#print(str_2)#NameError: name 'str_2' is not defined

#concatenation of strings

str_1='hello'
str_2='java'

#using +
print("str_1+str_2:",str_1+str_2)

#using *
print("str_2 *5:",str_2*5)

#iterating through strings and finding count of a character
count=0
for letter in 'hello world':
    if(letter =='l'):
        count+=1
print(count,"letters found")  

#str.find()
s='hello world'
print(s.find('o'))#will return the index of the char, for the first instance onle
print(s.find('world'))#return the index of word(where it starts)

#eunumeraton and length
a=1,2,3,4,5,6
print("list(a):",list(a))
b='a','b','c','d','e'
print("list(b):",list(b))

str1='welcome to python programming'
str1_enum=list(enumerate(str1))
print("enumerate(str1):",str1_enum)

print("str1.count('e'):",str1.count('e'))
print("str1.count('m'):",str1.count("m"))

#split the string
split=str1.split()
print(split)
split_to=str1.split("to")#split with 'to' instead of ' '(space)
print(split_to)

#capitalize
print(str1.capitalize())#capitalize the first char      
print(str1.upper())#capitalize the entire string
print(str1.lower())#change to lower case
print("len(str1):",len(str1))

#format() method to format strings

#default (implicit) order
default_order="{},{},and {}".format('john','bill','sean')#according to sequential order 
print(default_order)

#ordering using positional order

positional_order="{0},{2}, and {1}".format("john",'bill','sean')#as order specified in curly braces
print(positional_order)

#order using keyword argument
keyword_order="{s},{j}, and {b}".format(s='sean',b='bill',j='john')
print(keyword_order)

#formatting integers
print("Binary representation of {0} is {0:b}".format(12))#binary representation
print("hexa-decimal representaton of {0} is :{0:x}".format(16))#hexa decimal

#join stings
print(''.join(['This','will','join','all','words','into','a','string']))#all should be string
#replace
print("happy new year".replace("happy","brilliant"))#replace 'happy' with 'brilliant'




