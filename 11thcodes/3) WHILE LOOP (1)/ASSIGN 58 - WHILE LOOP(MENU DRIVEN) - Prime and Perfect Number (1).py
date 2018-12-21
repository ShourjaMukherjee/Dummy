def isprime(n):
    flag=True
    for i in range(1,n/2+1):
        if n%i==0:
            flag=False
            break
    return flag

def factor(n):
    sum=0
    for i in range(1,n/2+1):
        if n%i==0:
            sum+=i
    return sum

def check_num(val):
    x=factor(val)
    flag=False
    if x==val:
        flag=True
    return flag
def menu():
    choice='Y'
    while choice=='Y':
        print "Choose Course of Action:-"
        print "1) Check if Prime"
        print "2) Check if Perfect Number"
        n=int(raw_input("Enter Choice:- "))
        x=int(raw_input("Enter Number:- "))
        if n==1:
            m=isprime(x)
            if m==False:
                print x,"is a Prime Numnber."
            else:
                print x,"is not a Prime Number."
        elif n==2:
            m=check_num(x)
            if m==True:
                print x,"is a Perfect Number."
            else:
                print x,"is not a Perfect Number."
        else:
            print "Invalid Choice has been entered."
        choice='K'
        while choice!='Y' and choice!='N':
            choice=str(raw_input("Do you wish to continue?(Y/N)"))
            if choice!='Y' and choice!='N':
                print "Invalid Choice."

menu()
