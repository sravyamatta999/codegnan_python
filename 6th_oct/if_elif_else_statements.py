#Write a program to classify a number as positive, negative, or zero.
n=int(input("enter the number:"))
if n>0:
    print("positive number")
elif n==0:
    print("zero")
else:
    print("negative number")

#Write a program to categorize a person’s age as a child (0-12), teenager (13-19), or adult (20+).
age=int(input("enter your age:"))
if age >=0 and age <=12:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
else:
    print("adult")
#Write a program to determine the grade of a student based on marks (A: 90+, B: 80+, C: 70+, D: 60+, Fail: <40).
marks=int(input("enter the marks of the student:"))
if marks>=90:
    print("The grade is A")
elif marks >=80 :
    print("The grade is B")
elif marks>=70:
    print("The grade is C")
elif marks>=60:
    print("The grade is D")
else:
    print("Fail")
    

