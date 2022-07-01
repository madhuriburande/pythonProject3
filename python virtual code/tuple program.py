my_tuple=(11,24,56,88,78)
print(type(my_tuple))
print(my_tuple)

t1=tuple("Madhuri")
print(t1)

## inbuilt functions
tuple=("Madhuri is good devolper")
print(tuple)
print(len(tuple))

t1=(31,22,14,96,89)
print(max(t1))
print(min(t1))

t2=(22,31)
t3=(14,23)
print(sum(t2+t3))
###reverse
t4=('madhuri','anant','komal','swara')
print(t4)
print(t4[1])
print(t4[-1])

count=1
sum=0
for i in range(1,10):
    if i%2==0:
        print("Even number is:=",i)
        sum=sum+i
        print("sum of even number is:=",sum)
        count+=1
        
##que2.Access value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

##que3.Create a tuple with single item 50
tuple=(50)
print(tuple)

##que4.Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a,b,c,d=tuple1
print('a=',a,'b=',b,'c=',c,'d=',d)

##que5.Swap two tuples in Python
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print("tuple2=",tuple2)
print("tuple1=",tuple1)

t1=('a','b','c')
t2=('x','y','z')
t1,t2=t2,t1
print("t2=",t2)
print("t1",t1)

##que6.Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[-3:-1]
print(tuple2)

t1=("madhuri","anant","swara","komal")
t2=t1[1:]
print(t2)

##que7.Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
tuple1 = (11, [22, 33], 44, 55)
print(tuple1)
tuple1[1][0]=222
print(tuple1)

##que9.Counts the number of occurrences of item 50 from a tuple
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

##que10. Check if all items in the tuple are the same
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))


def check(t1):
    return all(i== t1[0] for i in t1)
tuple=('madhuri','anat')
print(check(tuple2))

# nested tuple
t1 = ("mouse", [8, 4, 6], (1, 2, 3))
print(t1)
print(t1[0])
print(t1[0:6:2])
print(t1[-1][-2])
t1[1][2]=9    #####note -in tuple we can't change value but in tuple list present then we can change
print(t1)

###concative tuple by using oprator(+,*)
t1=(1,2,3,4)
t2=(5,6,7)
print(t1+t2)
print(t2*2)
#### tuple membership oprator(in and not in)
tuple=('madhuri','anant','komal')
print('madhuri' in tuple)

t1=(1,2,3,4)
print(1 in t1)




##Write a program to traverse tuples from a list.
tuple=[(1,'Mahuri',2,'Anant',3,'Python')]
for name in tuple:
    print(name,end=' ')
#### zip function
l1=[1,2,3,4]  
l2=['a','b','c','d'] 
for i in zip(l1,l2):
    print(i) 

l1=['red','black','blue']
l2=[10,20,30] 
for i in zip(l1,l2):
    print(i)  

### inverse zip function
x=[('Apple',100000),('Dell',50000)]
laptop,price=zip(*x)
print(laptop)
print(price)

matrix=[(1,2),(3,4),(5,6)]
print(matrix)
x=zip(*matrix)
print(x)

###Consider an example of a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers
##present at odd index into a new tuple.
def addtuple(atup):
    rtup=()
    index=0
    while index< len(atup):
        rtup+=(atup[index],)
        index+=2
    return rtup
t=(1,3,2,4,6,5)  
print(addtuple(t))     