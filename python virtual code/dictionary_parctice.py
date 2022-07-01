##que1. Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30] 
d1=dict(zip(keys,values))
print(d1)

### or
d1={}
for i in range(len(keys)):
    d1.update({keys[i]:values[i]})
    print(d1)

##Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d4={**dict1,**dict2}
print(d4)

##or
d3=dict1.copy()
dict2.update(dict1)
print(dict2)

##Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

##Initialize dictionary with default values
##In Python, we can initialize the keys with the same values.
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res=dict.fromkeys(employees,defaults)
print(res)

##Create a dictionary by extracting the keys from a given dictionary
##Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
sampleDict = { "name": "Kelly","age":25,  "salary": 8000,  "city": "New york" }

keys = ["name", "salary"]
newd1={k:sampleDict[k] for k in keys}
print(newd1)
newd2={a:sampleDict[a] for a in keys}
print(newd2)

####orr
d1=dict()
for k in keys:
    d1.update({k:sampleDict[k]})
print(d1)

##Delete a list of keys from a dictionary

sample_dict = { "name": "Kelly","age":25,  "salary": 8000,  "city": "New york" }

keys = ["name", "salary"]##remove keys

for k in keys:
    sampleDict.pop(k)
    print(sampleDict)

### or---  
  
sample_dict={k: sample_dict for k in sample_dict.keys()-keys }
print(sample_dict)

##que.Check if a value exists in a dictionary
##Write a Python program to check if value 200 exists in the following dictionary.
sample_dict = {'a': 100, 'b': 200, 'c': 300}
if 200 in sample_dict.values():
    print('200 present in dict')
else:
    print('no')

##Rename key of a dictionary
##Write a program to rename a key city to a location in the following dictionary.
sample_dict = { "name": "Kelly","age":25,  "salary": 8000,  "city": "New york" }
sample_dict['location']=sample_dict.pop('city')
print(sample_dict)

##que.Get the key of a minimum value from the following dictionary
sample_dict = {'Physics': 82,'Math': 65,'history': 75}
min='physics'
for k in sample_dict:
    if min>k:
        min=k
print('The key of mimimum value is',min,'65')      

#Change value of a key in a nested dictionary
#Write a Python program to change Brad’s salary to 8500 in the following dictionary.
sample_dict = {'emp1': {'name': 'Jhon', 'salary': 7500},
               'emp2': {'name': 'Emma', 'salary': 8000},
                'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)

### by using fromkeys() method
marks={}.fromkeys(['english','math','science'],0)
print(marks)

# Dictionary Comprehension
squares={x: x*x for x in range(6)}
print(squares)

## or---
squares={}
for i in range(6):
    squares[i]=i*i
print(squares)

### divition
divistion={}
for i in range(5):
    divistion[i]=i%2

print(divistion) 

## multiplication
multiplication={}
for i in range(6):
    multiplication[i]=i*i
print(multiplication) 

#### addition
add={}
for i in range(6):
    add[i]=i+i 
print(add)

# Dictionary Comprehension with if conditional 
## square only odd number
square={x: x*x for x in range(11) if x%2==1}
print(square)

## Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])


