print "PLEASE TURN  ON CAPS!!!!!!"
def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=raw_input("Enter Value:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
        
    return L

def check_identical(L1,L2):
    l=len(L1)
    flag=True
    for i in range(l):
        if L1[i]!=L2[i]:
            flag=False
            break
    return flag

n=[]
r=[]
print "List 1:- "
n=acceptList(n)
print "List 2:- "
r=acceptList(r)
if len(n)!=len(r):
    print "The Lists",n,"and",r,"are not identical."
else:
    state=check_identical(n,r)
    if state==True:
        print "The Lists",n,"and",r,"are identical."
    else:
        print "The Lists",n,"and",r,"are not identical."
