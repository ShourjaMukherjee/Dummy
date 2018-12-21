def saddlepoint(M,r,c):  #To find the saddle point in a matrix
    count=0
    for i in range(r):

        l=M[i][0]
        for j in range(1,c):
            if M[i][j]>l:
                l=M[i][j]
                w=j
                
        s=M[0][w]
        for j in range(1,r):
            if M[j][w]<s:
                s=M[j][w]
        if l==s:
            count+=1
            print "The saddlepoint is",s
            break
    return count

def accept_mat(M,r,c):    #To accept the list
    for i in range(r):
        for j in range(c):
            M[i][j]=input("Enter the value in %d %d "%(i,j))
    return M

r=input("Enter the no. of rows ")
c=input("Enter the no. of columns ")
M=[[0 for i in range(c)]for j in range(r)]
M=accept_mat(M,r,c)

result=saddlepoint(M,r,c)
if result>=1:
    print "The no. of saddlepoints : ",result
else:
    print "There is no saddle point"
                
