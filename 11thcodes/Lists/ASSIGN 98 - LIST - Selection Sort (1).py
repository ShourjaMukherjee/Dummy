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

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "Orginal List:- ",L
Sel_sort(L)
print "The sorted List is:- ",L


