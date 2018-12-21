def sqrt(n):
    if n==0 or n==1:
        s=n
    else:
        s=n+1
        for i in range(2,n/2+1):
            if i*i==n:
                s=i
                break
    return s
num=int(raw_input("Enter No:- "))
if num<0:
    print "Invalid Entry."
else:
    result=sqrt(num)
    print "The Square root of ",num,"is",result
