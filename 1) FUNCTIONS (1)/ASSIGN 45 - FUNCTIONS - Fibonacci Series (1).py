def fib(n):
    x=0
    y=1
    if n==1:
        print x
    elif n==2:
        print x
        print y
    elif n<=0:
        print "Invalid Limit"
    else:
        print "Fibonacci Series till",n,"terms is:- "
        print x
        print y
        for i in range(1,n-1):
            z=x+y
            print z
            x=y
            y=z


n=int(raw_input("Enter Limit for Fibonacci Series:- "))
fib(n)
