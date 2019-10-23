#48.	From a list containing ints, strings and floats, make three lists to
#store them separately
list_mix=[1,4,6,8,'woods','forest','sea','river',3.45,5.67,6.666,7.0]
list_int=[]
list_str=[]
list_float=[]
for i in list_mix:
    if (type(i)== int):
        list_int.append(i)
    elif (type(i)== float):
        list_float.append(i)
    elif (type(i)== str):
        list_str.append(i)

print(list_mix,"\n",list_int,"\n",list_str,"\n",list_float)

"""
OUTPUT:
[1, 4, 6, 8, 'woods', 'forest', 'sea', 'river', 3.45, 5.67, 6.666, 7.0] 
 [1, 4, 6, 8] 
 ['woods', 'forest', 'sea', 'river'] 
 [3.45, 5.67, 6.666, 7.0]
"""
