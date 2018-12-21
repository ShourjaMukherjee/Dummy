def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=raw_input("Enter Value:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
    return L

def swap(L,i,j):
    t=L[i]
    L[i]=L[j]
    L[j]=t
    return L

def swapAlt(L):
    l=len(L)
    for i in range(0,l-1,2):
        swap(L,i,i+1)
    print L
    


L=[]
L=acceptList(L)
print L
swapAlt(L)

