##que1.Write a program to create a function that takes two arguments, name and age, and print their value.
def create_fun(name,age):
    print("My name is",name)
    print("my age is",age)

create_fun("madhuri",26)

##que2.Create a function with variable length of arguments.
def var_length(*x):
    print("This function is variable leegth of arguments")
    print(x)

var_length(20,40,60)    

def var_arguments(a=80,b=100):
    print("this  is variable arguments")
    print(a,b)
var_arguments()    

### or
def var_arg(*argv):
    for i  in argv:
        print(i)
var_arg(20,40,60)
var_arg(80,100)

##que3.it can accept two variables and calculate addition and subtraction. Also, 
# it must return both addition and subtraction in a single return call.
def calculation(a,b):
    add=a+b
    print("the addition of two numbers is:=",a+b)
    sub=a-b
    print("The subtraction of twonumbers is:=",a-b)
    return add,sub
calculation(31,22)    

## ## or 
def calculation_fun(a,b):
    return a+b,a-b
add,sub=calculation_fun(40,10)
print(add,sub)

##que4.Write a program to create a function show_employee() using the following conditions.
#It should accept the employee’s name and salary and display both.
#If the salary is missing in the function call then assign default value 9000 to salary

def show_employee(name="Madhuri",salary="180000"):
    print("Name:",name,"salary:",salary)

show_employee()
show_employee("anant",200000)

##que5.Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters, a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it
def outer_fun(a,b):
    square=a**2
    def inner_add(a,b):
        return a+b
        add=inner_add(a,b)
    return add + 5
print(outer_fun(40,10))  

##que6.rite a program to create a recursive function to calculate the sum of numbers from 0 to 10.
# A recursive function is a function that calls itself, again and again.
def addition(num):
    if num:
        return num+addition(num-1)
    else:
        return 0
res=addition(10)
print(res)        

### or---
def recursive_sum():
    add=0
    for x in range(0,11):
        add=add+x
    return add
print(recursive_sum())

### factorial number
def fact_num(x):
    if x==0:
        return 1
    else:
        return x*fact_num(x-1)
print(fact_num(5))            

##que 7.Assign a different name to function and call it through the new name Below is the function display_student(name, age). 
# Assign a new name show_tudent(name, age) to it and call it using the new name.
def student_display(name,age):
    print(name,age)
student_display("Madhuri",26)
show_student=student_display
show_student("Madhuri",26)

## or 
def function1(name,age):
    print(name,age)
function1("Anant",30)
new_function=function1
new_function("Anant",30)    

##que8.Generate a Python list of all the even numbers between 4 to 30
def list_evenodd():
    l2=[]
    for i in range(4,31):
        if i%2==0:
            l2.append(i)
    print(l2)   
    return l2
list_evenodd() 

## or 
print(list(range(4,30,2)))

##que9.Find the largest item from a given list

def large_num(lst):
    max=4
    for i in lst:
        if i>max:
            max=i
    print("The largest number in list is:=",max)  
lst = [4, 6, 8, 24, 12, 2]
print(lst) 
large_num(lst)   

### or
lst = [4, 6, 8, 24, 12, 2]
print("The large number:=",max(lst))

### forminimum number
def min_num(lst1):
    min=4
    for x in lst1:
        if x<min:
            min=x
    print("The minimum number is",min)        
lst1 = [4, 6, 8, 24, 12, 2] 
print(lst1)
min_num(lst)           




### by using filter:
def filter_fun(x):
    lst=['e','a','b','e','m','s']
    print(lst)
    if x in lst:
       return x
    return False
sequence=['w','a','e','c','d']
print(sequence) 
filterd=filter_fun(sequence) 
print('filterd letters are:=')  
for s in sequence:
    print(s,end=' ')
print()



    


