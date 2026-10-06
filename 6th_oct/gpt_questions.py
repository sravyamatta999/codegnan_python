#1)A website wants to check whether a person is old enough to create an account.
#If the person's age is 18 or above, print:
#You can create an account

n=int(input())
if n>=18:
    print("You can create an account")

'''2)
A movie theatre allows a person to enter a horror movie only if their age is 18 or above.
Write a program that:
- Takes age as input
- If age is 18 or above, print:
  "You can watch the movie"'''

age=int(input("Enter your age:"))
if age >=18:
    print("You can watch the movie")

'''3)
ATM scenario:
Write a program that takes the user's balance as input.
- If balance is greater than or equal to ₹500, print:
  "You can withdraw money"
- Otherwise, print:
  "Insufficient balance"'''

Balance=int(input())
if Balance>=500:
    print("You can withdraw money")
else:
    print("Insufficient balance")
    
'''4)  A shop gives a free gift if the customer's bill is more than ₹1000.
Write a program:
- Take bill as input
- If bill > 1000, print "Free gift"
- Otherwise print "No free gift"'''

bill=int(input())
if bill >1000:
    print("Free gift")
else:
    print("No free gift")

'''5)A student can write the exam if their attendance is 75% or more.
Write a program:
- Take attendance as input
- If attendance is 75 or above, print "Eligible for exam"
- Otherwise, print "Not eligible for exam"'''

attendance=int(input())
if attendance >=75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")
'''for the above question what if user enters the percentage beside the value cause its a attendance'''
#this is another method using replace()
attendance = float(input("Enter your attendance: ").replace("%", ""))
if attendance >=75:
    print("eligible for exam")
else:
    print("not eligible for exam")

'''6)Login scenario
A website asks the user for a PIN.
Write a program that:
- Takes the PIN as input
- If the PIN is exactly 1234, print:
  Login successful
- Otherwise, print:
  Wrong PIN'''

pin=int(input())
if pin==1234:
    print("Login successful")
else:
    print("wrong PIN")


'''7)Phone unlock scenario
A phone should stay locked if the entered PIN is NOT 5555.
Write a program:
- Take PIN as input
- If PIN is not equal to 5555, print "Phone locked"
- Otherwise, print "Phone unlocked"'''

lock=int(input())
if lock !=5555:
    print("phone locked")
else:
    print("phone unlocked")
    

    
    
    
    
    
    
