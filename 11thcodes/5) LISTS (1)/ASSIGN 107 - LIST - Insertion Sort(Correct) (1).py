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

def insertSort(L):
    l=len(L)
    for i in range(1,l):
        j=i
        while j>0 and L[j-1]>L[j]:
            swap(L,j,j-1)
            j-=1
    return L

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "Orginal List:- ",L
N=insertSort(L)
print "The sorted List is:- ",N
