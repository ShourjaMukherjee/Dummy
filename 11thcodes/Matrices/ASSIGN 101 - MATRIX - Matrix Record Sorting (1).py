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
        
def swap(L,i,j):
    t=L[i]
    L[i]=L[j]
    L[j]=t

def MatrixRecordSorting(M):
    l=len(M)
    for i in range(l-2,-1,-1):
        for j in range(i+1):
            if M[j][2]>M[j+1][2]:
                swap(M,j,j+1)
    return M

r=input("Enter Number of rows you wish to enter:- ")
c=input("Enter Number of columns you wish to enter:- ")
M=acceptMat(r,c)
R=MatrixRecordSorting(M)
printMat(R,r,c)
