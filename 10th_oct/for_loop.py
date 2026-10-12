#iterable:list,tuple,dict,strings

d={"name": "balayya","age":60}
for i in d:
    print(i)
    
d={"name": "balayya","age":60}
for i in d .values():
    print(i)
    

d={"name": "balayya","age":60}
for i in d .items():
    print(i)
    


d={"name": "balayya","age":60}
for i in d:
    print(d[i])
'''

'''for i in range(100,-1,-1):
    print(i)


for i in range(-20,0,1):
    print(i)'''

'''n=int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}")
   
n=int(input()) 
for i in range(1,11):
    if i%2==0:
        print(f"{n}*{i}={n*i}")
        
n=int(input()) 
for i in range(2,11,2):
    print(f"{n}*{i}={n*i}")

n=int(input()) 
for i in range(10,0,-1):
    print(f"{n}*{i}={n*i}")


 ##looping control statements.

n=int(input()) #2
for i in range(1,11):
    if i!=5:
        print(f"{n}*{i}={n*i}")
    else:
        print("loops was breaked")
        break


for i in range(1,11):
    if i==5:
        break      
    else:
        print(f"{n}*{i}={n*i}")
        
        
n=int(input()) #2
for i in range(1,11):
    if i%2==0:
        continue
    elif i>=6:
        break
    else:
        print(f"{n}*{i}={n*i}")
        
        
n=int(input()) #2
for i in range(1,11):
    if i%2==0:
        continue
    elif i>=6:
        break
    else:
        print(f"{n}*{i}={n*i}")
