## ACCESSING THE ELEMENTS OF A LIST +ve and -ve 
l1=[10,20,30,'a','b','c']
print(l1)
print(l1[4])
print(l1[-4])

## LIST SLICING [START: END:step]
l2=[10,20,30,40,50]
print(l2[::])

print(l2[1:4])

l3=[1,2,3,4,5]
print(l3)
print(l3[-3:-1])

MyList1=["Hello",1,"Monkey",2,"Dog",3,"Donkey"]
print(MyList1)
for i in range(0,len(MyList1),2):
    print(MyList1[i])

l1=['python',120,'java',90,'c++',92]
print(l1)
print(l1[0:6:3])

#Display List in Reverse Order
l2=['python',120,'java',90,'c++',92]
print(l2[::-1])
l3=[10,20,30,40,60]
l3.reverse()
print(l3)

#Start index with -1 and End Index with 0 and step Size with -1
l4=[10,20,30,40,60]
l4[-1:0:-1]
print(l4)

##PYTHON INBUILT FUNCTIONS FOR LISTS 
list1=['red','black','blue','white']
print(list1)
print(len(list1))
print(max(list1))
print(min(list1))

#Create a List, and Shuffle the elements in random manner
l1=[10,20,30,40,50]
print(l1)
import random
random.shuffle(l1)
print(l1)

#Create a List, and find the sum of all the elements of a List.
list2=[10,20,30,40,50]
print(list2)
print(sum(list2))

##THE LIST OPERATOR
l1=[1,2,3,4]
l2=[6,7,8]
print(l1+l2)
l3=[l2*2]
print(l3)

##The in and not in  Operator:
list2=[10,20,30,40,50]
print(30 in list2)
l3=['m','a','s','p','k']
print(l3)
print(" k is present in list=",'k' in l3)
print("l is present in list=",'l' in l3)

##The is and is not Operator:
l1=['a','b','c']
l2=['A','B','C']
print(l1,'\n',l2)
print(l1 is l2)
print(l1 is not l2)

l3=['a',1,'b',2,'c',3]
l4=['a',1,'b',2,'c',3]
print(l3,'\n',l4)
print(l3 is l4)
print(id(l3))
print(l3 is not l4)
print(id(l4))

A="Microsoft"
B="Microsoft"
print(A,'\n',B)
print(A is B)

##The del Operator:
l3=['a',1,'b',2,'c',3]
print(l3)
del l3[3]
print(l3)

l1=[10,20,30,'a','b','c']
print(l1)
del l1[2:4]
print(l1)
del l1[:]
print(l1)

##LIST COMPREHENSIONS
l1=[1,2,3,4,5]
l1=[x+10 for x in l1 ]
print(l1)

l2=[10,20,30,40,50]
print(l2)
l2=[a-5 for a in l2]
print(l2)

l3=[40,50,60,70]
print(l4)
l3=[x/5 for x in l3]
print(l3)

l4=[1,2,3,4,5]
print(l4)
l4=[z*2 for z in l4]
print(l4)
