def asterix(n):
    for i in range(1,n+1):
        for r in range(1,i+1):
            print '*',
        print
n=int(raw_input("Enter Limit:- "))
r=asterix(n)
