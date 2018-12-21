def reg_odr(s):
    l=len(s)
    print "Regular Order:- "
    for i in range(0,l,2):
        print s[i],

def rev_odr(s):
    l=len(s)
    print "Reverse Order:- "
    for i in range(l-1,-1,-2):
        print s[i],

def menu():
    print "Choose Course of Action:- "
    print "1> Regular Order"
    print "2> Reverse Order"
    n=int(raw_input("Enter Choice:- "))
    r=raw_input("Enter Word:- ")
    if n==1:
        reg_odr(r)
    elif n==2:
        rev_odr(r)
    else:
        print "Invalid Choice."

menu()
        
