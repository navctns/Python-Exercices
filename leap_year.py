#leap year

yr=int(input("Enter the year to check :"))
if ((yr%4==0)&(yr%100!=0) | (yr%100==0) & (yr%400==0)):
    print(yr, " is a leap year")
else:
    print(yr, " is not a leap year")


"""
Output:

Enter the year to check2012
2012  is a leap year

Enter the year to check2015
2015  is not a leap year


Enter the year to check1804
1804  is a leap year

Enter the year to check :1820
1820  is a leap year

Enter the year to check :2000
2000  is a leap year

Enter the year to check :2400
2400  is a leap year

Enter the year to check :2200
2200  is not a leap year

"""
