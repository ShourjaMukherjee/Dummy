def acceptMat(r,c):
    M=[[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            M[i][j]=int(raw_input("Enter Number in position (%d,%d):-" %(i,j)))
    return M

def printMat(M,r,c):
    for i in range(r):
        for j in range(c):
            print M[i][j],"   ",
        print


r=input("Enter Number of rows you wish to enter:- ")
c=input("Enter Number of columns you wish to enter:- ")
M=acceptMat(r,c)
printMat(M,r,c)
