#default argument, msg,msg2 are default arguments
def greet(name,msg="Welcome to python programming",msg2="it's nice"):
    print("Hi",name,msg,msg2)
greet('Sanju')
greet('john')
greet("Hari","Welcome to java programming")#second one is positional argument
#positional arguments have higher preference than default arguments
c="Welcome to C programming"
greet("Bennet",c)

