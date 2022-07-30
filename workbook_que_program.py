## Write a program that asks the user to enter his or her name. The program should
#respond with a message that says hello to the user, using his or her name
#user=(input("Enter the Name:"))
#print("Hello",user)

# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with

# width= float(input("Enter the width of room in feet:="))
# length=float(input("Enter the length of room in feet:="))
# Area=length*width
# print("Area of room=",Area,"square feet")

## Create a program that reads the length and width of a farmer’s field from the user in feet. Display the area of the field in acres
# width= float(input("Enter the width of room in feet:="))
# length=float(input("Enter the length of room in feet:="))
# squ_per_acr=43560
# Area=length*width/squ_per_acr
# print("Area of of the feild in acres=",Area)

# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places
# less_deposit=0.10
# more_deposit=0.25
# less=int(input("How many containers 1 litter,less do you have?"))
# more=int(input("How many containers more than 1 litter,do you have?"))
# refund=(less_deposit*less)+(more_deposit*more)
# print("Your total refund will be $%.2f",refund)

# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

# cost=float(input("Enter the cost of meal="))
# tax_rate=0.05
# tip_rate=0.18
# tax=tax_rate*cost
# tip=tip_rate*cost
# total=cost+tax+tip
# print("The Tax is:",tax ,"\n The Tip is:",tip,"\nTotal is:",total)

# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)/2
# n=int(input("Enter the number="))
# sum1=(n)*(n+1)/2
# print("sum of all integers from 1 to",n,"=",sum1)

## Exercise 9: Compound Interest
# formula of compound interest =  A = p * (pow((1 + r / 100), t))

# p=int(input("Enter the principle of ammount:="))
# r=int(input("Enter the  interest of rate:="))
# t=int(input("Enter the total number of year:="))
# compound_int=p*(pow((1+r/100),t))
# print("compound interest:=",compound_int)

# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# 6 1 Introduction to Programming Exercises
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in t


# from math import log10

# a=int(input("Enter the value  of a:="))
# b=int(input("Enter the value of b:="))
# print(a ,"+",b ,"is",a+b)
# print(a ,"-",b ,"is",a-b)
# print(a ,"*",b ,"is",a*b)
# print(a ,"/",b ,"is",a/b)
# print(a ,"+",b ,"is",a+b)
# print(a ,"//",b ,"is",a//b)
# print(a ,"%",b ,"is",a%b)

# print("The base 10 logrithim of:=",log10(a))
# print(a,"^",b,"is",a**b)

## ---------------------------------  from on if else ---------------------------##
##----------------------------------***************** -------------------------------##

#Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd

# n=int(input("Enter the number:="))
# if n%2==0:
#     print(n,"is a even number.")
# else:
#     print(n,"is a odd number.")

# Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.
# dog_year=int(input("Enter the dog year:=",))
# dog_age_to_human_age1=10.5*dog_year
# dog_age_to_human_age2=4*(dog_year-2)
# dog_1=[]
# if dog_year<0:
#     print("Please enter an positive hole integer number")
# elif dog_year>0 and dog_year<=2:
#     print(dog_age_to_human_age1)
#     #dog_1.append(dog_age_to_human_age1)
# for dog_year in range(3,dog_year+1):
#     dog_1.append(dog_age_to_human_age2)
#     print(dog_1[-1]+21)

# Vowel or Consonan
# s="Madhuri"
# t=('a','e','i','o','u')
# for i in s:
#     if i in t:
#         print(i,end='')
#     else:
#         False

## orr--
# s="Madhuri"
# t=('a','e','i','o','u')
# vowels=tuple(filter(lambda a:a if a in s else False,t))
# print(vowels)

# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.
# inside=int(input("Enter the number of sides:="))
# name=" "
# if inside == 3:
#     print("Triangle")
# elif inside ==4:
#     print("Square")
# elif inside == 5:
#     print("Pentogon")
# elif inside == 6:
#     print("Hexagon")
# elif inside == 7:
#     print("Heptagon")
# elif inside == 8:
#     print("octagon")

# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
#for February so that leap years are addressed

# month=int(input("Enter the number bwteween 1 to 12:="))
# year=int(input("Enter the year:="))
# if month == 2:
#     if (year % 4==0) and (not(year% 100==0)) or (year%400==0):
#         days=29
#         print("This year is a leap year and number of days in month:=",days)
#     else:
#         days=28
#         print("This year is not a leap year and number of days in month:=",days)
# elif month in(1,3,5,7,8,10,12):
#     days=31
#     print("Number of days in month:=",days)
# elif month in (4,6,9,11):
#     days=30
#     print("number of days in month:=",days)
# else:
#      if month>=13:
#          print("Sorry we can't enter the month of value above 12 number")

##Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters
# a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume
# that a valid position will always be entered. It does not need to perform any error
# checking
# alphabet="abcdefgh"
# block=input("Enter the position of block:=")
# column=int(alphabet.index(block[0]))+1
# row=int(block[1:])
# if row<9:
#     position= column + row
#     if position % 2 == 0:
#         print("The Block is \"Black\"")
#     else:
#         print("The Block is \"White\"")
# else:
#      print("Invalid Input")


### sort list
# l1=[90,56,110,34,31,14,2,9]
# print("l1=",l1)
# l2=[]
#
# while l1:
#
#     max1 = l1[0]
#     for i in l1:
#         if i>max1:
#             max1=i
#     l2.append(max1)
#     l1.remove(max1)
# print(" Sort Decending order=",l2)
#
# ## sort ascending order
# l3=[200,34,678,99,4,565,90]
# print(l3)
# l4=[]
# while l3:
#     min1=l3[0]
#     for i in l3:
#         if i<min1:
#             min1=i
#     l4.append(min1)
#     l3.remove(min1)
# print("ascending order=",l4)

## reverse list=
# lst=[]
# for num in range(0,5):
#     num=int(input("Enter element"))
#     lst.append(num)
# print(lst)
# for i in range(len(lst)-1,-1,-1):
#     print(i)

## remove duplicates


