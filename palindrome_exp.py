str1=input("Enter a string:")
s=0
if ',' in str1:
    split=str1.split(',')
    s=1
elif '.' in str1:
    split=str1.split('.')
    s=2
else:
    split=str1.split()
    s=3
#str2=''
if s!=0:
    clear(str1)
    for i in split:
        str1+=i
    



if str1==str1[::-1]:
    print(str1,"is a Palindrome")
else:
    print(str1,"is Not a Palindrome")
