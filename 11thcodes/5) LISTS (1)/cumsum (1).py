def cumulativesum(L,n):
    l=len(L)
    flag=False
    #print "The combinations of elements in list that gives sum",n,"is:- "
    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(j+1,l):
                for r in range(k+1):
                    if L[i]+L[j]+L[k]+L[r]==n:
                        print L[i],"+",L[j],"+",L[k],"+",L[r],"=",n
                        flag=True
    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if L[i]+L[j]+L[k]==n:
                    print L[i],"+",L[j],"+",L[k],"=",n
                    flag=True
    for i in range(l-1):
        for j in range(i+1,l):    
                if L[i]+L[j]==n:
                    print L[i],"+",L[j],"=",n
                    flag=True

    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(j+1,l):
                for r in range(k+1):
                     for a in range(r+1,l):
                         if L[i]+L[j]+L[k]+L[r]+L[a]==n:
                             print L[i],"+",L[j],"+",L[k],"+",L[r],"+",L[a],"=",n
                             flag=True

    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(j+1,l):
                for r in range(k+1):
                     for a in range(r+1,l):
                         for b in range(a+1,l):
                             if L[i]+L[j]+L[k]+L[r]+L[a]+L[b]==n:
                                 print L[i],"+",L[j],"+",L[k],"+",L[r],"+",L[a],"+",L[b],"=",n
                                 flag=True
    for i in range(l-1):
        for j in range(i+1,l):
            for k in range(j+1,l):
                for r in range(k+1):
                     for a in range(r+1,l):
                         for b in range(a+1,l):
                             for c in range(b+1,l):
                                 if L[i]+L[j]+L[k]+L[r]+L[a]+L[b]+L[c]==n:
                                     print L[i],"+",L[j],"+",L[k],"+",L[r],"+",L[a],"+",L[b],"+",L[c],"=",n
                                     flag=True                    
    if flag==False:
        print "There is no combination of elements in list that gives sum",n,"."
                

L=[1,5,3,4,2,7,6,9,8]
print L
n=input("Enter the number: ")
cumulativesum(L,n)
            
               
    
