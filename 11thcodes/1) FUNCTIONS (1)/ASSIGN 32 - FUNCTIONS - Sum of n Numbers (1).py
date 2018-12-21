def sum(n):
    s=0
    for i in range(1,n+1):
        s+=i
    return s
n=int(raw_input("Enter Value of n:- "))
a=sum(n)
print "The sum of first",n,"Natural Numbers is",a
