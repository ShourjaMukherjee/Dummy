def larger(a,b):
    if a>b:
        t=a
    else:
        t=b
    return t
x=raw_input("Enter First Number:- ")
y=raw_input("Enter Second Number:- ")
x=int(x)
y=int(y)
z=larger(x,y)
print "The larger of the two numbers",x,"and",y,"is",z
