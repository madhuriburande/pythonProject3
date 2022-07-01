##que1.Write a program that prompts a user to enter two integer values. Print the message ‘Equals’ if
##both the entered values are equal.
num1=int(input("Enter the first value:="))
num2=int(input("Enter the second value:="))
if num1==num2:
    print("both values are eqals")
else:
    print("both values are not equals")
    
##que2.Write a program which prompts a user to enter the radius of a circle. If the radius is greater than
##zero then calculate and print the area and circumference of the circle.
radius=int(input("Enter the radius of circle"))
pi=3.14
if radius>0:
    area=pi*radius*radius
    print("Area of circle is:=",area)
    circumference=2*pi*radius
    print("Area of circumference is:=",circumference)  

##que3.Write a program to prompt a user to enter two numbers. Find the greater number. 
num1=int(input("Enter the first number:="))
num2=int(input("Enter the second number:="))
if num1>num2:
    print("first number is grater than second number:=",num1)
else:
    print("Second number is grater than the first number:=",num2)  

#Write a program to calculate the salary of a medical representative considering the sales
#bonus and incentives offered to him are based on the total sales. If the sales exceed or equal to
#`1,00,000 follow the particulars of Column 1, else follow Column 2.
#Column 1                      Column 2
#Basic = `4000                 Basic = `4000
#HRA = 20% of Basic            HRA = 10% of Basic
#DA = 110 % of Basic           DA = 110 % of Basic
#Conveyance = `500             Conveyance = `500
#Incentive = 10% of Sales      Incentive = 4% of Sales
#Bonus = `1000                 Bonus = `500
sales=float(input("Enter the total sales of month:="))
if sales>=1000:
    basic=4000
    hra=20*basic/100
    da=110*basic/100
    conveyance=500
    incentive=10*sales/100
    bonus=1000
    
else:
    basic=4000
    hra=10*basic/100
    da=110*basic/100
    conveyance=500
    incentive=4*sales/100
    bonus=500
salary=basic+hra+da+incentive+bonus+conveyance
print('Salary Receipt of Employee')
print('Total Sales = ',sales)
print('Basic = ',basic)
print('HRA = ',hra)
print('DA = ',da)
print('Incentive = ',incentive)
print('Bonus = ',bonus)
print('Conveyance = ',conveyance)
print('Gross Salary = ',salary) 

##que5.Write a program to test whether a number is divisible by 5 and 10 or by 5 or 10. 
num=int(input("Enter the value:="))
if num%5==0 and num%10==0:
    print("number is divisible by 5 and 10")
    
if num%5==0 or num%10==0:
    print("number is divisible by 5 or 10")
else:
    print("number is not divisilbe by 5 and 10")

 ##que6.Write a program to read three numbers from a user and check if the first number is greater or
#less than the other two numbers.
num1=int(input("Enter the first value:="))
num2=int(input("Enter the second value:="))
num3=int(input("Enter the third value:="))
if num1>num2 and num1>num3:
    print("first number is grater than other two numbers:=",num1)
elif num1<num2 and num1<num3:
    print("first number is less than of other two numbers:=",num1)

##que7.write a program for take subject and final total and chek pass and fail students
mark=int(input("Enter the marks of studen:="))
subject='English'
total=100
if mark>40:
    print('In',subject,total,"out of",mark," and result is pass")
else:
    print('In',subject,total,"out of",mark," and result is fail")

##que8.by using list doaddition and multiplication
l1=[2,3,4]
l2=[4,5,6]
sum=l1[0]+l2[0],l1[1]+l2[1],l1[2]+l2[2]
print("Addtion of two list is:=",sum)
mul=l1[0]*l2[0],l1[1]*l2[1],l1[2]*l2[2]
print("multiplication of two list is:=",mul)

##que9.Write a program to prompt a user to read the marks of fi ve different subjects. Calculate the
##total marks and percentage of the marks and display the message according to the range of
#percentage given in table.
#Percentage                     Message
#per > = 90                      Distinction
#per > = 80 && per < 90          First Class
#per > = 70 && per < 80          Second Class
#per > = 60 && per < 70          Third Class
#per <60                         Fail

sub1=int(input("Enter the marks of python:="))
sub2=int(input("Enter the marks of java:="))
sub3=int(input("Enter the marks of Data sturucture:="))
sub4=int(input("Enter the marks of c++:="))
sub5=int(input("Enter the marks of dotnet:="))
sum=sub1+sub2+sub3+sub4+sub5
print("total 500 out of",sum)
per=sum/5
print("percentage",per)

if per>=90:
    print("Distinction")
    
elif per >=80 and per<90:
    print("First Class")
    
elif per>=70 and per<80 :
    print("Second Class")  

elif  per>=60 and per< 70:
    print("Third Class")
    
elif per<60:
    print("Fail")
else:
    print("No result")

##que10.Write a program to prompt a user to enter a day of the week. If the entered day of the week is
#between 1 and 7 then display the respective name of the day. 
day=int(input("Enter the day of week:="))
if day==1:
    print("The day of week is Monday")
    
if day==2:
    print("The day of week is Tusday")
    
if day==3:
    print("The day of week is Wen'sday")
    
elif day==4:
    print("The day of week is Thursday")
        
elif day==5:
    print("The day of week is Friday")
            
elif day==6:
    print("The day of week is Saturday")
    
elif day==7:
    print("The day of week is Sunday")
    
else:
    print("Complete weekend")


 ##que11.Write a program that prompts a user to enter two different numbers. Perform basic arithmetic
##operations based on the choices.
num1=int(input("Enter the first number is:="))
num2=int(input("Enter the second number is:="))
print('1 Addition')
print('2 Subtraction')
print('3 Multiplication')      
print('4 Division') 

choice=int(input("Please enter the choice:="))
if choice==1:
    print(num1,'and',num2,"The Addition is:=",num1+num2)
    
elif choice==2:
    print(num1,'and',num2,"The subtraction is:=",num1-num2) 
    
elif choice==3:
    print(num1,'and',num2,"The Multiplication is:=",num1*num2)      
    
elif choice==4:
    print(num1,'and',num2,"The Division is:=",num1/num2)
    
else:
    print("wrong choice")


 ##que12.Write a program to find the smaller number among the two numbers.
num1=int(input("Enter the frist number:="))
num2=int(input("Enter the second number:="))
if num1>num2:
    print("The minimum number of",num1,'and',num2,'is',num2)
else: 
    print("The minimum number of",num1,'and',num2,'is',num1)
    
    
 #################### mini project################
############# Finding the Number of Days in a Month ####################

month=int(input("Enter the month value from(1-12):="))
year=int(input("Enter the year:="))

if month==2:
    if (year%4==0) and (not(year%100==0)) or (year%400==0):
        days=29
        print("This year is leap year and number of days in month",days)
    else: 
        days=28
        print("This year is not leap year and number of days in month",days)
elif month in (1,3,5,7,8,10,12):     ##month=jan,march,may,july,aug,oct and dec only 31 days
    days=31
    print("Number of days in month is:=",days)
    
elif month in(4,6,9,11):     ##month=april,june,sep,nov
    days=30
    print("Number of days in month is:=",days)
    
else:
    print("no days")

##que13.write program for leap year is or not
year=int(input("Please enter the year number:="))
if (year%4==0) and (not(year%100==0)) or (year%400==0):
    print("This year is leap year:=",year)
else:
    print("This year is not leap year:=",year)                   