##que1.Write a function histogram that takes string as parameter and generates a frequency of characters contained in it.
 #S = “AAPPLE” The program should create a dictionary
 #D = {‘A’: 2, ‘E’: 1, ‘P’: 2, ‘L’: 1}
from msilib.schema import Binary


def count_char(s):
    d1=dict()
    for char in s:
        count=s.count(char)
        d1[char]=count
    return d1
s="Aapple"
print(s)
print(count_char(s))    

### or----
def histogram(s):
    d2=dict()
    for char in s:
        if char not in d2:
            d2[char]=1
        else:
            d2[char]=d2[char]+1
    return d2
s="madhuri"
print(s)
print(histogram(s))

##que2.Write a program to count the frequency of characters using the get() method
def Histogram(a):
    D=dict()
    for c in a:
        if c not in D:
            D[c]=1
        else:
            D[c]=D.get(c,0)+1
    return D

a="programming"
print(a)
print(Histogram(a))    

##que3.Write a program to print and store squares of numbers into a dictionary
def Square_num(n):
    D=dict()
    for i in range(1,n+1):
        if i not in D:
            D[i]=i*i
    return D
n=10
print('square of number n:=',n)
print(Square_num(n))    

##que4.Write a program to pass a list to a function. Calculate the total number of positive and negativenumbers from the list and 
# then display the count in terms of dictionary.Input: L=[1,-2,-3,4] Output: {‘Neg’: 2, ‘Pos’: 2}
def Pov_Neg(l):
    d=dict()
    d['positive']=0
    d['negative']=0
   
    for i in l:
        if i>0:
            d['positive']+=1
        else:
            d['negative']+=1
    return d
l=[1,2,3,-4,-5,6]
print(Pov_Neg(l))   

##que5.Write a program to convert an octal number into binary.
def convert_oct_bin(number,table):
    Binary=' '
    for digit in number:
        Binary=Binary+table[digit]
    return Binary
octToBinaryTable={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'100','6':'110','7':'111'}
print("The binary number is:=",convert_oct_bin('534',octToBinaryTable))        

       



    