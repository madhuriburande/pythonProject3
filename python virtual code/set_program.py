##que1.Add a list of elements to a set
#Given a Python list, Write a program to add all its elements into a given set.

s1={'a','b','c','d','e'}
s2=[1,2,3,4]
s1.update([1,2,3,4])
print(s1)
s1.update(s2)
print(s1)

##que2.Return a new set of identical items from two sets
s1={'madhuri','anant','komal','swara'}
s2={'ankita','madhuri','swara','harshada'}
s1.intersection_update(s2)
print(s1)

##que3.Get Only unique items from two sets
##Write a Python program to return a new set with unique items from both sets by removing duplicates.
s1={1,2,3,4,5,6}
s2={2,3,4,7,8,9}
s1.union(s2)
print(s1)

##que4.Update the first set with items that don’t exist in the second set
#Given two Python sets, write a Python program to update the first set with items
#that exist only in the first set and not in the second set.
s1={10,20,30,40,50}
s2={10,30,50,60,70}
s1.difference_update(s2)
print(s1)

#que5.Remove items from the set at once
##Write a Python program to remove items 10, 20, 30 from the following set at once.
s1={10,20,30,40,50}
s1.difference_update({10,20,30})
print(s1)

##que6.remove elemnet in set
s3={1,2,3,4,5}
s3.remove(3)
print(s3)
s1={'python','java','c++','testing'}
s1.remove('testing')
print(s1)

##que7.add elemnet in set
s1={11,12,13,14,15}
s1.add(18)
print(s1)

##que8.add tuple in set
s1={10,20,30,40}
tuple=('madhuri','anant','swara')
s1.add(tuple)
print(s1)

##que9.copy elelement in set
s1={1,2,3,4}
s2=s1
print(s2)
s2.add(5)
print(s2)

##que10.clear set
s1={2,4,6,8}
s1.clear()
print(s1)

##que11.discard elelement in set
s1={3,5,7,9,11}
s1.discard(7)
print(s1)
s1.discard(12)
print(s1)
s2={2,3,4,5}
s2.discard(9)
print(s2)

##que12.check two sets are isdisjoint()or not
A={1,2,3,4,5}
B={6,7,8,-5}
print('Are A and B disjoint?=',A.isdisjoint(B))

a={'a','b','c','d'}
b={'a','x','z'}
print('Are A and B disjoint?',a.isdisjoint(b))

##que13.check different itrables like list,str,tup,dict  is not support isdisjoint
s1={1,2,3,4}
st='madhuri','anant','swara'
print('Are s1 and st disjoint?',s1.isdisjoint(st))

##que14.chech both sets are issubset or not.
s1={1,2,3,}
s2={1,2,3,4,}
s3={1,2,3,4,5,6,7}
print("s1 and s2 are subset or not?",s1.issubset(s2))
print("s2 and s3 are subset or not?",s2.issubset(s3))
print("s2 and s1 are subset or not?",s2.issubset(s1))
print("s3 and s1 are subset or not?",s3.issubset(s1))

##que15.check pop method
s1={22,33,44,55}
s1.pop()
print(s1)

a={'a','b','c','d'}
a.pop()
print(a)
##que16.check issuperset
s1={1,2,3,4,5}
s2={2,6,5,4}
s1.issuperset(s2)
print(s1)
##que6.Return a set of elements present in Set A or B, but not both

A={10,20,40,50,6}
B={10,3,5,6,90,20}
print("set of element present in A or B but not both",A.symmetric_difference(B))

##que7.Check if two sets have any elements in common. If yes, display the common elements
s1={31,22,14,10,23}
s2={5,28,31,22,10}
print("common elements sre two sets:=",s1.intersection(s2))

##que8.Update set1 by adding items from set2, except common items
s1={'python','java','c++'}
s2={'java script','java','c','pi'}
s1.symmetric_difference_update(s2)
print("set 1 ny adding items from set but except common items",s1)

##que9.Remove items from set1 that are not common to both set1 and set2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print("remove item from set 1 are not common both",set1)
