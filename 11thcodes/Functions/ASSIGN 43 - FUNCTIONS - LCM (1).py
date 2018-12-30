def larger(a,b):
    if a<b:
        s=b
    elif a>b:
        s=a
    else:
        s=a
    return s
def LCM(a,b):
    p=larger(a,b)
    q=a*b
    for i in range(p,q+1):
        if i%a==0 and i%b==0:
            m=i
            break
    return m

x=int(raw_input("Enter First No:- "))
y=int(raw_input("Enter Second No:- "))
z=LCM(x,y)
print "LCM of",x,"and",y,"is",z
