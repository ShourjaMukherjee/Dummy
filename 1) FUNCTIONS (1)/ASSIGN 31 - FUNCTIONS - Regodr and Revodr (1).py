
def regodr(n):
    print "The First",n,"Natural Numbers are:-"
    for i in range(1,n+1):
        print i
def revodr(n):
    print "The First",n,"Natural Numbers in reverse order are:-"
    for i in range(n,0,-1):
        print i
num=(int(raw_input("Enter a Natural Number:-")))
print "Choice 1: Regular Order"
print "Choice 2: Reverse Order"
choice=(int(raw_input("Enter Choice Number:-")))
if choice ==1:
    regodr(num)
elif choice==2:
    revodr(num)
else:
    print "Incorrect Entry"
