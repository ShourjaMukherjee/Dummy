
def exp(m,n):
    m1=1
    flag=True
    if n<0:
        n=-n
        flag=False
    for i in range(1,n+1):
        m1*=m
    if flag==False:
        m1=1.0/m1
    return m1
x=int(raw_input("Enter Base Number:- "))
y=int(raw_input("Enter Exponant:- "))
t=exp(x,y)
print "The Result of",x,"^",y,"is",t
