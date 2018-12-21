def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def leaderList(L):
    l=len(L)
    R=[]
    for i in range(l):
        if i==0:
            if L[i]>L[i+1]:
                R.append(L[i])
        elif i==l-1:
            if L[i]>L[i-1]:
                R.append(L[i])
        elif L[i]>L[i+1] and L[i]>L[i-1]:
            R.append(L[i])
        else:
            R.append(L[i])
    r=R[-1]
    return r

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "List:- ",L
r=leaderList(L)
print "Leader of List is:- ",r 
