def extword(s):
    n1=0
    n2=0
    l=len(s)
    count=0
    for i in range(l):
        if s[i]==' ' or i==l-1:
            count+=1
            n2=i
            if i==l-1:
                print s[n1: ]
            else:
                print s[n1:n2]
                n1=n2+1
    print "No. of words:- ",count
r=raw_input("Enter Sentence:- ")
print "The words in sentence are:- "
extword(r)
