## programs on regex(regular expresion)
# Find digits in string
import re
# s="My roll number is 25"
# res=re.findall(r'\d',s)
# print(res)

# ## --------------------------------------1.compile ---------------------------------------##
# s1="Madhuri 3122"
# st=r"\d{4}"
# res1=re.compile(st)
# # print the type of compiled pattern
# print(type(res1))
# # find all the matches in string one
# print(res1.findall(s1))
#
# ##----------------------------------- 2.re match ---------------------------------------##
# str1="Emma is a basketball player who was born on June 17"
# result=re.match(r"\w{4}",str1)
# print("Find 4 char word in string:=",result)

# s1="Jessa and Kelly"
# ans=re.match(r'\b\w{5}\b',s1)
# print("match only first=",ans)  ## match only match the begining of string and show .fisrt show in only string
# print(ans.start())  ## it show the index of sring when it match .

# # -------------------------3.re.search---------------------------------------##
# s1="I love python programming since 1991"
# ans=re.search(r"\d{4}$",s1)
# print("show digits in string",ans)
# s2="Hello Every one @#$%"
# res1=re.search(r'\W{5}',s2)   ## search search the string,chara,special chara also it shows the space of between two strings.
# print(res1)

#s3="I love python and django"
# output=re.search(r'\w{7}',s3)
# print(output)
# print(output.group())

# # Target String
# target_string = "Emma is a baseball player who was born on June 17"
# # search() for eight-letter word
# result = re.search(r"\w{8}", target_string)
# # Print match object
# print("Match Object", result)
# # output re.Match object; span=(10, 18), match='baseball'
# # print the matching word using group() method
# print("Matching word: ", result.group())
# # Output 'baseball'

# ----------------------4.re.findall---------------------------------------##
# s3="I love python and django"
# op=re.findall(r'\w{6}',s3)
# print(op)
#
# ans=re.findall(r'python',s3)
# print(ans)
#
# sr="Emma 12 25"
# print(re.findall(r'\d+',sr))
#
# str1 = "a3c5d10hgjdfhjs2345d5d67zdd78f7888732hb"
# print(re.findall(r'\d+',str1))   ## d+ it show the oput like 2,5,2345 etc

# str2 = "Hello #Jessa!@#$%"
# print(re.findall(r'\W',str2))

## difference between match and search.
#target_string = "Emma is a baseball player who was born on June 17, 1993"

# Match 2-digit number
# # Using match()
# result = re.match(r'\d{2}', target_string)
# print(result)
# # Output None
#
# # Using search()
# result = re.search(r'\d{2}', target_string)
# print(result.group())

## 5.---------------------------------------re.sub---------------------------------------##

# str1=" Jessa knows testing and machine learning \t"
# print(re.sub(r'\s','-',str1)) ## here space replace the - in string.
# print(re.sub(r'\s+','',str1))  ## removing space between two string.
# print(re.sub(r'^\s+','',str1)) ##  ^=remove only space or gievn pattern
# print(re.sub(r'^\s+|\s$','#',str1))
# s="Madhuri@#%&"
# print(re.sub(r'@#%&','****',s,))
#
# s1="My Name is Madhuri"
# print(re.sub(r'\s','-',s1,count=2))
# replacement function to convert uppercase word to lowercase
# and lowercase word to uppercase
# def convert_case(match_obj):
#     if match_obj.group(1) is not None:
#         return match_obj.group(1).lower()
#     if match_obj.group(2) is not None:
#         return match_obj.group(2).upper()
#
# # Original String
# str = "EMMA loves PINEAPPLE dessert and COCONUT ice CREAM"
#
# # group 1 [A-Z]+ matches uppercase words
# # group 2 [a-z]+ matches lowercase words
# pass replacement function 'convert_case' to re.sub()
#res_str = re.sub(r"([A-Z]+)|([a-z]+)", convert_case, str)

# String after replacement
#print(res_str)
# Output 'emma LOVES pineapple DESSERT AND coconut ICE cream'

## 6.----------------------------------------re.subn------------------------------------#3

import re

target_string = "Emma loves PINEAPPLE, COCONUT, BANANA ice cream"
result = re.subn(r"[A-Z]{2,}", "MANGO", target_string)
print(result)
# Output ('Emma loves MANGO, MANGO, MANGO ice cream', 3)

s="Madhuri loves APPLE,PINEAPPLE,CHERRY,STRWABERY and ice cream."
print(re.subn(r'[A-Z]{2,}','MANGO',s))