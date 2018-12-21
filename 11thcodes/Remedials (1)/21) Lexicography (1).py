def accept_list(n):
    L=[]
    for i in range(n):
        a=int(raw_input("Enter Element at index %d :- "%i))
        L.append(a)
    return L

def strCompare(S1,S2):
    l1=len(S1)
    l2=len(S2)
    l=l1 if l1<l2 else l2
    small = 'x'
    large = 'y'
    flag = False
    for i in range(l):
        d=ord(S1[i])-ord(S2[i])
        d=-d if d<0 else d
        if d in range (1,32):
            if (S1[i] < S2[i]):
                small,large = S1[i], S2[i]
                flag = True
            else:
                small,large = S2[i], S1[i]

        small = chr (ord (small)+32)
           
        if ord(small)<ord(large):
            return -1
        elif ord(small)>ord(large):
            return 1
    if l1==l2:
        return 0
    elif l1<l2:
        return -1
    else:
        return 1

def lexicography(L):
    l=len(L)
    for i in range(l-1):
        for j in range(i+1,l):
            if strCompare(L[i],L[j])==1:
                swap(L,i,j)
    return L

def swap(L,i,j):
    t=L[i]
    
    L[i]=L[j]
    L[j]=t

L=['rose','santa claus', 'red','greenary','pump','paradox','santa','apple','war','ball','green']
#n=int(raw_input("Enter the Number of Elements:- "))
#L=accept_list(n)
print "Original List:- ",L
N=lexicography(L)
print N
