print "PLEASE TURN  ON CAPS!!!!!!"
def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=float(raw_input("Enter Value:- "))
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
        
    return L

def ascen(L):
    l=len(L)
    for i in range(l):
        for j in range(l):
            if L[j]>L[i]:
                t=L[i]
                L[i]=L[j]
                L[j]=t
    return L

L=[]
L=acceptList(L)
print "Orginal List:- ",L
N=ascen(L)
print "The List in Ascending order is:- ",N
