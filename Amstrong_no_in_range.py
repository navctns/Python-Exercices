#armstrong number in interval
print("Armstrong number in  an interval")
l,u=eval(input("Enter the interval(from,to):"))

#len_num=len(num)
#num=int(num)
for i in range(l,u+1):
    num=str(i)
    len_num=len(num)
    
    ch=0
    for i in range(len_num):
    
        ch+=int(num[i])**3
    if ch==int(num):
        print(num)

"""
OUTPUT:

Armstrong number in  an interval

Enter the interval(from,to):0,450
0
1
153
370
371
407

"""