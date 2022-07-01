## basic inbuilt function for string.
a='Python'
print(a)
print(len(a))
print(max(a))
print(min(a))

B="Madhrui anant burande"
print(B)
print(len(B))
print(max(B))
print(min(B))

###  python index[] oprator
p='Python is high levle langauage'
print(p)
print(len(p))
print("0th index of string is",p[0])
print("negative or last index of string is",p[-1])
print(p[-5])

###TRAVERSING STRING WITH for AND while LOOP
s1="India is beautyfull country"
for char in s1:
    print(char,end='')

##que.Write a program to traverse every second character of a string using the for loop.
s="ILOVEPYTHONPROGRAMMING"
print(s)
for char in range(0,len(s),2):
    print(s[char],end=' ')
    
    
##que.Write a program to traverse all the elements of a string using the while loop.     
s="Madhuri "
index=0
while index<len(s):
    print(s)
    index+=1
    break
##MMUTABLE STRINGS
##s="i love Mango"
#print(s)
#s['Mango']='Apple'
#print(s)  ######## it gives the bocouse string is immutable 

##Note: If you want to change the existing string, the best way is to create a new string that is a
##variation of the original string.
s1="i love Mango,"
print(s1)
s2=s1[::]+"Apple"
print(s2)

##str1 and str2 refers to the same string object, whereas str1 and str2 have the same ID number.
str1="Hello"
str2="Hello"
print(str1,str2)
print(id(str1))
print(id(str2))

##The String Slicing Operator [start: end]
str1="IIT Bombay"
print(str1)
print(str1[4:10])
print(str1[:3])

##String Slicing with Step Size
str1="IIT Bombay"
print(str1)
for char in range(0,len(str1),2):
    print(str1[char],end='')


##Some More Complex Examples of String Slicing     
str1="i love danceing"
print(str1[::])  ### print hole sttring
print(str1[::-1]) ## reverse string
print(str1[2:6])
print(str1[-1:0:-1])

###The String +, * and in Operators 
s1="madhuri"
s2="Anant"
print(s1+s2)
print(s1*2) 

### the in and not in oprator
##que.Write a program to print all the letters from word1 that also appear in word2.
word1 = "USA North America"
word2= "USA South America"
for char in word2:
    if char in word1:
        print(char,end='')

s1="python programming"
s2="java programming"
print(s1)
print(s2)

if "java" in s1:
    print(" java is present in s1")
else:
    print("java s not present ins1")

s1="team brain works"  
s2="team brain works class"   
print(s1)
print(s2)
if "team brain"in s2:
    print("Yes,team brain  is present in s2")
else:
    print("No,team brain  is not present in s2")    


###String Comparison
s1="abcd"  ### ir comair with Ascci value i.e A_z=65-90 and a-z=97-122
s2="ABCD"
print(s1>s2)
print(s1<s2)
print(s1==s2)

str1="ABC"
str2="def"
print(str1<str2)
print(str1>str2)

s1="ABC"
s2="SDF"
print(s1==s2)

a="mab"
b="mab"
print(a==b)

###The String .format() Method()
##way 1
print("My Name is %s and I am from %s"%("JHON","USA"))
print("My name is %s and i from %s"%("Madhuri","Pune"))
##way 2
print('{} and {} equals to {}'.format(4,5,9))
#num=int(input("Enter the number"))
num=22
if num%2==0 :
        print('{} is even number'.format(num))
else:    
        print("{} is odd number".format(num))

## Keyword Argument and format() Method
print("I am {0}  and I love work on {pc} laptop".format("Madhuri",pc="Apple"))

##The split() Method
s="python,java,c,c++,dotnet"
s.split()
print(s,end='')


TOP_10_Company="TCS,INFOSYS,GOOGLE,MICROSOFT,YAHOO"
Company=TOP_10_Company.split(",")
print(Company)
for c in Company:
 print(end="")
 print(c)


 



