def printall(s):
    l=len(s)
    n=''
    for i in range(1,l+1):
        #print s[-i]
        n+=s[-i]
    return n

n=str(raw_input("Enter Word:- "))
r=printall(n)
print r
#r=int(r)
#l=r+10
#print l
