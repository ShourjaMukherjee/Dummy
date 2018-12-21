def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=input("Enter Values:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
    return L

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
    
def bubbleSort(L):
    l=len(L)
    for i in range(l-2,-1,-1):
        for j in range(i+1):
            if L[j]>L[j+1]:
                swap(L,j,j+1)
    return L

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "Orginal List:- ",L
R=bubbleSort(L)
print "Sorted List:- ",R

