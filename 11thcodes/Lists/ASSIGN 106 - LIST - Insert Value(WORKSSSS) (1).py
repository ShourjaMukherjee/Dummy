def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def insertValue(L,n):
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
L=[14,25,34,56,79]
print "Orginal List:- ",L
r=int(raw_input("Enter Element to be inserted:- "))
N=insertValue(L,r)
print "New List:- ",N
