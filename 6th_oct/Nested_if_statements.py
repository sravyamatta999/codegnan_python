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
        