#focus on rows , spaces columns ,values
'''
for i in range(4):#0,1,2,3,4
    for j in range(i+1):
        print("*",end="")
    print()
    
n=4
for i in range(4,0,-1):#0,1,2,3,4
    for j in range(n-i+1):
        print("*",end="")
    print()


n=4
for i in range(n):
    for spaces in range(n-i-1):
        print(" ",end="")
    for stars in range(i+1):
        print("*",end="")
    print()'''

n=4
rows=0
while rows<n:
    spaces=0
    while spaces<n-rows-1:
        print(" ",end=" ")
        spaces+=1
    
    stars=0
    while stars<rows+1:
        print("*",end=' ')
        stars+=1
    print()
    rows+=1


n=4
rows=0
while rows<n:
    spaces=0
    while spaces<n-rows-1:
        print(" ",end=" ")
        spaces+=1
    
    stars=0
    while stars<rows+1:
        print(stars,end=' ')
        stars+=1
    print()
    rows+=1