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

def Binary_search(L,k):        #To check if the key is present in the list
    Sel_sort(L)
    flag=False
    l=0
    u=len(L)-1
    while l<=u:
        mid=(l+u)/2
        if L[mid]>k:
            u=mid-1
        elif L[mid]<k:
            l=mid+1
        else:
            flag=True
            break
    return flag

n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
key=int(raw_input("Enter the Key:- "))
state=Binary_search(L,key)
if state==True:
    print ("The key",key,"is present in the given list.")
else:
    print ("The key",key,"is not present in the given list.")


