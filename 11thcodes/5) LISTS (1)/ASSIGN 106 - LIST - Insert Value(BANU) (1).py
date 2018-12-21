def insertionsort(L,n):
    l=len(L)
    N=[]
    if n>=L[-1]:
        L.append(n)
        return L

    if l+1!=len(L):
        for i in range(l):
            if n>=L[i]:
                N.append(L[i])
        N.append(n)
        for i in range(l):
            if n<L[i]:
                N.append(L[i])
    return N

L=[11,24,34,46,55]
print L
n=input("Enter the number: ")
A=insertionsort(L,n)
print A
                
