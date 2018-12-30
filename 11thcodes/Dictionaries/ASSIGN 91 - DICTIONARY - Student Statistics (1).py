def detaillist():
    L=[]
    a=input('Enter roll number:')
    b=raw_input('Enter Name:')
    c=input('Marks in Mathematics:- ')
    d=input('Marks in English:- ')
    e=input('Marks in Physics:- ')
    f=input('Marks in Chemistry:- ')
    g=input('Marks in Optional:- ')

    h=c+d+e+f+g

    i=h/5
    L.append(b)
    L.append(c)
    L.append(d)
    L.append(e)
    L.append(f)
    L.append(g)
    L.append(h)
    L.append(i)
    return L
def acceptdictionary():
    D={}
    n=input('Enter the number of elements:')
    for i in range(1,n+1):
        a=i
        D[i]=detaillist()
    return D

def printDictionary(D):
    print "ROLL NO. \t NAME|MATH|ENG|PHY|CHEM|OPT|TOTAL|AVG"
    for a in D:
        print a," \t\t ",D[a][0],D[a][1],D[a][2],D[a][3],D[a][4],D[a][5],D[a][6],D[a][7]

D=acceptdictionary()
printDictionary(D)
