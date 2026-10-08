#linear search checking the elements one by one from beginning to end
#basic pattern
numbers=[10,20,30,40,50]
#we want to search number 50
'''for i in range(len(numbers)):
    if numbers[i]==50:
        print("Found")
    else:
        print("Not found")'''

#another method
numbers=[10,20,30,40,50]
target=50
for i in range(len(numbers)):
    if numbers[i]==target:
        print("Found")
    else:
        print("Not found")

#but we want to get only one o/p which is found or not found .

numbers=[10,20,30,40]
target=20
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        found=True
if found==True: 
    print("Found")
else:
    print("Not found")
    
#for the above one we can write if statement in another way
numbers=[10,20,30,40]
target=int(input("enter the value:"))
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        found=True
if found:
    print("element got Found")
else:
    print("Not found")

##linear search -finding the index
numbers=[10,20,30,40]
target=int(input("enter the value:"))
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        found=True
if found:
    print("element got Found")
    print(i)
else:
    print("Not found")

'''the above one i got o/p as 3 for print(i),beacuse its giving me the last index value ,
    we have to store the index when it got true or else the loop iterates and gives the last value.'''

##crct version of linear search -finding the index
numbers=[10,20,30,40]
target=int(input("enter the value:"))
index=-1
for i in range(len(numbers)):
    if numbers[i]==target:
        index=i
if index!=-1 and found:
    print(f'element found at,{index} index')
else:
    print("Not found")
    





        