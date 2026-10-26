##anonymous function -->nameless functions
#lambda(argu:expression)#lambda is a keyword any no of arguments but only one expression.
#the main reason to use lambda is to reduce the no of lines

add=lambda x,y:x+y
print(add(10,20))
    
##this is usual method
def add (x,y):
    print(x+y)
add(10,20)


result=lambda x,y,z,n:[x,y,z,n]
print(result("python","cython","java","bava"))

   

x=10;y=20
print((lambda x,y:x+y)(x,y))


print((lambda x,y:x+y)(10,20))

    
    
#find the given number is even or odd
print((lambda x:"even" if x%2==0 else "odd")(10))
'''
print((lambda x:x%2==0 "even")(12))   #error
#if is mandatory while uisng lambda if there is a condition'''

print((lambda n:"even" if n%2==0 and n>5 else "odd" if  n%2!=0 else "not")(10))

print((lambda n:"even" if n%2==0 and n>5 else "odd" if  n%2!=0 else "not")(2))

'''
name=input()
if len(name)<12 and len(name)>5:
    print("valid")
else:
    print("not valid")'''
    

name=input()
print((lambda name:"valid" if len(name)>5 and len(name)<12 else"not valid")(name))




