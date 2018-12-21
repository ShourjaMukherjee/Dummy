def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=input("Enter Value:- ")
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

def mod_List(L):
    R=[]
    R.append(L[0])
    l=len(L)
    for i in range(1,l):
        flag=isPresent(L[i],R)
        if flag==False:
            R.append(L[i])
    return R

def check_majority(L,N):
    l=len(L)
    n=len(N)
    flag=False
    for i in range(n):
        count=0
        for j in range(l):
            if N[i]==L[j]:
                count+=1
        if count>l/2:
            flag=True
            print L[i],"is a Majority Element. It occurs ",count,"times."
    if flag==False:
        print "There is no Majority Element."
     

L=[]
L=acceptList(L)
print L
N=mod_List(L)
print N
check_majority(L,N)


