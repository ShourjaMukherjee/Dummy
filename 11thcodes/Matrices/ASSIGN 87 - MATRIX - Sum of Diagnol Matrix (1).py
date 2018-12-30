def acceptMat(r,c):
    M=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            M[i][j]=int(raw_input("Enter Number in position (%d,%d):-" %(i,j)))
    return M

def sumLeadDiag(M,m):
    sum=0
    for i in range(m):
        sum+=M[i][i]
    return sum

def sumSecondDiag(M,m):
    sum=0
    for i in range(m):
        sum+=M[i][m-i-1]
    return sum

def printMat(M,r,c):
    print "Matrix:- "
    for i in range(r):
        for j in range(c):
            print M[i][j],
        print


m=input("Enter Number of rows/column you wish to enter:- ")
M=acceptMat(m,m)
printMat(M,m,m)
N=sumLeadDiag(M,m)
R=sumSecondDiag(M,m)
print "Sum of Leading Diagnol is:- ",N
print "Sum of Secondary Diagnol is:- ",R
