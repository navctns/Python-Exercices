#keyword arguments
def print_num(a,b,c=23):
    print(a,b,c)
print_num(1,2)
print_num(1,2,5)
c=33
print_num(1,2,c)
#arbitrary arguments
def shopping(name,*products):#products is an arbitrary argument
    print("Hi",name,"\nThese are the products you have ordered:",products)

prod_1='soap','brush','knife'
prod_2='shampoo','shaving set'
#print(type(prod_1))
shopping('john',prod_1)
shopping("ravi",prod_2)
