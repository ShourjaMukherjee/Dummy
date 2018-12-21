def consecutiveCharacter(S):
    S+=' '
    l=len(S)
    count=1
    L=[]
    for i in range(l-1):
        if S[i]==S[i+1]:
            count+=1
        else:
            L.append(count)
            count=1
    return L

def swap(L,i,j):
    t=L[i]
    L[i]=L[j]
    L[j]=L[i]

def largest(L):
    N=L
    l=len(L)
    for i in range(l-1):
        for j in range(i+1,l):
            if L[i]<L[j]:
                swap(L,i,j)
    print L[0]
    

def fat(S):
    L=consecutiveCharacter(S)
    l=largest(L)
    

S="rrrwefsfsasdeeeeewtrr"
L=consecutiveCharacter(S)
largest(L)
