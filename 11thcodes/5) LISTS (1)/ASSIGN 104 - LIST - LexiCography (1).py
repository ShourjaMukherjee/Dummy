
def lexiCography(L):
    l=len(L)
    for i in range(1,l+1):
        #print len(L[i])
        if len(L[i-1])==len(L[i]):
            n=len(L[i-1])
            for j in range(n):
                #print i,j
                if ord(L[i-1][j])<ord(L[i][j]):
                    swap(L,i-1,i)
                    print L
        elif len(L[i-1])>len(L[i]):
            n=len(L[i])
            for j in range(n):
                #print i,j,ord(L[i-1][j]),ord(L[i][j])
                if ord(L[i-1][j])<ord(L[i][j]):
                    swap(L,i-1,i)
                    print L
        else:
            n=len(L[i-1])
            for j in range(n):
                #print i,j
                if ord(L[i-1][j])<ord(L[i][j]):
                    swap(L,i-1,i)
                    print L

    return L


def swap(L,i,j):
    t=L[i]
    L[i]
    L[i]=L[j]
    L[j]=t

L=["hello",'fatt','potassium','neon']
R=lexiCography(L)
print R
