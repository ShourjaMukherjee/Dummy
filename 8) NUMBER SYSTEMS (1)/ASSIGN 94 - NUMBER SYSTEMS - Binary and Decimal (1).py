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

def DecimalToBinary(n):
    t=0
    i=0
    while n>0:
        d=n%2
        t+=d*10**i
        i+=1
        n/=2
    return t

print "Welcome to Number System Converter :) "
print "1. Convert Binary to Decimal"
print "2. Convert Decimal to Binary"
c=int(raw_input("Enter Choice(1/2):- "))
if c==1:
    m=int(raw_input("Enter Binary Number:- "))
    t=BinaryToDecimal(m)
    print "The Decimal equivalent of Binary Number",m,"is:- ",t
elif c==2:
    m=int(raw_input("Enter Decimal Number:- "))
    t=DecimalToBinary(m)
    print "The Binary equivalent of Decimal Number",m,"is:- ",t
else:
    print "Invalid Choice"
        
