def extractwords(s):
    i=0
    flag=False
    n1=0
    n2=0
    l=len(s)
    count=0
    while i<l:
        if s[i]==' ' or i==l-1:
            flag=True
            count+=1
            n2=i
            if i==l-1:
                print s[n1: ]
            else:
                print s[n1:n2]
            j=n2+1
            while s[j]==' ':
                j+=1
            n1=j
            if flag==True:
                i=j
                flag=False
            else:
                i+=1
    print "No. of words are:- ", count

r=raw_input("Enter Sentence:- ")
print "The words in sentence are:- "
extractwords(r)

            
