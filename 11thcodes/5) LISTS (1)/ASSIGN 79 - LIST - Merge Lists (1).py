def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=raw_input("Enter Value:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
    return L

def merge(L,N):
    l=len(L)
    n=len(N)
    r=l+n
    R=[0 for i in range(r)]
    for i in range(l):
        R[i]=L[i]
    for i in range(n):
        R[l+i]=N[i]
    print R


N=[]
R=[]
N=acceptList(N)
print N
R=acceptList(R)
print R

merge(N,R)
