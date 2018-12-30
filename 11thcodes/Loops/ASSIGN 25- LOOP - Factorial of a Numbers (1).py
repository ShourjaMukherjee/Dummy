n=raw_input("Enter Value of 'n:- ")
n=int(n)
prod=1
for i in range(1,n+1):
    prod*=i
print "The factorial of Natural Number",n,"is",prod
