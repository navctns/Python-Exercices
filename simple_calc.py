while True:
    ch=int(input("choose the operation\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Exit\n:"))
    a,b=eval(input("Enter number(separate by commas):"))
    if ch==1:
        print(a,"+",b,"=",a+b)
    elif ch==2:
        print(a,"-",b,"=",a-b)
    elif ch==3:
        print(a,"/",b,"=",a/b)
    elif ch==4:
        print(a,"*",b,"=",a*b)
    elif ch==5:
        break
    else:
        print("Invalid Entry")
