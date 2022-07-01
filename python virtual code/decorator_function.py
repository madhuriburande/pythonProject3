def hello_decorator(func):
    def inner1():
        print("Hello this is before function execuation")
        func()

        print("This afetr function  execuation")
    return inner1
def function_to_be():
    print("This is inside the function!!!")
function_to_be=hello_decorator(function_to_be)

function_to_be()

def fun_decorator(func):
    def inner1(*arg,**kwargs):
        print("Before execuation")
        returned_value= func(*arg,**kwargs)
        print("After the execution")
        return returned_value
    return inner1  
@fun_decorator   
def sum(a,b):
    print("Inside the function!!")
    return a+b
print("sum of two numbers",sum(20,30) )   

##que1.write program  for addition,subtraction,divisition,multiplication  by using decorator 
def decorator1(func):
    def inner1(x,y):
        sum=func(x,y)
        print("This resultis addition of",x,'and',y,'is:=',sum)
        return sum
    return inner1    
  
def decorator2(func):
    def inner2(p,q):
        #x=int(input("enter the first number:="))
        #y=int(input("enter the secondnumber:="))
        div=func(p,q)
        print("The division of",p,'and',q,'is:=',div)
        return div
    return inner2

def decorator3(func):
    def inner3(r,s):
        mul=func(r,s)
        print("The multiplication of ",r,'and',s,'is:=',mul)
        return mul
    return inner3

def decorator4(func):
    def inner4(m,n):
        sub=func(m,n)
        print("The subtraction of",m,'and',n,'is:=',sub)    
        return sub
    return inner4
@decorator1
@decorator2
@decorator3
@decorator4

def Arithematic(a,b):
    sum=a+b
    div=a/b
    mul=a*b
    sub=a-b
    result=sum,div,mul,sub
    return result
Arithematic(45,9) 
           

##que.erite prigram for min and max by using  function.
def Maximum_num(lst):
    max=10  
    for i in lst:
        if i>max:
            max=i
    print("The maximum number is present in list is:=",max)
    return Maximum_num
lst=[10,31,22,4,5,3,23,28]  
Maximum_num(lst)     

def div(a,b):
  
    return a/b


def decor_func(func):
    def inner(x,y):

        return func(x,y)
        
    return inner
divno=decor_func(div)
print(divno(10,2))

### imp
def div(a,b):
    print(a/b)
def deco_div(func):
    def inner(a,b):
        a,b=b,a
        return func(a,b)
    return inner
div1=deco_div(div)
div1(2,10)


