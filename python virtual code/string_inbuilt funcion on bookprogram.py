## Testing String
## 1.bool isalnum()
s="Python Programming"
print(s)
print("In string alphabetic and number are present:=",s.isalnum())

s="Python120"
print(s)
print("In string alphabetic and number are present:=",s.isalnum())

## 2.bool isalpha()
s2="helloeveryone"
print(s2)
print(s2.isalpha())

s1="Hello 1223"
print(s1)
print(s1.isalpha())

## 3.bool isdigit()
s3="python 3"
print(s3)
print(s3.isdigit())

s4='3122'
print(s4)
print(s4.isdigit())

## 4.bool islower()
s1="Madhuri Anant"
print(s1)
print(s1.islower())

s2="my namne"
print(s2)
print(s2.islower())

## 5.bool isupper()
str1="MY LAPTOP IS APPLE COMPANY"
print(str1)
print(str1.isupper())
 
str2="oo it's grate"
print(str2)
print(str2.isupper())

### bool isspace()
s=" "
print(s.isspace())

str1="iamworkinattcs company"
print(str1)
size=len(str1)
print(size)

i=1
while i<size:
    if str1[i].isspace():
        break
    i+=1
    print(str1[i],end='') 


## Searching Substring in a String
## 1.bool endswith(str Str1)
str1="Python programming"
print(str1)
print(str1.endswith("programming"))
print(str1.endswith("python"))
      
## 2.bool startswith(str Str1)
str2="name Madhuri"
print(str2)
print(str2.startswith("name"))   
print(str2.startswith("madhuri"))  

## 3.int find(str Str1) 7#Returns the index from where the string “Prog”begins or find index[] of string
s1="Madhuri is python developer"
print(s1)
print(" index of Madhuri is:=",s1.find("Madhuri"))
 
## 4.int rfind(str Str1) #Returns the index of last occurrence of string “o”in Str1
str2="Madhuri is python developer"
print(str2)
print("The index of o is:=",str2.rfind('o'))

## 4.int count(str S1)
s="Good afternoon "
print(s)
print("Total count of o present in string is:=",s.count('o'))

## Methods to Convert a String into Another String
## 1.str capitalize()  #Convert first alphabet of String Str1 to uppercase
s="hello"
print(s.capitalize())

## 2.str lower()   #convrt all upper latters into lowercase
s1="INDIA"
print(s1.lower())

## 3.str upper() ##conver all small letters into  upper
s2="anant"
print(s2.upper())

## 4.str title() ## each word start with capital letter
s5="welcome to the world of programming"
print(s5)
print(s5.title())

## 6.str swapcase() it converts upper to lower and lower to upper 
str1="IncreDible India"
print(str1)
print(str1.swapcase())

## 7.str replace (str old, str new [,count])  ###Replace the old string i.e “two” by new string i.e.“three”.
s1="I have brought two chocolates, two cookies and two cakes"
print(s1)
print(s1.replace("two","three"))
print(s1.replace("two","three",2))  

##Stripping Unwanted Characters from a String 
## 1.str lstrip()   #Remove left white space characters
s=" Hey Cool!!!"
print(s)
print(s.lstrip())

s1="\t\tHey Cool!!."
print(s1)
print(s1.lstrip())

## 2.str rstrip() #Remove trailing white space character
str1="Welcome!!!\n\n\ "
print(str1)
print(str1.rstrip())

## 3.str strip() # bothside remove whote space and tab
str2=" Hello Eveyone Wlcome to python wold\t\t "
print(str2)
print(str2.strip())

str3='@Cost Prize of Apple Laptop is at Rs = 20 Dollars $$$$'
print("before strip function")
print(str3)
print("After strip function")
print(str3.strip('@$'))

## Formatting String
## 1.str center(int width)  we get width 
m="APPLE MACOS" 
print(m)
print(m.center(15))

##2.str ljust(int width) #Place the string S1 at the left of a string with 15 characters.
a="Hey Cool!!"
print(a)
print(a.ljust(15))

##3.str rjust(int width) #Place the string S1 at the right of a string with 15 characters.
b="wlcome to pune"
print(b)
print(b.rjust(15))

