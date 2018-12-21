print "PLEASE TURN  ON CAPS!!!!!!"
def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=raw_input("Enter Value:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
        
    return L

def isPresent(n,L):
    flag=False
    l=len(L)
    for i in range(l):
        if L[i]==n:
            flag=True
            break
    return flag

def modify_str(L):
    N=[]
    N.append(L[0])
    l=len(L)
    for i in range(1,l):
        flag=isPresent(L[i],N)
        if flag==False:
            N.append(L[i])
    print "Modified List:- ",N

L=[]
L=acceptList(L)
N=modify_str(L)



