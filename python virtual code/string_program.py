##que1.Write a program to create a new string made of an input string’s first, middle, and last character.
from distutils.filelist import translate_pattern
from platform import python_build


str1="Madhuri"
print(str1)
fc=str1[0]

length=len(str1)

mi=int(length//2)
fc=fc+str1[mi]

lc=fc+str1[length-1]
print(lc)

##que2.Write a program to create a new string made of the middle three characters of an input string.
str1="Madhuri"
print(str1)
str1=str1[2:5]
print(str1)

###or---
l=len(str1)
mi=int(l//2)
res=str1[mi-1:mi+2]
print(res)

##que3.Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
str1="anant"
str2="Madhuri"
print(str1,str2)
l=len(str1)
mi=int(l//2)
s=str1[:mi:]
s=s+str2
s=s+str1[mi:]
print(s)

##que4.Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
s1="python"
s2="java"
print(s1,s2)
first_char=s1[0]+s2[0]
middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
last_char=s1[len(s1)-1]+s2[len(s2)-1]
res=first_char+middle_char+last_char
print("The first,middle,last characterofs1 and s2 is:",res)

##que5.Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string 
# so that all lowercase letters should come first.
str1 = "PyTHon"
print(str1)
lower=[]
upper=[]

for char in str1:
    if char.islower():
        lower.append(char)
    
    else:
        if char.isupper():
            upper.append(char)
store_char=''.join(lower+upper)            
print(store_char)        

##que6.Count all letters, digits, and special symbols from a given string
str1 = "M@#an27at^&i5te"
print(str1)
count_lettrs=0
count_digit=0
count_symbol=0
for char in str1:
    if char.isalpha():
        count_lettrs+=1
    elif char.isdigit():
        count_digit+=1
    else:
        count_symbol+=1 
print("count of lettrs is:=",count_lettrs)   
print("count of lettrs is:=",count_digit) 
print("count of lettrs is:=",count_symbol)   

##que7.Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced 
# if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
##case 1:
s1='dh'
s2='Madhuri'
##case 2:
s1='dan'
s2='Anant'
def Balance_char(s1,s2):
    flag=True
    for char in s1:
        if char in s2:
            continue
        else:
            flag=False
    return flag
##case 1:
s1='dh'
s2='Madhuri'   
flag=Balance_char(s1,s2)
print("all the characters in the s1 are present in s2",flag)
##case 2:
s1='dan'
s2='Anant'
flag=Balance_char(s1,s2)
print("all the characters in the s1 are present in s2",flag)

##que8.Find all occurrences of a substring in a given string by ignoring the case
##Write a program to find all occurrences of “USA” in a given string ignoring the case.
str1 = "Welcome to INDIA. india awesome, isn't it?"
sub_string='INDIA'
print(str1)
temp=str1.lower()
count=temp.count(sub_string.lower())
print("all occurrences of INDIA in given string count is:=",count)

##que9.Given a string s1, write a program to return the sum 
##and average of the digits that appear in the string, ignoring all other characters.
str1 = "PYton39@#2819"
print(str1)
sum=0
count=0

for char in str1:
    if char.isdigit():
        sum+=int(char)
    count+=1
average= sum/count
print("The sum of digits is:=",sum,"and the average of digits is:=",average)   

##que10.Write a program to count occurrences of all characters within a string
s1='Programming'
print(s1)
dict_char=dict()
for char in s1:
    count=s1.count(char)
    dict_char[char]=count
print(dict_char)    

##que11.Reverse a given string
str1="Madhuri"
print(str1)

str1=str1[::-1]
print("reversed string is:=",str1,end='') 
print(' ') 

### or----
str2="i love python"
print(str2)
str2=''.join(reversed(str2))
print("After reversed string is:=",str2,end='')

##que12.Write a program to find the last position of a substring “Madhuri” in a given string.
str1 = "Madhuri is a python devloper who knows Python. Madhuri works at google."
print(str1)
index=str1.rfind("Madhuri")
print("The index of last potion of substring madhuriis:=",index)

##que13.Write a program to split a given string on hyphens and display each substring.
str1 = "Madhuri-is-a-python-developer"
print(str1)
sub_string=str1.split("-")
for sub in sub_string:
    print(sub)

##que14.Remove empty strings from a list of strings
str_list = ["Madhuri", "Jon", "", "Kelly", None, "Anant", ""]    
print(str_list)
### by using filter function.
new_list=list(filter(None,str_list))
print(new_list)

### by using if condition.
temp_list=[]
for s in str_list:
    if s:
        temp_list.append(s)
print(new_list)   

##que15.Remove special symbols / punctuation from a string
str1 = "/*Jon is @developer & musician"
print(str1)
import string
new_str=str1.translate(str.maketrans('','',string.punctuation))
print(new_str)

##que16.Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
print(str1)
for char in str1:
    if char.isdigit():
        print(char,end='')
print(' ')        

##que17.Write a program to find words with both alphabets and numbers from an input string.
str1 = "Emma25 is Data scientist50 and AI Expert"        
print(str1)
res=[]
temp=str1.split()
for item in temp:
    if any(char.isalpha() for char in item)and any(char.isdigit() for char in item):
        res.append(item)
for i in res:
    print(i)   

##que18.Replace each special symbol with # in the following string
str1 = '/*Jon is @developer & musician!!'
print(str1)    
import string
replace_char='#'
for char in string.punctuation:
    str1=str1.replace(char,replace_char)
print("After replacing char:=",str1)    