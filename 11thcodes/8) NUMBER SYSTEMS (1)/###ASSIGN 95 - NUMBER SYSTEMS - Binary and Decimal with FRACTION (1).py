def BinaryToDecimal(n):
    s=0
    f=0
    while n>0:
        d=n%10
        t=d*2**f
        s+=t
        f+=1
        n/=10
    return s

def fracbin_dec(s):
    t2=0
    t=0
    for i in range(len(s)):
        if s[i]=='.':
            t=i
            break
    s1=int(s[ :t])
    f=len(s[t+1: ])
    s2=int(s[t+1: ])
    t1=BinaryToDecimal(s1)
    while s2>0:
        d=s2%10
        t2=d*(1.0/2**f)
        f-=1
        s2/=10
    ans=t1+t2
    return ans

n=raw_input("Enter Binary Number:- ")
ans=fracbin_dec(n)
print "The Decimal equivalent of Binary Number",n,"is:-",ans










    
