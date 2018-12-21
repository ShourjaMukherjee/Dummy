def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def swap(L,i,j):
    t=L[i]
    L[i]=L[j]
    L[j]=t

def Sel_sort(L):
    l=len(L)
    for i in range(l-1):
        for j in range(i+1,l):
            if L[i]>L[j]:
                swap(L,i,j)
    return L

def evenorodd(n):
    flag=False                                              #odd
    if n%2==0:
        flag=True                                          #even
    return flag

def sort(L):
    l=len(L)
    E=[]
    Ei=[]
    O=[]
    Oi=[]
    for i in range(l):
        a=evenorodd(L[i])
        if a==True:
            E.append(L[i])
            Ei.append(i)
        else:
            O.append(L[i])
            Oi.append(i)
    E=Sel_sort(E)
    #print "Sorted E=",E
    O=Sel_sort(O)
    #print "Sorted O=",O
    for i in range(len(E)):
        L[Ei[i]]=E[i]
    for i in range(len(O)):
        L[Oi[i]]=O[i]
    return L        

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "Orginal List:- ",L
L=sort(L)
print "Sorted List:- ",L
