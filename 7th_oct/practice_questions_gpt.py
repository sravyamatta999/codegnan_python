'''Bank loan scenario
A person gets a loan only if:
- Age is 18 or above
- AND salary is ₹30,000 or above'''

age=int(input())
salary=int(input())
if age>=18 and salary>=30000:
    print("loan approved")
else:
    print("loan rejected")

'''College Admission Scenario
A student can get admission through a special quota if either:
- Their entrance exam score is 90 or above
  OR
- Their sports achievement is "yes"
'''

score=int(input())
sports=input()
if score>=90 or sports=="yes":
    print("special admission")
else:
    print("regular admission")

'''Premium Bank Account
A customer gets a premium account if:
- Their salary is ₹50,000 or above AND their age is 25 or above
- OR
- They have been a customer for 5 years or more'''

salary=int(input())
age=int(input())
customer=int(input())
if (salary>=50000 and age>=25) or customer>=5:
    print("premium account")
else:
    print("Normal account")
    

'''Student Grade System
Take a student's marks as input.
- 90–100 → print "Grade A"
- 80–89 → print "Grade B"
- 70–79 → print "Grade C"
- 60–69 → print "Grade D"
- Below 60 → print "Fail"'''
marks=int(input())
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
elif marks>=60 and marks<70:
    print("Grade D")
else:
    print("Fail")

#for the above question i don't need to right upper limit .can be written like this
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")


'''Swimming Pool Entry
A swimming pool has these rules:
- Age below 5 → "Free entry"
- Age 5–17 → "Child ticket"
- Age 18–59 → "Adult ticket"
- Age 60 or above → "Senior citizen ticket"'''

age=int(input("enter your age:"))
if age<=5:
    print("Free ticket")
elif age<=17:
    print("Child ticket")
elif age<=59:
    print("Adult ticket")
else:
    print("Senior citizen ticket")

        








           
