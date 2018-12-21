def accept_list(n):
    L=[]
    for i in range(1,n+1):
        a=int(raw_input("Enter Share in Month %d :- "%i))
        L.append(a)
    return L

def bestshares(L):
    l=len(L)
    D=0
    for i in range(l-1):
        for j in range(i+1,l):
            if L[j]-L[i]>D:
                D=L[j]-L[i]
                b=i
                s=j
    return b,s


D=['January','Febuary','March','April','May','June','July','August','September','October','November','December']
#L=[4,8,9,3,14,7,15,5,2,10,11,7]
y=int(raw_input("Enter Starting Year:- "))
n=int(raw_input("Enter the Number of Months:- "))
L=accept_list(n)
print "List:- ",L
T=bestshares(L)
print "Best Month to Buy:- "
print "Month :- ",T[0]+1,"(",D[T[0]],y,")"
print "Share value:- ",L[T[0]]
print
print "Best Month to Sell:- "
print "Month :- ",T[1]+1,"(",D[T[1]],y,")"
print "Share value:- ",L[T[1]]
print "Profit:- ",L[T[1]]-L[T[0]]
