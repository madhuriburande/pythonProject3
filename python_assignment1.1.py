##1.Python Program for factorial of a number with and without recursion
### with recursion:
def factorial(num):
    if num==0:
        return 1
    if num==1:
        return 1
    else:
        return num*(factorial(num-1))
print("Factorial is:=",factorial(5))

## without recursion:
def fact_num(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print("Factorial is:=",fact)
#num=int(input("Enter The Number:="))
fact_num(7)


## 2.Python Program to check Armstrong Number
#num=int(input("Enter The Number:="))
num=153
n=num
sum1=0
while num!=0:
    r= num%10
    sum1=sum1+(r*r*r)
    num=num//10
if n==sum1:
    print("The given number",n,"is armstrong number.")
else:
    print("The given number",n,"is not aremstrong number.")
    
## 3.Python program to print all Prime numbers in an Interval
def prime_num():
    for num in range(100):
        for i in range(2,num):
            if num%i==0:
                break
                print(num,"is not prime number.")
        else:
            print(num,"is a prime number")
prime_num()
        
## 4.Python Program for Fibonacci numbers
def Fib(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return Fib(num-1)+Fib(num-2)
print("Fibonacci series is:=",Fib(10))

## with itervals:
def fib(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        return fib(num-1)+fib(num-2)
for i in range(0,12):
    print(fib(i))
    
## 5.Python Program to find sum of array (using multiple approach)
# 1 way by using for loop or itrerate.
l1=[1,2,3,4,5,10,20,30]
print(l1)
sum1=0
for i in l1:
    sum1=sum1+i
print("The addition of array is:=",sum1)
# 2 way,by using inbuild fun i.e sum 
arr=[31,22,14,10,5]
print(arr)
print("Sum of array is:=",sum(arr))

## 3 way by using function
def sum_arr(l1):
    sum1=0
    for i in l1:
        sum1=+sum1+i
    return sum1
l1=[7,8,9,11,12,13]
print("The sum of array is:=",sum_arr(l1))


## 6.Python Program to find largest element in an array
## without inbuilt function 
list1=[10,23,3,5,22,31,28]
print("Original list:=",list1)
largest=10
for i in list1:
    if i>largest:
        largest=i
print("In array largest number is:=",largest)
## with inbuilt function
arr=[10,2,7,12,8,9,67,100]
print("Original array:=",arr)
print("Largest number is:=",max(arr))

## 7.Python Program for array rotation
l1=[1,2,3,4,5,6]
print("Original list:=",l1)
print(l1)
temp=l1[0]
l1[0]=l1[-1]
l1[-1]=temp
res=l1[1]
l1[1]=l1[-2]
l1[-2]=res
for i in l1:
    print(i,end=' ')
print()
    

    
## 8.Python Program for Reversal algorithm for array rotation

## 9.Python Program to Split the array and add the first part to the end
l2=[6,5,4,3,2,1]
print("Original list:=",l2)
ouput=[1,2,4,3,5,6]
temp=l2[0]
l2[0]=l2[-1]
l2[-1]=temp
res=l2[1]
l2[1]=l2[-2]
l2[-2]=res
for i in l2:
    print(i,end=' ')
print()

## 10.Python Program for Find reminder of array multiplication divided by n 
from functools import reduce
def find_reminder(arr,n):
    sum_1= reduce(lambda x,y: x*y,arr)
    reminder= sum_1% n
    print("The reminder of array of multiplication divided by n is:=",reminder)
arr=[100, 10, 5, 25, 35, 14]
print("original array:",arr)
n=11
find_reminder(arr,n)
print()

## 11.Python program to interchange first and last elements in a list
list1=[31,5,3,23,10,28,22]
print("Original list:=",list1)
temp=list1[0]
list1[0]=list1[-1]
list1[-1]=temp
print("After inter change first and last element in list are:")
for i in list1:
    print(i,end=' ')
print()

## 12. Python program to swap two elements in a list
def swap_list(s,pos1,pos2):
    s[pos1],s[pos2]= s[pos2],s[pos1]
    return s
s=["Madhuri","Ankita","komal","harshada","Swara"]
print("Original list:",s)
pos1,pos2=1,3   ## swappotion 1,3 in list
print(swap_list(s,pos1,pos2))

## 13. Python program to remove Nth occurrence of the given word
lst=['Apple','Banana','Cherry','Mango','Strwaberry']
print(lst)
#n=2

word='Cherry' ## remove tjis word index pos=2
def remove_word(lst,word):
    for i in lst:
        if i==word:
            lst.remove("Cherry")
            print(lst)
        else:
            pass
remove_word(lst,word)

## or
l1=[1,2,3,4,5]
print(l1)
l1.remove(3)
print(l1)

## or
def RemoveIthWord(lst, word, N):
    newList = []
    count = 0
    for i in lst:
        if(i == word):
            count = count + 1
            if(count != N):
                newList.append(i)
        else:
            newList.append(i)
             
    lst = newList
     
    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", lst)   
     
    return newList
 
list = ["Red", "Pink", "Black"]

word = "Pink"
N = 2
RemoveIthWord(list, word, N)
 
## 14. Python | Ways to find length of list
## 1.way inbuilt function len()
list1=[100,54,28,89,354,8]
print(list1)
print("The length f list is :=",len(list1))
##2.way whout inbuilt function
l1=["Apple","Orenge","watermilon","Cherry"]
print(l1)
count=0
for i in l1:
    count+=1
print("Length of list is:=",count)

## 15.Python | Ways to check if element exists in list
## 1,way
l1=['a','m','s','h','k']
print(l1)
for i in l1:
    if 'm' in i:
        print(i,"Element is present in list")
    else:
        pass
print()
## 2.way
lst=["Apple","Orenge","watermilon","Cherry"]
print(lst)
for i in lst:
    if "A" in i:
        print(i,"Element present in list")
    else:
       pass
print()

## 3.way
list1= [[1, 2, 5, 10, 7],
        [4, 3, 4, 3, 21],
        [45, 65, 8, 8, 9, 9]]
find_ele=8
find_ele1=0
res1=any(find_ele in sublist for sublist in list1)
res2=any(find_ele1 in sublist for sublist in list1)
print(res1,'\n',res2)
## 4.way comprehension
l2=['a','b','c','d']
print(l2)

res=[x for x in l2 if 'a' in x]
print("Yes it is present:",res)

## 16.Different ways to clear a list in Python
## 1.way by using clear
l1=['a','m','s','h','k']
print(l1)
l1.clear()
print(l1)
## 2.way by using del 
l2=[10,20,30,40,50]
print(l2)
del l2[::]
print(l2)
## 3.way using *
l3=['a','b',1,2,3]
print(l3)
l3*=0
print(l3)

## 17. Python | Reversing a List Python
lst=['Python','Java','C++','Data engg']
print("Original list:=",lst)
lst.reverse()
print("Reverse list:=",lst)

##2.way  slicing
l1=[100,123,2+5j,5.6,'m']
print("Before reverse list",l1)
print("After reverse list:=",l1[::-1])

## 3.way
l2=[125,500,200,400,100]
print("list:=",l2)
for i in range(len(l2)-1,-1,-1):
    print(l2[i],end=' ')
print()

## 4.way
list1=[11,9,3,22,31,20,5,10]
print("list1=",list1)
count=1
lst=[]
for i in range(len(list1)):
    lst.append(list1[len(list1)-count])
    count+=1
print("Reverse list:=",lst)
print()
## 18.Cloning or Copying a list Python.
# 1.way
l1=[11,12,13,14,15]
print("original list:=",l1)
l2=l1.copy()
print("Copy list:=",l2)

#2.way
def cloning(l2):
    l3=l2[:]
    return l3

l2=['Madhuri',['Anant','Sonali'],'komal','Swara']
print("original list:=",l2)
print("cloning list:=",cloning(l2))

## 2.way
def cloning_list(l1):
    new_list=[]
    new_list.extend(l1)
    return new_list
l1=[0,1,1,2,3,2,3]
print("Original list",l1)
print("cloning list:=",cloning_list(l1))

## 19. Count occurrences of an element in a list
list1=['Python','Java','C++','Data engg']
def count_ele(list1):
    count=1
    for i in list1:
        if i !=count:
            count+=1
        else:
            pass
    return count
print("count of element in list are:=",count_ele(list1))

## 20.Python program to find sum of elements in list
def sum_list(lst):
    sum1=0
    for i in lst:
        sum1=sum1+i
    print("sum of list:=",sum1)
lst=[31,22,23,5,20,28]
print(lst)
sum_list(lst)
## 2.way
l1=[10,20,30,40,50]
print(l1)
print("sum of list",sum(l1))

## 21.Python | Multiply all numbers in the list
lst=[5,10,15,20]
print(lst)
mul=1
for i in lst:
    mul=mul*i
print("Multiply all members in list:",mul)

## 22.Python program to find smallest number in a list
list1=[100,45,76,2,3,31,22]
print("Original list:=",list1)
smallest=100
for i in list1:
    if i<smallest:
        smallest=i
print("Smallest number in list:=",smallest)

## 2.way
l1=[31,22,28,3,5,10]
print(l1)
print("minimum number in list:=",min(l1))
    
## 23. Python program to find largest number in a list
list1=[100,45,76,2,3,31,22]
print(list1)
largest=100
for i in list1:
    if i>largest:
        largest=i
print("Largest number in a list:=",largest)

## 2.way
l2=[90,45,34,200,77,12]
print(l2)
print("largest number is:=",max(l2))

## 24.Python program to find second largest number in a list 
lst=[7,9,11,4,1,23,45]
print(lst)
sec_large=7
for i in range(2,len(lst)):
    if i>sec_large:
        i=lst[i]-1
        sec_large=i
print(sec_large)

## 25. Python program to print even numbers in a list
lst=[3,2,4,11,13,45,66,22,31]
print("Originallist:",lst)
l=[]
for i in lst:
    if i%2==0:
        l.append(i)
print("even number in list:=",l)

## 2.way
l1=[90,34,33,87,90,56,78,43,34,56]
print("Original list:=",l1)
l2=[x for x in l1 if x%2==0]
print("Even number in list:=",set(l2))

## 25. Python program to print even numbers in a list
lst=[3,2,4,11,13,45,66,22,31]
print("original list:=",lst)
l1=[]
for i in lst:
    if i%2==1:
        l1.append(i)
print("Odd numbers in list:=",l1)

## 2.way
l4=[2,3,7,9,11,13,2,7,11,9]
print("list:=",l4)
l5=[x for x in l4 if x%2==1]
print("Odd number in list :=",set(l5))

## 27. Python program to print all even numbers in a range 
l1=[]
for i in range(1,20):
    if i%2==0:
        l1.append(i)
print("Even number range between 1 to 20 are:=",l1)
        
## 2.way
t=(x for x in range(1,22) if x%2==0)
for i in t:
    print(i,end=' ')
print()

## 28. Python program to print all odd numbers in a range
t1=[]
for i in range(1,20):
    if i%2==1:
        t1.append(i)
print("Odd numbers range between 1 to 20 are:=",t1)

##2.way
t2=(x for x in range(1,22) if x%2==1)
for i in t2:
    print(i,end=' ')
print()

## 29. Python program to count Even and Odd numbers in a List
list1=[9,8,8,1,6,5,2,8,4,7]
print("list1:=",list1)
even_count=0
odd_count=0
for i in list1:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Count even numbers in list:=",even_count)
print("Count odd numbers in list:=",odd_count)

## 30. Python program to print positive numbers in a list
list2=[1,-5,-2,7,8,9,11,-3,-6]
print("list2:=",list2)
l3=[]
for i in list2:
    if i>0:
        l3.append(i)
print("Positive number in list:=",l3)

## 2.way
l5=[22,31,-34,-8,-5,67,1,-3,23]
print("l5",l5)
positive=[x for x in l5 if x>0]
print("positive number:=",positive)

## 31. Python program to print negative numbers in a list
list3=[-9,-2,8,4,-6,7,-8,-11]
print("list3:=",list3)
l4=[]
for i in list3:
    if i<0:
        l4.append(i)
print("Negative number in list:=",l4)

## 2.way
l6=[1,-5,-2,7,8,9,11,-3,-6]
print("l6=",l6)
Negative=[x for x in l6 if x<0]
print("Negative number:=",Negative)

## 32. Python program to print all positive numbers in a range
positive_num=[x for x in range(-10,10) if x>0]
print("Positive number:=",positive_num)

## 33. Python program to print all negative numbers in a range 
negative_num=[i for i in range(-10,10) if i<0]
print("Negative number:=",negative_num)

## 34. Python program to count positive and negative numbers in a list 
l7=[1,-5,-2,7,-18,9,-3,-66,77]
pos_count=0
neg_count=0
for i in l7:
    if i>0:
        pos_count+=1
    else:
        neg_count+=1
print("Positive num count :=",pos_count)
print("Negative num count:=",neg_count)

## 35. Remove multiple elements from a list in Python 
list1 = [11, 5, 17, 18, 23, 50]
print("list1=",list1)
for i in list1:
    if i%2==0:
        list1.remove(i)
print("Remove multiple elements from a list:=",list1)

## 2.way
l1=[77,88,3,9,34,31,22,14]
print("l1=",l1)
l2=[x for x in l1 if x%2!=0 ]
print(l2)

## 36. Python | Remove empty tuples from a list
def remove_tuple(tuple1):
    tuple1=[t for t in tuple1 if t]
    return tuple1
tuple1=([(),'Apple','red',(""),31,(),22,'cat','Black',('',''),()])
print("tuple1=",tuple1)
print("After removing tuple in list is:=",remove_tuple(tuple1))

## 2.way
t2=([(),'Cherry','Jessa',(""),31,(),22,'Dog','Pink',('',''),()])
print("t2=",t2)
l1=[]
for i in t2:
    if i:
        l1.append(i)
    else:
        pass
print("After removing tuple in list:=",l1)

## 3.way
tup1=([(),10,23,'a','b',(""),31.22,(),()])
print("tup1=",tup1)
lst1=[t for t in tup1 if t]
print("After remove tuple=",lst1)

## 37. Python | Program to print duplicates from a list of integers

## 1.way for duplicate number in list
l1=[2,1,3,4,1,5,2,6,7,3,8,5]
l2=[]
l3=[]
for  i in l1:
    if i not in l2:
        l2.append(i)
        
    else:
        l3.append(i)
        
print("duplicate number in list",l3)
print()

## 2.way
from collections import Counter
## here this module import for counter 
list1=[31,22,5,6,31,22,9,14,10,1,1,2]
print("list1=",list1)

duplicate=Counter(list1)
print(duplicate)
list2=[i for i in duplicate if duplicate[i]>1]
print("duplicate numbers:=",list2)

## 38.Python program to find Cumulative sum of a list Break a list into chunks of size N in
l1=[10,20,30,40,50]
print("l1=",l1)
l2=[]
add=0
for i in range(len(l1)):
    add+=l1[i]
    l2.append(add)
print("cumulative sum of list:=",l2)

## 2.way by using function

def cumulative_sum(l3):
    l4=[]
    sum1=0
    for i in range(len(l1)):
        sum1=sum1+l3[i]
        l4.append(sum1)
    print("cumulative sum of list:=",l4)
l3=[1,2,3,4,5]
print("l3=",l3)
cumulative_sum(l3)

## 39.Python | Sort the values of first list using second list
def sort_list(list1,list2):
    list3=zip(list2,list1)
    z=[x for _, x in sorted(list3)]
    return z
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
print("list1=",x)
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print("list2=",y)
print(sort_list(x,y))

## que on string
## 40. Python program to check if a string is palindrome or not Reverse words in a given String in
## 1.for palindrome string
def palindrome(str1):
    if str1==str1[::-1]:
        print(str1,",Yes it is palindrome string.")
    else:
        print(str1,",No it is not palinderome string.")
(palindrome("nayan"))

#2.not palindrome
def not_palindrome(str2):
    if str2 == str2[::-1]:
        print(str2,",Yes it is palindrome string.")
    else:
        print(str2,",No it is not palinderome string.")
(not_palindrome("Madhuri"))


## 41. Python Ways to remove i’th character from string 
str1="Python Programming"
print("Originalstring:=",str1)
i=3
print("Remove i'th character:=",str1[:i]+str1[i+1:])

## 2.way
def remove_chara(str1,i):
    x=str1[:i]+str1[i+1:]
    return x
print("Remove character:=",remove_chara("India",1))
## 42. Python | Check if a Substring is Present in a Given String Find length of a string in python (4 ways).
str1="I love python programming"
print(str1)
sub_str="python"
if sub_str in str1:
    print(sub_str,",Yes sub string is present in given string.")
else:
    print(sub_str,",No sub string is not present in given string.")
## find length in python 4 ways
## 1.built in fun len
s="My name is Madhuri"
print(s)
print("Length of string is=",len(s))
## 2.way
s1="Hello Everyone"
print(s1)
count=0
for i in s1:
    count+=1
print("Length of given string is=",count)

## by using function
def find_length(s1):
    length=0
    for i in s1:
        length+=1
    print("length of string:=",length)
find_length("Madhuri")

## by using while loop
def len_find(s):
    length=0
    while s[length:]:
        length+=1
    print("length of string:=",length)
s="Madhuri Anant Burande"
print("s",s)
len_find(s)

## 43.Python program to print even length words in a string
str1="I love python programming"
print(str1)
s=str1.split(' ')
for i in s:
    if len(i)%2==0:
        print(i,end=' ')
print()
        
## 2.way by using function.
def even_len(s1):
    s2=s1.split(' ')
    for word in s2:
        if len(word)%2==0:
            print(word)
s1="I am Madhuri"
print("s1=",s1)
even_len(s1)

## 44. Python | Program to accept the strings which contains all vowels 
#s=['a','j','i','r','m','i','o']
s="madhuri burande" 
print(s)
t=('a','e','i','o','u')
print(t)
res=tuple(filter(lambda a: a if a in s else False,t))
print("Contains all vowels:=",res)

## 45. Python | Count the Number of matching characters in a pair of string
def matching_chara(str1):
    count={}
    for chr in str1:
        if chr in count:
            count[chr]+=1
        else:
            count[chr]=1
    for a,b in count.items():
        print("character {} occures {} times".format(a,b))
(matching_chara("Good"))

## 46. Python program to count number of vowels using sets in given string Remove all duplicates from a given string in Python
def count_vowels(s1):
    count=0
    a=['a','e','i','o','u']
    for i in set(s1):
        if i in a:
            count+=1
        else:
            pass
    return count
print("count number of vowels:=",count_vowels("embroidery audio"))
    
    

    
