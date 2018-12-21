def acceptMat(r,c):
    M=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            M[i][j]=int(raw_input("Enter Number in position (%d,%d):-" %(i,j)))
    return M

def printMat(M,r,c):
    for i in range(r):
        for j in range(c):
            print M[i][j],
        print

def multiMatrix(M1,M2,r1,r2,c1,c2):
    N=[[0 for i in range(c2)]for i in range(r1)]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                N[i][j]+=M1[i][k]*M2[k][j]
    return N
print "Matrix 1:- "
r1=input("Enter Number of rows you wish to enter:- ")
c1=input("Enter Number of columns you wish to enter:- ")
M1=acceptMat(r1,c1)
printMat(M1,r1,c1)
print "Matrix 2:- "
r2=input("Enter Number of rows you wish to enter:- ")
c2=input("Enter Number of columns you wish to enter:- ")
M2=acceptMat(r2,c2)
printMat(M2,r2,c2)
print
N=multiMatrix(M1,M2,r1,r2,c1,c2)
print "The resultant Multiplied Matrix is:- "
printMat(N,r1,c2)
