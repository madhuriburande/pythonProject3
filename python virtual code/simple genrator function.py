def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


# Using for loop
for item in my_gen():
    print(item)

## reverse string by using genrator
def reverse_str(str1):
    size=len(str1)
    for i in range(size-1,-1,-1):
        yield str1[i]
for chr in reverse_str("hello"):
    print(chr,end=' ')
print()
### reverse string another example
def rev_str(str2):
    size=len(str2)
    for i in range(size-1,-1,-1):
        yield str2[i]
for chr in rev_str("madhuri"):
    print(chr,end=' ')            
print()

### program for frequency of char present in string
def count_char(str3):
    count={}
    for chr in str3:
        if chr==' ' or  chr=='\t':
            continue
        if chr in count:
            count[chr]+=1
        else:
            count[chr]=1    
    for a,b in count.items():
        print("character {} occurs {} times".format(a,b))       

count_char("Good boy Anant")

## write  frogram for square by using genrator.
l1=[1,2,3,4,5]
print(l1)
a=(x**2 for x in l1)
print("The square is:=", next(a))
print("The square is:=",next(a))
print("The square is:=",next(a))
print("The square is:=",next(a))
print("The square is:=",next(a))
print("The sumof all square numbers in listis:=",sum((x**2 for x in l1)))
print("The maximum number of square of list is:=",max((x**2 for x in l1)))
