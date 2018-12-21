print "PLEASE TURN  ON CAPS!!!!!!"
def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=raw_input("Enter Value:- ")
        n=float(n)
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
        
    return L

def sum(s):
    l=len(s)
    N=[]
    sum=0
    for i in range(l):
        sum+=s[i]
        N.append(sum)
    return N

L=[]
L=acceptList(L)
print "Orginal List:- ",L
sum=sum(L)
print "List with Cummalative sum:- ",sum
