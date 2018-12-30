def fibonacci(n):
    L=[0 for i in range(n)]    
    if n>2:
        for i in range(2,n):
            L[1]=1
            L[i]=L[i-1]+L[i-2]
    elif n==2:
        L[1]=1
    elif n<0:
        print "Invalid Limit."
    for i in range(n):
        print L[i]

n=input("Enter Limit of Fibonacci Series:- ")
print "Fibonacci Series till",n,"terms:- "
fibonacci(n)
