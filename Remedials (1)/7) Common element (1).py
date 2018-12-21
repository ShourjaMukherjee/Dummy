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

def MatrixtoList(M,r,c):
    L=[0 for i in range(c*r)]
    k=0
    for i in range(r):
        for j in range(c):
            L[k]=M[i][j]
            k+=1
    print L

r=input("Enter Number of Rows:- ")
c=input("Enter Number of Columns:- ")
M=acceptMat(r,c)
printMat(M,r,c)
MatrixtoList(M,r,c)
