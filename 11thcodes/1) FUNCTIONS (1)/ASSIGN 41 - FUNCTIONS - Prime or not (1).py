def countf(n):
    count=0
    for i in range(2,n/2+1):
        if n%i==0:
            count+=1
    return count
def prime(m):
    flag=False
    x=countf(m)
    if x==0:
        flag=True
    return flag
m=int(raw_input("Enter Number:- "))
z=prime(m)
if z==True:
    print m,"is a prime number."
else:
    print m,"is not a prime number."
