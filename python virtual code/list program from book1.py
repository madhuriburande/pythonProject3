##que1.Write a program to create a list with elements 1,2,3,4 and 5. Display even elements of the list using list comprehension.
## even numbers of list
l1=[1,2,3,4,5]
print(l1)
l1=[x for x in l1 if x%2==0 ]
print("even number of list is=",l1)

## square of list
l2=[1,2,3,4,5]
print(l2)
l2=[x*x for x in l2]
print("The square of list is=",l2)

### or--
l3=[x*x for x in range(1,11)]
print("The square of first 10 number is")
print(l3)

l4=[x**3 for x in range(1,11)]
print("The cube of first 10 number is")
print(l4)

## que2.Consider a list with fi ve different Celsius values. Convert all the Celsius values into Fahrenheit. 
Celsius=[10,20,31.3,40,39.2]
print(Celsius)
print("Celsius to Fahrenheit Conversion")
Fahrenheit=[ ((float(9)/5)*x + 32) for x in Celsius]
print(Fahrenheit)
### formula of Fahrenheit = (9/5) * Celsius + 32

##que3.Consider the list with mixed type of elements, such as L1 = [1,’x’,4,5.6,’z’, 9, ‘a’, 0, 4]. Createanother list using list 
# comprehension which consists of only the integer element present within the list L1.
L1 = [1,'x',4,5.6,'z', 9, 'a', 0, 4]
print(L1)
z=[x for x in L1 if type(x) == int]
print(z)

##LIST METHODS
## 1. append(object x)
list1=['x','y','z']
print(list1)
list1.append('A')
print(list1)

##Note: Append method is equivalent to doing:
 ##List1[len(List1):]=[Element_Name]
list2=['Red','Blue','Black','Pink']
list2[len(list2):]=['yellow']
print(list2)

l5=[10,20,30,40]
print(l5)
l5[len(l5):]=[111]
print(l5)

## 2.clear()
list1=['x','y','z']
print(list1)
list1.clear()
print(list1)

##3.int count(object x) Count the number of times the element ‘x’ has appeared in the list 
list2=['Red','Blue','Black','Pink','Red','Blue']
print(list2)
print("The count of red present in ",list2.count("Red"),"times")

## 4.List copy()
list1=['x','y','z']
list2=list1.copy()
print(list2)

##Note: Copy() Method is equivalent to doing
##List2=List1[:] # Copies the content of List1 to List2
list1=['Red','Blue','Black','Pink']
list2=list1[:]
print(list2)

##5.extend(list L2)
l1=[1,2,3]
l2=[4,5,6]
print(l1,'\n',l2)
l1.extend(l2)
print(l1)

l3=['a','d','r','t']
l4=['e','o','p','w']
print(l3,'\n',l4)
l3.extend(l4)
print(l3)

## 6.int index(object x)
l3=['a','d','r','t']
print(l3)
print("The index of d is:=",l3.index('d'))
print("The index of t is:=",l3.index('t'))

## 7.insert(int index,Object X)
lis1=[10,20,30,40,60]
print(lis1)
lis1[2]='anant'
print(lis1)

##8.Object pop(i) # the element pop by indexwise
l1=[2,4,6,8,10]
print(l1)
l1.pop(4)
print(l1)

l2=['madhuri','komal','ankita','swara','harshada']
print(l2)
l2.pop(0)
print(l2)

##Lis1.pop() at the last elelmnet is pop only
l3=[1,2,3,3,4,55]
print(l3)
l3.pop()
print(l3)

### None remove(object x)
l4=['chocklet','cake','cookies','cadbary']
print(l4)
l4.remove('cookies')
print(l4)

##None reverse()
l5=['chocklet','cake','cookies','cadbary']
l5.reverse()
print(l5)

##None sort() 
l6=[4,6,2,1,8,9,22,31]
print(l6)
l6.sort()
print(l6)

### LIST AND STRINGS
p='Python'
print(p)
l1=list(p)
print(l1)

### SPLITTING A STRING IN LIST
A="Wow!!! I Love Python Programming"
print(A)
print(A.split())

##PASSING LIST TO A FUNCTION
def l1_fun(l2):
    for num in l1_fun:
        print(num,end=' ')
l2=[10,30,50,70,80] 
print(l2)

