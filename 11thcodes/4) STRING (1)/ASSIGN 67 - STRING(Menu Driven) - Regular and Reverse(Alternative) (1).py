def reg_odr(s):
    print s[0: :2]

def rev_odr(s):
    print s[-1: :-2]

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
