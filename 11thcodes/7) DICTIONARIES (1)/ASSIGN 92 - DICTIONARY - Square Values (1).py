def expn(b,e):
    prod=1
    for i in range(1,e+1):
        prod*=b
    return prod

def dictionary():
    D={}
    n=input("Enter Number of Elements ")
    for i in range(1,n+1):
        a=input("Enter the key: ")
        D[a]=expn(a,2)
    return D

def printd(D):
    print "Number \t Square of Number"
    for a in D:
        print a, "\t\t", D[a]


D=dictionary()
printd(D)
print D

