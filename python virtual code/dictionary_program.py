## create dictionary
d1={}
print(type(d1))
my_dict={1:'Madhuri',2:'Ankita',3:'komal'}
print(my_dict)
print(type(my_dict))
# create a dictionary using a dit class
##way 2
d1={}
d1['name']='Anant'
d1['Age']=30
print(d1)

## way 3
d3=dict(name='python',fee=240000)
print(d3)

##way 4
d4=dict([('NAme','python'),('fee',240000)])
print(d4)

d1=dict({1:'a',2:'b',2:'c'})
print(d1)
print(type(d1))

# access value using a key name
my_dict={1:'Madhuri',2:'Ankita',3:'komal'}
print(my_dict[1])

# change the value of a key
d1=dict({1:'a',2:'b',2:'c'})
d1[2]='d'
print(d1)

##que.Adding and replacing value in dict
## 1.add value by key
d1={1:'python',2:'java',3:'c++'}
print(d1)
d1[4]='testing'
print(d1)

## replace the value
d2={'english':80,'Math':90,'science':70}
print(d2)
d2['Math']=100
print(d2)

##Retrieving Values ie.display value by usingkey
d3={'city1':'pune','city2':'mumabai','city3':'nashik'}
print(d3)
print("The is a",d3['city1'])

## formating method
d4={'Laptop':'Mac','Count':10}
print(d4)
print(" I Want to {Count} laptops {Laptop}".format(**d4))

##Deleting Items 
d5=dict(name='python',fee=2400000,city='pune')
print(d5)
del d5['city']
print(d5)

##Comparing Two Dictionaries
A={'I':'India','A':'America'}
print(A)
B={'I':'Itly','A':'America'}
print(B)
print(A==B)
print(A!=B)

##The Methods of Dictionary Class

##1.keys()
Ascii_code={'A':65,'B':66,'C':67,'D':68}
print(Ascii_code)
print(Ascii_code.keys())

##2.values()
Ascii_code={'E':69,'F':70,'G':71}
print(Ascii_code.items())
print(Ascii_code.values())

##3.get(keys)
Temp={'Pune':30,'Mumnai':35,'Nashik':40}
print(Temp)
print("The temp of pune is:=",Temp.get('Pune'))

##4.pop(key)
color={'Red':10,'Yellow':20,'Black':30,'Blue':50}
print(color)
color.pop('Red')
print(color)

##4.clear()
d1={1:10,2:20,3:30}
print(d1)
d1.clear()
print(d1)

##Traversing Dictionaries
Grades={'Madhuri':'A','Anant':'A+','Ankita':'B','Komal':'C'}
for key in Grades:
    print(key,":",str(Grades[key]))

d1={'Swara':'A','Harshada':'A+'}
for key in d1.keys():
    print(key,':',d1.get(key))

##Nested Dictionaries
Players={'Virat Kolhi':{'ODI':7212,'Test':3245},'Sachin ten':{'ODI':18456,'Test':12345}}
print("Virat Kolhi runrate of ODI match is",Players['Virat Kolhi'] ['ODI'])
print('Schin ten runrate of test match is',Players['Sachin ten'] ['Test'])
print(Players['Virat Kolhi'].values())
print(Players['Virat Kolhi'].keys())

##Traversing Nested Dictionaries
Grades={'Madhuri Burande':{'Python':100,'Java':90},'Anant Burande':{'c++':100,'Data':80}}
for name,score in Grades.items():
    print(name)
    print(score)
