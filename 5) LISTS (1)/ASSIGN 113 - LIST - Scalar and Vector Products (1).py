def accept_Vector():
    i=float(raw_input("Enter value in i direction:- "))
    j=float(raw_input("Enter value in j direction:- "))
    k=float(raw_input("Enter value in k direction:- "))
    L=[i,j,k]
    return L

def rollup(L):
    t=L[0]
    for i in range(1,len(L)):
        L[i-1]=L[i]
    L[len(L)-1]=t
    return L

def vector_prod(L1,L2):
    rollup(L1)
    rollup(L2)
    L1.append(L1[0])
    L2.append(L2[0])
    sum=0
    Result=[]
    for i in range(3):
        a=L1[i]*L2[i+1]-L2[i]*L1[i+1]
        Result.append(a)
    return Result


print "First Vector:- "
L1=accept_Vector()
print
print "Second Vector:- "
L2=accept_Vector()
v=vector_prod(L1,L2)
print "Vector Product:- ",v
