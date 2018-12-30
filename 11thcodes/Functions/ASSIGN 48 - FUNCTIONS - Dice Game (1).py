import random
def game(n):
    for i in range(1,n+1):
        result=random.randint(1,6)
        print "The NO. on dice is",result

r=int(raw_input("Enter No. of Rolls:- "))
game(r)
