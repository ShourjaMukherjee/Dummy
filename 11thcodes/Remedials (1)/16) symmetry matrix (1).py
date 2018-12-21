def matrix_symmetry(M,r):              #To check if the matrix is symmetrical around the leading diagonal
    flag=True
    for i in range(r):
        for j in range(r):
            if i<j:
                if M[i][j]!=M[j][i]:    #Checking for mismatch
                    flag=False
                    break
        if flag==False:
            break
    return flag

def accept_mat(M,r,c):                   #To accept the matrix
    for i in range(r):
        for j in range(c):
            M[i][j]=input("Enter the value in %d%d:  "%(i,j))
    return M

def print_matrix(M,r,c):               #To print the matrix
    for i in range(r):
        for j in range(c):
            print M[i][j],
        print 

print "The matrix entered should be a square matrix"

r=input("Enter the no. of rows:  ")
M=[[0 for i in range(r)]for j in range(r)]
M=accept_mat(M,r,r)

k=matrix_symmetry(M,r)

print_matrix(M,r,r)

if k==True:
    print "The matrix is symmetrical"
else:
    print "The matrix is asymmetrical"
    
