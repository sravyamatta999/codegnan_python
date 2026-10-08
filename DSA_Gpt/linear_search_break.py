#break
numbers=[1,2,3,4,5]
target=4
for i in range(len(numbers)):
    if numbers[i]==target:
        print("found the element")
        break
        
    
numbers=[20,30,40,50]
target=30
index=-1
for i in range(len(numbers)):
    if numbers[i]==target:
        index=i
        break
if index!=-1:
    print("found at index :" ,index)
else:
    print("Not found")


numbers=[20,30,40,50,60]
target=100
found=False
for i in range(len(numbers)):
    if numbers[i]==target:
        found=True
        break
if found:
    print("Found")
else:
    print("Not Found")
               
               
numbers = [10, 20, 30, 40]
target = 50

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        print("Found at index", i)
        break

if not found:
    print("Not found")