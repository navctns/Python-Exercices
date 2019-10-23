set_1=set([1,3,5,7,9,"python","java",4,7,8,16])
set_2=set(['python','java','c#','c','swift'])
set_3=set([1,2,3,4,5,6,7,8,9,10,11,12,13])
set_4={2,4,6,8,10}

#print("set_1 union set_2:",set_1|set_2)
"""
print("set1:",set_1)
print("set2:",set_2)
print("set3:",set_3)
print("set4:",set_4)
"""
print("set1 union set2:",set_1|set_2)
"""
print("set1 union set2 union set3",set_1.union(set_2,set_3))
print("set1 intersection set2",set_1.intersection(set_2))
print("set2 intersection set3:",set_2.intersection(set_3))

print("set1 difference set2:",set_1 -set_2)
print("set1 symmetrical difference set2:",set_1 ^ set_2)
for i in set_1:
    if i==1:
        print(i)
        break
    print(i)
    
set_4.update(['software','architecture'])
set_2.add("cpp")
print("set2 after add:",set_2)
print("updating set:",set_4)

set_2.remove("java")
print("set2 after removing java",set_2)
set_2.discard("java")
print("set2 after discard java:",set_2)
"""