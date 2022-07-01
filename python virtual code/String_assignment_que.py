## 1.Python program to check if a string is palindrome or not
def Palindrome(str1):
    return str1==str1[::-1]

print("is it palindrome:=",Palindrome("nayan"))

## or 
def palindrome_str(s):

    rev=''.join(reversed(s))
    if s==rev:
        print("Yes, It is plaindrome string")
    else:
        print("No,it is not palindrome")  

palindrome_str("nayana")  

## 2.Python program to check whether the string is Symmetrical or Palindrome
str2="amaama"
print(str2)
half=int(len(str2)/2)

if len(str2)%2==0:
    first_str=str2[:half]
    second_str=str2[half:]

else:
    first_str=str2[:half]
    second_str=str2[half+1:]
## for semmentrical string
if first_str==second_str:
    print("Yes,it is a symmentrical")
else:
    print("No,it is not symmentrical") 
## for palindrom string
def palindrome_s(str2):
    res=''.join(reversed(str2))
    if res==str2:
        print("Yes,it is plaindrome")
    else:
        print("No,it not palindrom")

palindrome_s(str2)

## 3.Reverse words in a given String in Python
string1="i love python programming "
print(string1)
result=string1.split()[::-1]
print(result)

## 4.Ways to remove i’th character from string in Python
## remove pos=4
str1="Madhuri Anant Burande"
print("The original string is:",str1)
new_str=''.join([str1[i] for i in range(len(str1))if i!=3])
print("Removeing i'th character of string:",new_str)

## 5.Check if a Substring is Present in a Given String
string="I love dancing"
print(string)

if "love" in string:
    print("Love is prsent in string.")
else:
    print("Not present")

## 6.Python – Words Frequency in String Shorthands
def frequency_char(str1):
    count={}
    for chr in str1:
        if chr==' ' or chr=='\t':
            continue
        if chr in count:
            count[chr]+=1
        else:
            count[chr]=1
    for a,b in count.items():
        print("character {} occurrs {} times".format(a,b))
frequency_char("Good")

## 7.Python – Convert Snake case to Pascal case
test_str = 'geeksforgeeks_is_best'
result=test_str.replace("_"," ").title().replace(" "," ")
print(result)
print()

## 8.Find length of a string in python (4 ways)
## 1 way
str1="madhuri"
print(str1)
count=0
for i in str1:
    count+=1
print("the lenth of string is:=",count)
print()

## 2, way but here lenth of words
str2="python is high level language"
print(str2)
res=str2.split()
print("The length of string is:=",len(res))
print()

## 3rd way
def findlen_str(str3):
    count=0
    for i in str3:
        count+=1
    print("The lenth of string is:",count)

findlen_str("Python")   

## 4'th way
def find_len(str4):
    count=0
    while str4[count:]:
        count+=1
    print("the length of string:=",count)
find_len("Anant")   

## 9.Python program to print even length words in a string
n="This is a python language"
print(n)
s=n.split(" ")
for i in s:
    if len(i)%2==0:
       print(i)

## or---

def print_evenwords(s):
    s1=s.split(' ')
    for word in s1:
        if len(word)%2==0:
            print(word)
print_evenwords("i am madhuri")        

## 10.Python program to accept the strings which contains all vowels
#vowels meanse=(aeiou)
def check(string):
    if len(set(string.lower()).intersection("aeiou"))>=5:
        return ('assepted')
    else:
        return ('Not assepted')

if __name__=='__main__':
    string="SEEquoiaL"
    print(check(string))

def check (string):
    if len(set(string.lower()).intersection("ariou"))>=5:
        return ('assepted')
    else:
        return ('Not assepeted')
if __name__=='__main__':
    string='SEEquoial test'
    print(check(string))

## 11.Python | Count the Number of matching characters in a pair of string.
def count_match(str1,str2):
    count=1
    for i in str1:
        for j in str2:
            if i==j:
                count+=1
            else:
                continue
    return count            

str1="Madhuri@#3122" 
str2="Anant$$&*2214" 
print("Matching chara count is:=",count_match(str1,str2))  

## 12.	Remove all duplicates from a given string in Python.
def duplicate_remove(str1):
    duplicate_str=set(str1)
    print("Remove duplicate string is:=",duplicate_str)
duplicate_remove("aabcddeff") 

## 13.Python – Least Frequent Character in String

def frequent_chara(string1):
    count={}
    for chr in string1:
        if chr==' ' or chr=='\t':
            continue
        elif chr in count:
            count[chr]+=1
        else:
            count[chr]=1
    for k,v in count.items():
        print("chara {} occurrs {} times".format(k,v))
frequent_chara("Good") 

## 14.Python | Maximum frequency character in String
freq_chara={}
string2="Good morning"
for chr in string2:
    if chr==' ' or chr=='\t':
        continue
    elif chr in freq_chara:
        freq_chara[chr]+=1
    else:
        freq_chara[chr]=1
print("Maximun frequency character is := ",max(freq_chara,key=freq_chara.get))

## 15.Python | Program to check if a string contains any special character.
string="Madhuri#@$%^&*31"
#string.split()
count=0

s=("@#$%^&*!")
for i in range(len(string)):
    if string[i] in s:
        count+=1
if count:
    print("string is not accepeted") 
else:
    print("string is accepted")   

## 16.Generating random strings until a given string is generated

## 17.Find words which are greater than given length k
str1= "love python programming "
str1.split()
k=4
count=1
for i in range(len(str1)):
    if i==' ' or i=='\t':
        continue
    elif i>k:
        print(str1[i],end=' ')
        count+=1
print()
print()

## 18.	Python program for removing i-th character from a string
str1="Madhuri Burande"
print("Original string is:",str1)
new_str=" "
for i in range(len(str1)):
    if i!=2:
        res=str1[i]+new_str
        print(res,end='')
print()

## 19.Python program to split and join a string.
str1="Hello every one, i am Madhuri"
print(str1.split(" "))
print('-'.join(str1.split()))

## 20.Python | Check if a given string is binary string or not
def str_bin(str1):
    count=1
    binary='01'
    for chr in str1:
        if chr not in binary:
            count+=1
            break
        else:
            pass
    if count:
        print("Yes it is binary string:=",str1)
    else:
        print("No only string",str1)
str_bin("madhuri00111")

## 21.Python program to find uncommon words from two Strings
a={"Apple","Banana","Cherry"}
print("Original string:",a)
b={"Banana","Cherry","kivi","Mango"}
print("Original string:",b)
res=a.symmetric_difference(b)
print("Uncoomon word from two strings:",res)

#### or--
def check_uncommon(a,b):
    res=set(a).symmetric_difference(set(b))
    print("Uncommon word in string:",res)
a=["Red","Black","Blue"]
print("Original string:",a)
b=["Yellow","Black","Pink"]
print("Original string:",b)
check_uncommon(a,b)
