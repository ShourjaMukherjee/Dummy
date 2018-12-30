print "PLEASE TURN  ON CAPS!!!!!!"
def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=input("Enter Value:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
        if choice!='Y':
            break
    return L
def LinearSearch(K,L):
    flag=False
    l=len(L)
    count=0
    
    for i in range(l):
        if K==L[i]:
            flag=True
            count+=1
            print "Key is found at Index",i
    if flag==False:
        print "Key is not found."
    print "Key occurs",count,"times."

L=[]
L=acceptList(L)
key=input("Enter Key:- ")
LinearSearch(key,L)
