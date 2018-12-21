def binaryfloat_to_dec(x):
    x=str(x)
    l=len(x)
    for i in range(l):
        if x[i]=='.':
            a=x[0:i]
            b=x[i+1:]
    a=int(a)
    integer=binarytodecimal(a)#Answer to integer part
    i=len(b)
    b=int(b)
    d=0
    while b>0:
        a=b%10
        d+=a*2**-i
        i-=1
        b/=10
    answer=integer+d #*10**-(i-1)
    return answer

def binarytodecimal(x):
    i=0
    d=0
    while x>0:
        a=x%10
        d+=a*2**i
        i+=1
        x/=10
    return d
n=raw_input("Enter Binary Number:- ")
ans=binaryfloat_to_dec(n)
print "The Decimal equivalent of Binary Number",n,"is:-",ans
