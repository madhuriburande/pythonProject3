#### for using lambada
##que1.addition  for twonumber and get value from user.
from tempfile import tempdir


add=(lambda x: x+x)
print(add(10))

#x=int(input("Enter the first number:="))
#y=int(input("Enter the second number:="))
#sum=(lambda x,y: x+y)
#print(sum(x,y))

addition=lambda x,y: x+y
print(addition(20,30))

## que2.subtraction by using lambda.
sub=lambda x,y: x-y
print("The addition of two numbers is:=",sub(110,10))

#x=int(input("Enter the first number:="))
#y=int(input("Enter the second number:="))
#sum=(lambda x,y: x-y)
#print(sum(x,y))

## multiplication 
mul=lambda x: x*x 
print("The multiplication is:=",mul(5))

#a=int(input("Enter the first number:="))
#b=int(input("Enter the second number:="))
#multiplication=lambda a,b: a*b
#print("The multiplication of two numbers is:=",multiplication(a,b))

## Divisition
div=lambda a,b:a/b
print("the divisition of two numbers is:=",div(50,25))

## even odd number by usinglambda
evenodd=lambda x: 'even' if x%2==0 else 'odd'
print("The given numner is",evenodd(22))

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
print(my_list)
list1=list(filter(lambda x: x%2==0,my_list))
print("The even number numbers in list:=",list1)

l1=[1,2,4,8,9,4,11,23,33]
l2=list(filter(lambda x :  x%2==0,l1))
print(l2)

############# By using filter###############
## program for filter out the odd items from list
l1=[3,5,7,9,2,4,6,8,11]
print(l1)
l2=list(filter(lambda x: x%2==1,l1))
print("The odd number is in list:=",l2)

## program for filter out the max number from list
l3=[31,22,14,23,5,3,]
print(l3)
print("The max number is",max(l3))
print("The min number is",min(l3))
l3.sort()
print("The sort list is:=",l3)
###### sorted list by using function###########
def sorted_list(lst):
    for i in range(len(lst)-1,0,-1):
        for x in range(i):
            if lst[x]>lst[x+1]:
                temp=lst[x]
                lst[x]=lst[x+1]
                lst[x+1]=temp
    return lst
lst=[77,22,31,23,5,3,28,10]
print(lst)
result=sorted_list(lst) 
print(result)               

#### factoraila number ########
num=int(input("Enter the number:="))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("The factorial number is",fact)

## que.by using filter filterout the two list .commom elelmnet filter.
list1=['a','b','c','e','d','e','e']
lst=['a','c','m','e','b']
z=list(filter(lambda x: True if x in lst else False , list1))
print(z)
##que.python program to display all the prime numbers within an interval
#def prime_num(num):
    #num=int(input("enter the number:="))
    

