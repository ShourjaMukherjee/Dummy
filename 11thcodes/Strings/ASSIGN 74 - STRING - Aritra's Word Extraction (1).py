def extractwords(s):
    i=0
    n1=0
    n2=0
    l=len(s)
    count=0
    while i<l:
        if s[i]==' ' or i==l-1:
            n2=i
            if i==l-1:
                if s[i]!=' ':
                    if count==0:
                        print "The Words Are:- "
                    print s[n1: ]
                count+=1
            elif s[n1]!=' ':
                if count==0:
                    print "The Words are:-"
                print s[n1:n2]
                count+=1
            if s[i]==' ':
                j=n2+1
                while s[j]==' ':
                    j+=1
                    if j==l:
                        break
                n1=j
                i=j

        i+=1
    return count

n=raw_input("Enter String:- ")
t=extractwords(n)
print "Number of Words are:-",t

                        
