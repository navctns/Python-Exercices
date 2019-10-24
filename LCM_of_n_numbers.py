def lcm(*a):
    """
    input: sequence of numbers
    output: lcm
    logic:
    input is converted to a list
    all multiplicants of all numbers are stored to a list by cheking
    num%i==0
    then found the common multiplicants by comparing its count with the
    length of input(since it should be common to every input)
    then took the minimum from it
    """
    list1=list(a)
    len_in=len(list1)#length of input
    list_all=[]#all multiplicants
    list_fin=[]#common multiplicants
    #set1=set()#not used here
    #set2=set()#not used here
    for i in list1:
        for j in range(2,i//2+1):
            if i%j==0:
                list_all.append(j)
    print("listall:",list_all)#for debugging
    
    for i in list_all:
        if list_all.count(i)==len_in:
            list_fin.append(i)
    #print(list_fin)#for debugging
    #print("len_in:",len_in)#debugging
    if len(list_fin)==0:
        print("No lcm")
        return None
    else:
        return min(list_fin)
print(lcm(9,27,36,45))
