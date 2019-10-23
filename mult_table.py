#multiplication table
print("________Multiplication table________")
ch=int(input("For which number:"))

for i in range(1,11):
    print(ch,"X",i,"=",ch*i,end="\n")
    
"""
OUTPUT:


________Multiplication table________

For which number:5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50

________Multiplication table________

For which number:12
12 X 1 = 12
12 X 2 = 24
12 X 3 = 36
12 X 4 = 48
12 X 5 = 60
12 X 6 = 72
12 X 7 = 84
12 X 8 = 96
12 X 9 = 108
12 X 10 = 120

"""