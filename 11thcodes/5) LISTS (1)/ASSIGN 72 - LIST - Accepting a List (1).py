def acceptList(L):
    choice='Y'
    while choice=='Y':
        n=input("Enter Values:- ")
        L.append(n)
        choice=raw_input("Do you wish to continue?(Y/N):- ")
    return L

L=[]
L=acceptList(L)
