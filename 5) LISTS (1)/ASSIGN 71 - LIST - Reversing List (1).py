def revlist(l):
    l=list(l)
    L=len(l)
    r=[]
    r.extend(l)
    for i in range(L):
        r[i]=l[-i-1]
    return r

a=raw_input("Enter String:- ")
c=revlist(a)
print "Reverse of",a,"is:- "
print c
