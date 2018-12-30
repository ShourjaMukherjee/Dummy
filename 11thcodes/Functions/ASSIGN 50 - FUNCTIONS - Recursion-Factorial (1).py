def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(raw_input("Enter No.:- "))
result=fact(num)
print "Factorial of",num,"is",result
