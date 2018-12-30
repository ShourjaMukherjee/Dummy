def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def leftSum(L,n):               # gives sum of all elements to the left of
    sum=0                       # index n
    for i in range(n):
        sum+=L[i]
    return sum

def rightSum(L,n):              # gives sum of all elements to the right
    l=len(L)                    # of index n
    sum=0
    for i in range(n+1,l):
        sum+=L[i]  
    return sum

def check_Pivot(L):             # checks and prints index of Pivot Element
    l=len(L)
    flag=False
    for i in range(1,l-1):
        n=leftSum(L,i)          # sum of elements to left of index i
        r=rightSum(L,i)         # sum of elements to right of index i
        if n==r:
            flag=True
            print "Pivot Element is present at index:- ",i
            break
    if flag==False:
        print "There is no Pivot Element."

#L=[1,2,3,4,6]
n=int(raw_input("Enter the Number of Elements:- "))
L=accept_list(n)
print "List:- ",L
N=check_Pivot(L)
