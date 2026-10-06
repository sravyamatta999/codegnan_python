#Leap year 
year = int(input())

if year % 400 == 0:
    print("Leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap year")
else:
    print("Not a leap year")

#car rentals question.
customers=int(input())
if customers %4==0:
    print(customers//4)
else:
    print(customers//4+1)


#password plm
pwd=input()
l=len(pwd)
if l==8:
    print("weak")
elif l>8 and l<16:
    print("good")
elif l>15 and l<=20:
    print("excellent")
elif l>20:
    print("hard to remember")
else:
    print("not valid")

#nested
username=input()
if username=="john":
    password=int(input())
    if password==1234:
        print("log in")
    else:
        print("wrong password")
else:
    print("wrong username")
    
#student eligibility
year=int(input())
marks=int(input())
backlogs=int(input())
if year==4:
    if marks>81:
        if backlogs==0:
            print("special training")
        else:
            print("should be 0 backlogs")
    else:
        print("marks should be greater than 81 ")
else:
    print("you have to be in 4th year")

##student eligibility
year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input("enter marks:"))
    
    if marks>80 and marks<=100:
        backlogs=int(input("enter bakclogs:"))
        
        if backlogs!=0:
            if backlogs>=1 and backlogs<=3:
                
                pay=input("you have to pay 5000 extra: [yes (or) no]:")
                if pay=="yes":
                    print("eligible for training")
                else:
                    print("must need to pay")

            elif backlogs>3:
                
                pay=input("you have to pay 10k [yes (or) no]:")
                if pay=="yes":
                    print("eligible for trainig")
                else:
                    print("must need to pay 10k")
                    
            
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")
    




    

