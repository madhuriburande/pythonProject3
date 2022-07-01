##que1.Write a program to prompt the name of a user and print the welcome message, “Dear Name_of_user Welcome to Python Programming!!!”
from re import X
from tkinter import Y


def message(name):
    print("Dear",name,"Wlcome to python Programming")
message("Madhuri")  

## from user definename
#def message_fun():
    #name=str(input("Please Enter your name:="))
    #print("Dear",name,"Wlcome to python Programming.")
#message_fun()  

##que2.Write a program to illustrate the use of functions.sumof 1 to 25,50 to 75,90 to 100.
def sum(x,y):
    s=0
    for i in range(x,y+1):
        s=s+i
    print("The sum of integers",x,'to',y ,'is:=',s)
    
sum(1,25) 
sum(50,75)
sum(90,100)  

##que3.Write a program to fi nd the maximum of two numbers.
def max_number(num1,num2):
    print("Num1:=",num1)
    print("Num2:=",num2)
    if num1>num2:
        print("The number",num1,'is grater than',num2)
    elif num1<num2: 
        print("The number",num2, 'is grater than',num1)   
    else:
        print("the number",num1,'and',num2,'are equals')
max_number(31,22)

##que4.Write a program to find the factorial number. 
def cal_factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial number of",num,"is:=",fact)
#num=int(input("Enter the number:="))
cal_factorial(5)        

##que5.Write a simple program on keyword argument.
def key_arg(name,age):
    print("Name:",name,"Age:",age)
key_arg("Madhuri",26)

##que6.Precautions for Using Keyword Arguments 
def Display(num1,num2):
    print('num1:',num1,'num2:',num2)
Display(31,22)

##by default value
def Display_default(x,y=22,z=10):
    return x+y+z
print("The addition of three numbers are:=",Display_default(31) )

## default 
def message_default(name,msg="Welcome to python wolrd!!!"):
    print("Hello",name,msg)
message_default("Madhuri")    
message_default("Anant")
message_default("Bill Gates","How are you?")

##que7.Write a program to calculate the area of a circle using the formula:Area of Circle = pi*(r) 2
##Declare the default parameter value of pi as 3.14 and radius as 1.
def area_of_circle(pi=3.14,radius=1):
    
    Area=pi*radius*radius
    print("Radius is:=",radius) 
    print("The default value of pi is:=",pi)
    print("The Area of circle is:=",Area)
area_of_circle(radius=5) 

##que8.What will be the output of the following program?
def  Disp_values(a,b=10,c=20):
    print('a=',a,'b=',b,'c=',c)
print("The output of program will be below display:")    
Disp_values(15)
Disp_values(50,b=30)
Disp_values(c=80,a=25,b=35)  
   
##que9.Write a program to show local scope vs global scope.
p=10
def demo_of_scope():
    q=20
    print("The value  of local variable q is:=",q)
    print("The value of global varable p is:=",p)
demo_of_scope()    
print("The value of global varable p is:=",p)  ## acess the value of p is outside the function.

##-Note------>Local Variables Cannot be Used in Global Scope.

## que10.Write a program where global variables are read from a local scope
def demo():
    print(s)
s="I love Python"    
demo()    

##Local and Global Variables with the Same Name
##que11.Write a program to change the value ‘s’ within the function.
def change_val():
    s="I love Programming"
    print(s)
s="I love Java" 
change_val()
print(s) 

##que12.Write a program without using the global statement
a=10
def function1():
    a=30
    print("The value display inside the function",a)
function1()
print("The value display outside the function",a)  

##que13.Write a program using the global statement.
a=31
def global_key():
    global a
    a=22
    print("The value of inside the function",a)
global_key()
print("The value of outside the function",a)   

## another example.
x=45
def add_fun():
    global X
    y=30
    sum=x+y
    print("The addition of two numbers is:=",sum)
add_fun()

## Return statment---
##que14.Write a program to return the minimum of two numbers.
def minimum_val(num1,num2):
    if num1<num2:
        return num1
    elif num1>num2:
        return num2  

print("The minimum number is:=",minimum_val(31,22))

##que14.Write a program to return the maximum of two numbers.
def minimum_val(num1,num2):
    if num1>num2:
        return num1
    elif num1<num2:
        return num2  

print("The maximum number is:=",minimum_val(31,22))

##que15.Write a function calc_Distance(x1, y1, x2, y2) to calculate the distance between two points represented by 
# Point1(x1, y1) and Point2 (x2, y2). The formula for calculating distance is:Distanc= - + - ( ) 2 2

import math
def cal_distance(x1,y1,x2,y2):
    print('x1=',x1)
    print('y1=',y1)
    print('x2=',x2)
    print('y2=',y2)
    dx=x2-x1
    dx=math.pow(dx,2)
    dy=y2-y1
    dy=math.pow(dy,2)
    z=math.pow(dx+dy,0.5)
    return z
print("The calculate distance between two",(format(cal_distance(4,4,2,2),'.2f')))

##que16.For a quadratic equation in the form of ax2+bx+c, the discriminant D, is b2- 4ac. Write afunction to compute the discriminant D, 
# that returns the following output depending on thediscriminant D.
 #if D > 0: The Equation has two Real Roots
 #if D = 0: The Equation has one Real Root
 #if D < 0: The Equation has two Complex Roots
def quadratic_equ(a,b,c):
    d=b*b-4*a*c
    print('a=',a)
    print('b',b)
    print('c',c)
    if d>0:
        return "The Equation has two Real Roots"
    elif d==0:
        return "The Equation has one Real roots"

    elif d<0:
        return "The Equation has two complex roots"
print(quadratic_equ(1,2,5))  


##que17.Write a program to pass the radius of a circle as a parameter to a function area_of_circle().
##Return the value none if the value of the radius is negative or return the area of the circle.
def area_of_Circle(radius):
    if radius<0:
        print("Try again,radius of circle can not be negative")
        return
    else:
        return 3.14*radius*radius
print("The area of circle is:=",area_of_Circle(3))    

##que18.What will be the output of the above program?
def cal_abc(x):
    if x<0:
        return -X
    elif x>0:
        return X
print(cal_abc(0))       

##que19.Write a function calc_arith_op(num1, num2) to calculate and return at once the result of arithmetic operations such as 
# addition and subtraction.
def cal_arith(num1,num2):
    return num1+num2,num1-num2
print(cal_arith(31,22))   

##que20.Write a program to return multiple values from a function.
def cal_fun_cube(n):
    print("Number:=",n)
    return n*n,n*n*n
square,cube=cal_fun_cube(5)
print("The square is",square)    
print("The cube is",cube)

### recursion function.
##que21.Calculate the factorial of a number using recursion.
def factorial_fun(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of",num,'is:=',fact)
factorial_fun(5)

### or-----
def factorial(n):
    if n==0:
        return 1
    else:
        return  n* factorial(n-1)
print("The factorial of:=",factorial(3)) 

##que22.Write a recursive function which computes the nth Fibonacci number. Fibonacci numbers aredefined as:
#Fib(0)= 1,
#Fib(1) = 1
#Fib(n)= Fib(n-1)+Fib(n-2)
def fib(n):
    if n==0:
        return 1
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
print("The Value of 8th Fibonacci number = ",fib(6))     











