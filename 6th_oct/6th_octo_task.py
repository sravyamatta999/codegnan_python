'''Q. Rapido Ride Fare Calculator

A Rapido bike ride charges the customer based on the distance travelled:

• For the first 5 km, the fare is ₹5 per km.
• For the next 7 km (6–12 km), the fare is ₹6 per km.
• For the next 8 km (13–20 km), the fare is ₹8 per km.
• For the distance from 21–29 km, the fare is ₹10 per km.
• If the distance is 30 km or more, the ride is not possible.

Write a Python program to take the total distance travelled (in km) as input and calculate the total ride fare.

Examples:

Input: 4
Output: 20

Input: 8
Output: 43

Input: 18
Output: 115

Input: 20
Output: 131

Input: 25
Output: 181

Input: 29
Output: 221

Input: 30
Output: Ride not possible'''
n=int(input())
if n<=5:
    total_cost=n*5
    print(total_cost)
elif n<=12:
    total_cost=n*5+(n-5)*6
    print(total_cost)
elif n<=20:
   total_cost=5*5+7*6+(n-12)*8
   print(total_cost)
elif n<30:
    total_cost=5*5+7*6+8*8+(n-20)*10
    print(total_cost)
else:
    print("ride not possible")


'''An electricity company charges according to the number of units consumed:
- First 50 units → ₹2 per unit
- Next 50 units (51–100) → ₹3 per unit
- Next 100 units (101–200) → ₹5 per unit
- Above 200 units → ₹8 per unit
- If the consumption is more than 300 units, print "High consumption"
Write a Python program that takes the number of units consumed as input and calculates the total electricity bill.'''

units=int(input())
if units<=50:
    total_cost=units*2
    print(total_cost)
elif units<=100:
    total_cost=50*2+(units-50)*3
    print(total_cost)
elif units<=200:
    total_cost=50*2+50*3+(units-100)*5
    print(total_cost)
elif units<=300:
    total_cost=50*2+50*3+100*5+(units-200)*8
    print(total_cost)
else:
    print("High consumption")




