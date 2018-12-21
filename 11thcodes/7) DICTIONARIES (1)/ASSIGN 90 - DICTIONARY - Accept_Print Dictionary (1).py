def acceptDictionary():
    D={}
    n=input("Enter Number of Items:- ")
    for i in range(1,n+1):
        a=input("Enter Key:- ")
        D[a]=input("Enter Value:- ")
    print D
    return D

def printDictionary(D):
    print "KEY \t\t VALUE"
    for a in D:
        print a,"\t\t",D[a]

D=acceptDictionary()
printDictionary(D)
    
        
