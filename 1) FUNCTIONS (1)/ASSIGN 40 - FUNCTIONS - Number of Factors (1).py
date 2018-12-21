def f(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    return count
m=int(raw_input("Enter Number:- "))
z=f(m)
print m,"has",z,"factors excluding 1 and",m
