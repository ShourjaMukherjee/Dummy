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

def check_occurance(L,N):
    l=len(L)
    n=len(N)
    for i in range(n):
        count=0
        for j in range(l):
            if N[i]==L[j]:
                count+=1
        if count%2==0:
            print N[i],"occurs even times:-",count
        else:
            print N[i],"ocuurs odd times:-",count
        
L=[1,1,1,2,3,4,3,2,4,1,2,5,7,2,3,4,5]
print L
N=mod_List(L)
print N
check_occurance(L,N)

