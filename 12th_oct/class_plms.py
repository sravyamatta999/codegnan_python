l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2==0:    
        empty.append(l[i])
print(empty)

#
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if l[i]%2==0:    
        empty.append(l[i])
print(empty)

#
l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)):
    if i%2==0:    
        empty.append(l[i])
        print(empty)


        
#even index od value
n = [1, 3, 2, 5, 7, 9, 8]
empty = []

for i in range(len(n)):
    if i % 2 == 0 and n[i] % 2 != 0:
        empty.append(n[i])

print(empty)


#

n=[1,3,2,5,7,8,9]
empty=[]
for i in range(len(n)):
    n[i]=n[i]*n[i]
    empty.append(n[i])
print(empty)


#l=[1,3,2,5,7,9,8]
empty = []
for i in range(len(l)):
  n=l[i]**2
  empty.append(n)
print(empty)


#odd values +10
l=[1,3,2,5,7,9,8]
empty=[]
for i in l:
    if i%2!=0:
        empty.append(i+10)
    else:
        empty.append(i)
print(empty)

##reverse
l=[1,3,2,5,7,9,8]
l.reverse()
print(l)

#reverse using loop

l=[1,3,2,5,7,9,8]
empty=[]
for i in range(len(l)-1,-1,-1):
    empty.append(l[i])
print(empty)


for i in range(len(l)-1,-1,-1):
    empty.insert(0,l[i])
    print(empty)
    
n = ["mohan", "sravya", "pavani", "lasya"]

for i in range(len(n)):
    if n[i] == "babu":
        print("available")
        break
else:
    print("no")


names=["mohan","sravya","pavani","babu","lasya"]
i=0;count=[]
while i<len(names):
    count.append(len(names[i]))
    i+=1
print(count)



names=["mohan","sravya","pavani","babu","lasya"]
i=0
d={}
while i<len(names):
    d[names[i]]=len(names[i])
    i+=1
print(d)
#using for loop
names=["mohan","sravya","pavani","babu","lasya"]
d={}
for i in range(len(names)):
    d[names[i]]=len(names[i])
print(d)

