def ispalindrome(str1):
    return str1==str1[::-1]
str1="madam"
ans=ispalindrome(str1)
if str1:
    print(str1,"is a palindrome:","yes")
else:
    print(str1,"is a palindrome:","No")    

## 2nd way
def palindrome_str(str2):
    return str2==str2[::-1]

  