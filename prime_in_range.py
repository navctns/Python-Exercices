#to check prime numbers in an interval
fr,to=eval(input("Enter the interval(from,to):"))

for i in range(fr,to):
    if i==2:
        print(i,end='\n')
    elif (i==0)|(i==1):
        #print(num, " is Not Prime")
        pass
    else:
        f=1
        for j in range(2,int(i/2)+1):
            if i%j==0:
                #print(num," is Not Prime")
                f=0
                break
        if f!=0:
            
            print(i , end="\n")
    

"""
OUTPUT:

Enter the interval(from,to):0,40
2
3
5
7
11
13
17
19
23
29
31
37

"""
   