#List accessing the element/values
numbers=[10,20,30,40,50]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

#changing an element
#lists are mutable
numbers=[10,20,30,40,50]
print(numbers)
numbers[3]=200
print(numbers)

#length
print(len(numbers))

numbers=[1,2,3,4,5]
for i in range(len(numbers)):
    print(i)
print(numbers)
    
#the above one can be write as
for i in range(5):
    print(i)
print(numbers)
#the first one range(len()) is best cause if list is chnaged we don't need to change the code .
#this is how we traverse in a list.
marks=[10,20,30,40]
for i in range(len(marks)):
    print(f'{marks[i]},{i}')




    