def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def prodList(L):
    l=len(L)
    N=[1 for i in range(l)]
    for i in range(l):
        for j in range(l):
            if j!=i:
                N[j]*=L[i]
    return N

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "Orginal List:- ",L
N=prodList(L)
print "Modified List:- ",N
