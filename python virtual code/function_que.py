##que1.Write a Python function to find the Max of three numbers
#def max_number():
 #   num1=int(input("enter the first number:="))
  #  num2=int(input("Enter the second number:="))
   # num3=int(input("Enter the third number:="))
    #if num1>num2:
     #   print(num1,"is grater then",num2)
    #elif num2>num3:
   #     print(num2,"is grater than",num3)
   # elif num3>num1:
    #    print(num3,"is grater than",num1)       

    #return max_number
#max_number()

#### or-----


from re import I


def maximum_num(a,b,c):
    if (a>b) and (a>c): 
        print("Maximum number is :=",a)
    elif (b>a) and (b>c):
        print("maximum number is:=",b)
    elif (c>a) and (c>b):
        print("the maximum number is:=",c)       
    return maximum_num
maximum_num(2,3,11)   

##que2.Write a Python function to sum all the numbers in a list. Sample List : (8, 2, 3, 0, 7) Expected Output : 20
def Sum_all_numbers(lst):
    sum=0
    for i in lst:
        sum=sum+i
    print("The sum of all numbers in list:=",sum)
lst=[8,2,3,0,7]
print(lst)
Sum_all_numbers(lst)    

##que3.Write a Python function to multiply all the numbers in a list.  Sample List : (8, 2, 3, -1, 7) Expected Output : -336
def multiply_numbers(lst):
    mul=1
    for i in lst:
        mul=mul*i
        
    print("The multiplication of all numbers in list:=",mul)
lst=[8,2,3,-1,7]
print(lst) 
multiply_numbers(lst)  

##que4.Write a Python program to reverse a string.  Sample String : "1234abcd" Expected Output : "dcba4321"

def reverse_str():
    str1="1234abcd"
    print("Before reverse string:=",str1)
    
    print("After reverse string:=",str1[::-1])
reverse_str()    

##que5.write progrm for divisition of two number and division by large number divider by small,
# if user smallnum divider bye large the it convert.
def decorator_div(func):
    def inner(x,y):
        x,y=y,x
        return func(x,y)
    return inner
@decorator_div
def div_fun(a,b):
    
    return b/a
print("the divisition of two numbers",div_fun(10,2))

##que6.Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def factorial_fun(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of",num,'is:=',fact)
factorial_fun(5)    

## another way

def fact_num(n):
    if n==0:
        return 1
    else:
        return n*fact_num(n-1) 
#n=int(input("Enter the number:="))
#print("factorial of",n,'is:=',fact_num(n))   
print("The factorials:=",fact_num(4))

##que7.Display an error message if n is a negative or a floating point number for factorial .
def factorial(n):
    if not (n>=0) and  (n%1==0):
        return("Number can't be negative or floating point!")
    return 1 if n==0 else n*factorial(n-1)
#n=int(input("Enter the number:="))
print("factorial",factorial(-2))   

##que8.Write a Python function to check whether a number falls in a given range
def number(n):
    if n in range(1,10):
        print("The gievn number {} is present in given range".format(n))
    else:
        print("The given number  {} is not present in given range".format(n))
number(9)
   
##que9.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
#Sample String : 'The quick Brow Fox' Expected Output :No. of Upper case characters 3 : No. of Lower case Characters : 12
def cal_upper_lower():
    str1='The quick Brow Fox'
    print(str1)
    count_upper=0
    count_lower=0
    for c in str1:
        if c.isupper():
            count_upper+=1
        elif c.islower():
            count_lower+=1    
    
    print("No. of Upper case characters:=",count_upper)
    print("No. of Lower case Characters :",count_lower)
cal_upper_lower()  

##que10.Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5] Unique List : [1, 2, 3, 4, 5]
def set_unique(list1):
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2
    
print(set_unique([1,2,3,3,3,3,4,5]))    

##que11.Write a Python function that takes a number as a parameter and check the number is prime or not

def prime_number(num=11):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                print(num,"is not a prime number")
        else:
            print(num,"is a prime number")
prime_number(num=11)                    
    
prime_number(num=11) 

### or---
def prime_num(num=29):
    flag= False
    if num>=1:
        for i in range(2,num):
            if (num%i==0):
                flag=True
                break
    if flag:
        print(num,"is not a prime number")
    else:
        print(num,"is prime number")  

prime_num(num=29)  

##que12.Write a Python function that checks whether a passed string is palindrome or not.
def ispalindrom(str1):
    left_pos=0
    right_pos=len(str1)-1
    while left_pos >= right_pos:
        if not left_pos==right_pos:
            return False
        left_pos+=1
        right_pos-=1
    return True
print(ispalindrom("remainder"))  

##que13.11.	Write a Python function to check whether a string is a pangram or not Note : Pangrams are words or 
# sentences containing every letter of the alphabet at least once. For example : "The quick brown fox jumps over the lazy dog"

## que14.Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).
def square_num():
    l=list()
    for i in range(1,30):
        
        l.append(i**2)
    print(l,end=' ')
    return l    
square_num()        


   
