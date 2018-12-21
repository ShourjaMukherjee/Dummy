def check(S):          # checks no. of words that start with CAP letters
    l=len(S)
    L=[0]
    for i in range(l):     # forms a list with index of first letter of every word
        if S[i]==' ' and ord(S[i+1])>=65 and ord(S[i+1])<=122:
            if ord(S[i+1])<91 or ord(S[i+1])>96:
                L.append(i+1)
    count=0
    for i in range(len(L)):     # checks if first letter of each word is Capitalized 
        for j in range(65,91):
            if S[L[i]]==chr(j):
                count+=1
                
    return count

S=raw_input("Enter String:- ")
r=check(S)
if r==0:
    print "No words start with a Capitalized Letter."
else:
    print "Number of words that start with Capitalized Letter:- ",r
