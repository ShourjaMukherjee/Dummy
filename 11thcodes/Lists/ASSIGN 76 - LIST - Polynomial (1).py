def acceptList(n):
    L=[]
    
    for i in range(n+1):
        x=float(raw_input("Enter coeficient of x raised to %d:-"%i))
        L.append(x)

    return L

def value(x,L):
    sum=0
    l=len(L)
    for i in range(l):
        r=(x**i)*L[i]
        sum+=r
    return sum

n=int(raw_input("Enter degree of polynomial,n:- "))
L=acceptList(n)
x=int(raw_input("Enter value of x:- "))
sum=value(x,L)
print "The value of polynomial is:- ",sum
