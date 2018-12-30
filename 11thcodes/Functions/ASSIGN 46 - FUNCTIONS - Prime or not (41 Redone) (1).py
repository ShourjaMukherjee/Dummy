def isprime(n):
    flag=True
    for i in range(2,n/2+1):
        if n%i==0:
            flag=False
            break
    return flag

n=int(raw_input("Enter The Number:- "))
r=isprime(n)
if r==True:
    print n,"is Prime"
else:
    print n,"is Composite"
