def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def sortValue(L,n):
    L.append(0)
    l=len(L)
    if n<L[0]:
        L=rolldown(L,0)
        L[0]=n
    elif n>L[-2]:
        L[-1]=n
    elif n>L[0] and n<L[-2]:
        for i in range(l):
            if n>=L[i] and n<L[i+1]:
                L=rolldown(L,i+1)
                L[i+1]=n
                break
    return L

def rolldown(L,n):
    l=len(L)
    t=L[-1]
    for i in range(l-1,n-1,-1):
        L[i]=L[i-1]
    L[n]=t
    return L

#n=int(raw_input("Enter the Number of Elements:- "))
#L=accept_list(n)
L=[9,5,3,6,7,2,5,6,0,1]
print "Orginal List:- ",L
n=L[0]
l=len(L)
for i in range(1,l):
    N=sortValue(L,i)
print N

