def cumulativeSum(L):
    l=len(L)
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if L[j]+L[k]==L[i] and L[j]!=L[k] :
                    print "Fat:- ",L[j],"+",L[k],"=",L[i]

L=[1,3,4,7,9,3,2]
print L
cumulativeSum(L)
