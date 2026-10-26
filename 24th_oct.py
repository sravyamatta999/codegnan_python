def Number(n):
    if n==0:
        return
    
    else:
        print(n)
        Number(n-1)
       
Number(10)

def Fact(n):
    if n==5:
        return 5
    else:
        return n*Fact(n+1)
print(Fact(1))



def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def Fact(n):
    if n==5:
        return 5
    
    else:
        return n*Fact(n+1)
        
print(Fact(1))


