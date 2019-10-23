#dictionaries
dict_1={"water":"rain","sky":"cloud","road":"car","shop":"gloceries"}
#retrieving values from dictionary
print("value in the key -sky dict_1['sky']:",dict_1["sky"])
print("value in the key water: dict_1.get('water'):",dict_1.get('water'))
#add value key pairs
dict_1[2]=4
print(dict_1)
#update list
dict_1[2]="changed"
print("dict_1[2]='changed':",dict_1)
print("dict before pop:",dict_1)
dict_1.pop('water')
print("pop item-dict_1.pop('water'):",dict_1)
print("dict before dict_1.popitem():",dict_1)
dict_1.popitem()
print("afterwards:",dict_1)
print("dict_1.values():",dict_1.values())
print("dict_1.keys():",dict_1.keys())
print("length of dictionary- len(dict_1):",len(dict_1))

a=['forest','urban','rural','islands']
b=['oxygen','rush','irony','different']

nature_dict={a[i]:b[i] for i in range(len(b)) }
print(nature_dict)
print('forest' in nature_dict)
print("sorted natural dict:",sorted(nature_dict))
print("unsorted:",nature_dict)#shows keys sorted
print(sorted(nature_dict.values()))#values are sorted
dict_1.clear()
print(dict_1)#clear all data
del dict_1#delete dict
print(dict_1)
