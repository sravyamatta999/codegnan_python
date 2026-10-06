#A bank checks if a person is eligible for a loan based on their age and salary.
age=int(input("enter your age:"))
salary=int(input("enter your salary:"))
if age>=18 and salary>=1000000:
    print("you are eligible for loan")
else:
    print("sorry you are not eligible")

#nested if for the above question.
age=int(input("enter your age:"))
salary=int(input("enter your salary:"))
if age>=18:
    if salary>=1000000:
        print("you are eligible for loan")
    else:
        print("sorry ,your salary is low")
else:
    print("you are underage")
    

#A student needs at least 35 marks to pass. If they score above 90, they get a scholarship.
marks=int(input("enter your marks:"))
if marks>=35:
    if marks>90:
        print("you are eligible for scholarship")
    else:
        print("you are not eligible for scholarship")
else:
    print("you haven't passed the exam")
 ##   
n=input()
if n.isupper():
    print("allow")
else:
    print("don't allow")
#if the given letter is capital letter print small letter 
#if the given letter is small letter print capital letter
n = input() 
if n.isupper():
    print(n.lower())
else:
    print(n.upper())
    
#another method for the above question
n=input()
x=n.swapcase()
print(x)
##take the input from the user and add +10 to it and check the new number whether it even or odd 
n=int(input())
x=n+10
if(x%2==0):
  print("even")
else:
  print("odd")