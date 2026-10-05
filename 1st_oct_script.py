'''#set methods
asdd() to add one element in the set , update is to add more than one value .
n= {1,2,3} and if we give n.add(1) it doen't add casuse set doesn't allow duplicates.


n={1,2,3}
n.add(1)
print(n)
print(n.remove(4))
so basically if we give the number which is not present it throws an error
print(n.pop())
print(n)
#so pop removes random element
n={1,2,3,4}
print(n.discard(5))
#soo discard gives none if the element is not present in list. it doen't throw an error unlike remove ()

n.add(30)
print(n)
n.update([30,40])
print(n)
n.update({30,40})
print(n)
n.update((60,70))
print(n)
set.add() adds exactly ONE item to a set.
The item given to add() must be hashable.
List and set are unhashable, so they cannot be added as one element.
update() is used to add multiple elements from a list, tuple, or set.

babu={"phani","sai","john","ram"}
ntr={"pardhu","john","ram","kumar"}
#union-->all
#intersection
#difference
#symmetric_differnece
#superset
#issubset
#isdisjoint-->no common elements
n={1,2,3}
m={4,5,6,2}
print(n.isdisjoint(m)'''

"""s={1,2,3,4,5}
print(max(s),min(s),len(s),sum(s))
print(sorted(s))
print(s)"""


#user inputs
#list as intergers

n=list(map(int,input().split(",")))
print(n)
#if it string -->str,if it is float -->float()

#tuple antey tuple()

n=6
l=list(map(int,input().split()))
print(l)
