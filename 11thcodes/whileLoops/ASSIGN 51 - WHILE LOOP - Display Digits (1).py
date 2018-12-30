def extract(n):
    print "The digits of",n,"are:-"
    while n>0:
        d=n%10
        print d
        n//=10
n=int(raw_input("Enter No:- "))
r=extract(n)

