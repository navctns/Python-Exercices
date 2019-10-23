#43.	Write a program to check if the two strings entered by user are
#anagrams or not. Two words are said to be anagrams if the letters of one word
#can be rearranged to form the other word. For example, jaxa and ajax are
#anagrams of each other
str1=input("Enter word-1:")
str2=input("Enter word-2:")
if len(str1)==len(str2):
    set_1=set(str1)
    set_2=set(str2)
    if set_1==set_2:
        print("{} and {} are anagrams".format(str1,str2))
    else:
        print("{} and {} are NOT anagrams".format(str1,str2))
else:
    print("{} and {} are NOT anagrams".format(str1,str2))
"""
OUTPUT:

Enter word-1:ajax
Enter word-2:jaxa
ajax and jaxa are anagrams
>>> 
============ RESTART: D:/NOTES/Programs/43_str_words_anagrams.py ============
Enter word-1:morse
Enter word-2:mesore
morse and mesore are NOT anagrams
>>> 
============ RESTART: D:/NOTES/Programs/43_str_words_anagrams.py ============
Enter word-1:morse
Enter word-2:mesor
morse and mesor are anagrams
>>> 
============ RESTART: D:/NOTES/Programs/43_str_words_anagrams.py ============
Enter word-1:shoe
Enter word-2:show
shoe and show are NOT anagrams
"""
