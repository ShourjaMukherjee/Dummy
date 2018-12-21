def multitable(a,b):
    prod=1
    for i in range(1,b+1):
        prod=a*i
        print a,"*",b,"=",prod
m=int(raw_input("Enter Multiplicant:- "))
n=int(raw_input("Enter Limit:- "))
multitable(m,n)
