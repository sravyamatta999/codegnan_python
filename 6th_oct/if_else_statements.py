#Write a program to check if a number is even or odd.
n=int(input("enter a number:"))
if n%2==0:
    print("the number is even")
else:
    print("odd")

#Write a program to check if a person is eligible for a driving license (age 18 or above).
driving_license=int(input("enter your age:"))
if driving_license>=18:
    print("eligible for driving license")
else:
    print("Not eligible for driving license")

#Write a program to check if a number is positive or negative.
n=int(input("enter a number:"))
if n>=0:
      print("positive number")
else:
    print("Negative number")
    
#Write a program to check if a student passed or failed based on marks (Pass: 40+, Fail: below 40).
Marks=int(input("enter marks:"))
if Marks>=40:
    print(f'The student marks are {Marks} and got passed in the exam,congratulations.')
          
