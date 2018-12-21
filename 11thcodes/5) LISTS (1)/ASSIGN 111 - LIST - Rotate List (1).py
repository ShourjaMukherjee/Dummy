def RollUp(L):
    l=len(L)
    t=L[0]
    for i in range(l-1):
        L[i]=L[i+1]
    L[-1]=t
    #print "Rolled Up List:-", L
    return L

def RollDown(L):
    l=len(L)
    t=L[-1]
    for i in range(l-2,-1,-1):
        L[i+1]=L[i]
    L[0]=t
    #print "Rolled Down List:-", L
    return L


L=[1,2,3,4,5]
#N=[1,2,3,4,5]
print "Orginal List:- ", L
#RollUp(L)
#RollDown(N)
n=int(raw_input("Enter Rotation Factor:- "))
if n>0:
    for i in range(n):
        N=RollDown(L)
else:
    a=-n
    for i in range(a):
        N=RollUp(L)
print "The List after being rotated with a factor of",n,"is:-"
print N

    
