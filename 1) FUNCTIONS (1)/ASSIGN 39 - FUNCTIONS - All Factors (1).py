def fac(n):
    for i in range(1,n+1):
       if n%i==0:
           print i
m=int(raw_input("Enter Number:- "))
print "Factors of",m,"are:-"
fac(m)
    
