
def vowelconsec(s):
    l=len(s)
    k='AaEeIiOoUu'
    d='aeiou'
    v=''
    c=""
    for i in range(l-1):
        for j in range(0,len(k),2):
            if k[j] not in c:
                if s[i]==k[j] or s[i]==k[j+1]:
                    if s[i+1]==k[j] or s[i+1]==k[j+1]:
                        v+=k[j+1]
                        c=k[j]
                        break
    print v
    return v
x=raw_input("Enter the string:- ")
k=vowelconsec(x)
print "The consecutive vowels are:  ",
for i in range(len(k)):
    print k[i],
    
