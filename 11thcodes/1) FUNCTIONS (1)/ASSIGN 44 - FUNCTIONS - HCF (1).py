def smaller(a,b):
    if a<b:
        s=a
    elif a>b:
        s=b
    else:
        s=a
    return s
def HCF(m,n):
    p=smaller(m,n)
    for i in range(p,0,-1):
        if m%i==0 and n%i==0:
            q=i
            break
    return q

x=int(raw_input("Enter First No:- "))
y=int(raw_input("Enter Second No:- "))
z=HCF(x,y)
print "HCF of",x,"and",y,"is",z
