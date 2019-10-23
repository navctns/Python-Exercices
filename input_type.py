#input item and return its type
inp=input("input any data of container data types:")

if ((inp[0]=="[") & (inp[-1]=="]")):
    print("it is a list")
elif (inp[0]=='(') &(inp[-1]==')'):
    print("it is a tuple")
elif (inp[0]=='{') &(inp[-1]=='}')&(":" in inp ):
    print("it is a dictionary")
elif (inp[0]=='{') &(inp[-1]=='}'):
    print("it is a set")
else:
    print("Invalid Entry")
    
    
"""
OUTPUT:

input any data of container data types:[1,2,3]
it is a list

input any data of container data types:(1,1)
it is a tuple

input any data of container data types:{2,3}
it is a set

input any data of container data types:{1:2,2:3}
it is a dictionary

"""
user _ 1,2,3,4
[1,2,3,4]
