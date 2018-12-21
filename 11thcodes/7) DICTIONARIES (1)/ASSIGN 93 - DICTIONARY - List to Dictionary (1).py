def dictionary(L1,L2):
    D={}
    n=len(L1)
    for i in range(n):
        a=L1[i]
        D[a]=L2[i]
    return D

def acceptList(n):
    L=[]
    for i in range(n):
        a=input("Enter Element %d :- "%i)
        L.append(a)
    return L
        
def printDictionary(D):
    print "KEY \t\t VALUE"
    for a in D:
        print a,"\t\t",D[a]

n=input("Enter Number of Entries:- ")
print "Enter Key Values:- "
L1=acceptList(n)
print "Enter Corresponding Values:- "
L2=acceptList(n)
D=dictionary(L1,L2)
printDictionary(D)


