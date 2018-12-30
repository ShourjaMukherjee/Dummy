def printpattern(c,n):    #      Displays character 'c' n times
    for i in range(n):
        print c,



def pattern(c,n):       #        Displays upper half of required patter
    max=2*n-1
    r=len(c)            #       Calculates length of character to be displayed 
    sch=' '
    for i in range(1,n+1):
        num=2*i-1       #        Calculates no. of times c should be diplayed
        space=max-num
        h_space=space/2  #       Calculates no. of leading and trailing spaces
        printpattern(r*sch,h_space)
        printpattern(c,num)
        printpattern(sch,h_space)
        print
        

def revpattern(c,n):   #         Displays lower half of required pattern
    max=2*n-1
    r=len(c)
    sch=' '            #       Calculates length of character to be displayed
    for i in range(n-1,-1,-1):
        num=2*i-1         #        Calculates no. of times c should be diplayed
        space=max-num
        h_space=space/2    #        Calculates no. of times c should be diplayed
        printpattern(r*sch,h_space)
        printpattern(c,num)
        printpattern(sch,h_space)
        print
        
print "Welcome to Pattern Printer! :D"
print "Choose Pattern Formation:- "
print "1. Pyramidal"
print "2. Upside down Pyramidal"
print "3. Diamond (LEVELS WILL BE TWICE THAT ENTERED)"
r=input("Enter Choice(1/2/3):- ")
print 
n=int(raw_input("Enter No. of Levels:- "))
c=raw_input("Enter Character used in Pattern:-  ")
if r==1:
    pattern(c,n)
elif r==2:
    revpattern(c,n)
elif r==3:
    pattern(c,n)
    revpattern(c,n)
else:
    print "Invalid Choice."
