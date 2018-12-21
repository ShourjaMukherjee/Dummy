def firstoccurance(s1,s2):
    k=[]
    L=[]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                if s1[i] not in s1[:i]:
                    k.append(i)
    if k==L:
        k.append(-1)
                    
    s=k[0]
    for i in range(1,len(k)):
        if k[i]<s:
            s=k[i]

    return s

def lower_case(s):
    L=[]
    for i in range(len(s)):
        L.append(s[i])
        if ord(s[i])>=65 and ord(s[i])<=90:
            L[i]=chr(ord(s[i])+32)
    return L
        
s1=raw_input("Enter the first string: ")
s2=raw_input("Enter the second string: ")
s1=lower_case(s1)
s2=lower_case(s2)

k=firstoccurance(s1,s2)

if k>=0:
    print "The occurance of the first character is: ",k
elif k==-1:
    print "There is no common letter"

