
def expn(a,b):
    p=1.0
    for i in range(1,b+1):
        p*=a
    return p

def fact(m):
    q=1.0
    for i in range(1,m+1):
        q*=i
    return q

def sinn(x,y):
    s=0
    for i in range(1,y+1):
        N=expn(x,2*(i-1)+1)
        D=fact(2*(i-1)+1)
        Sn=expn(-1,i-1)
        t=Sn*N/D
        s+=t
    return s
c=int(raw_input("Enter value of Angle:- "))
d=int(raw_input("Enter value of Accuracy:- "))
j=c*3.14/180
r=sinn(j,d)
print "The Value of sin",c,"for",d,"terms in Maclaurin's Series is",r

