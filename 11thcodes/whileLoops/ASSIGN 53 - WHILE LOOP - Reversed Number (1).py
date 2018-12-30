def rev(n):
    a=0
    while n>0:
        d=n%10
        a=a*10+d
        n//=10
    return a

n=int(raw_input("Enter Number:- "))
x=rev(n)
print x,"is the Reversed Number of",n
