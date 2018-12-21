def acceptMat(r,c):
    M=[[0 for i in range(c)]for i in range(r)]
    for i in range(r):
        for j in range(c):
            M[i][j]=input("Enter the number at(%d,%d):- "%(i,j))
    return M

def printMat(M,r,c):
    for i in range(r):
        for j in range(c):
            print M[i][j]," ",
        print

def traverseOutline(M,m,n,r,c):
    i=r
    j=c
    ri=r
    ci=c
    rf=m-1-ri
    cf=n-1-ci
    for j in range(ci,cf+1):
        print M[i][j],
    for i in range(ri+1,rf+1):
        print M[i][j],
    for j in range(cf-1,ci-1,-1):
        print M[i][j],
    for i in range(rf-1,ri,-1):
        print M[i][j],
   

def spiralPrint(M,m,n):
    p=smaller(m,n)
    if p%2!=0:
        p+=1
    i=0
    j=0
    for fat in range(p/2):
        traverseOutline(M,m,n,i,j)
        i+=1
        j+=1

def smaller(m,n):
    result=m if m<n else n
    return result
r=input("Enter Number of Rows:- ")
c=input("Enter Number of Columns:- ")
M=acceptMat(r,c)
printMat(M,r,c)
spiralPrint(M,r,c)
