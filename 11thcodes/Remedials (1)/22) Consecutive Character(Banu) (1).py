def consecutiveCharacter(S):
    L = []
    S+=' '
    l=len(S)
    count=1
    g=0
    for i in range(l-1):
        if S[i]==S[i+1]:
            count+=1
        else:
            count=1
        L.append (count,i)
        if g<count:
            g=count
            n=i
    return g,n

S=str(raw_input("Enter Sentence:- "))
T=consecutiveCharacter(S)
print "The letter",S[T[1]],"occurs maximum times consecutively. No. of occurences:- ",T[0]

