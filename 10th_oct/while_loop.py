#while syntax

i=0
while i<=5:
    print(i)#up to here we will get infite loop we need to increment
    i=i+1
    
i=5
while i>=0:
    if i==1:
        continue
        i-=1
    else:
        print(i)
        i-=1
else:
    print("completed")
    
    
i=5
while i>=0:
    if i==1:
        pass
        
    else:
        print(i)
        i-=1
else:
    print("completed")
    
    
    
a=int(input())
b=int(input())
for i in range(1,b+1):
  print(f"{a}*{i}={a*i}")
  
  
n=["pushpa","sravya","babu","lasya","prabha","paul"]
for i in n:
    if 

