def extract(n):
    s=0
    while n>0:
        d=n%10
        s+=d
        n//=10
    return s
n=int(raw_input("Enter No:- "))
r=extract(n)
print "The sum of digits of",n,"is",r
