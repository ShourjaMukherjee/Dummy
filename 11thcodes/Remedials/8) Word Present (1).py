def matchwords(S1,S2):
    s1=len(S1)
    s2=len(S2)
    L=countspace(S1)
    R=lengthofword(S1)
    #print "L=",L
    #print "R=",R
    l=len(L)
    count=0
    for i in range(l+1):
        if R[i]!=s2:            
            continue
        elif R[i]==s2:
            if i==0:
                spc1=-1
            elif i>0:
                spc1=L[i-1]
            #print "i=",i
            #print "Spc1=",spc1
            flag=True
            for j in range(s2):
                #print S2[j]," ",S1[j+spc1+1]
                if S2[j]!=S1[j+spc1+1]:
                    flag=False
                    #print flag
                    break
            if flag==True:
                count+=1
            #print
    return count
    
def countspace(S1):
    s=len(S1)
    count=0
    space=[]
    for i in range(s):
        if S1[i]==' ':
            count+=1
            space.append(i)
    #print count
    return space

def lengthofword(S1):
    S1=S1+" "
    l=len(S1)
    count=0
    L=[]
    for i in range(l):
        count+=1
        if S1[i]==" ":
            L.append(count-1)
            i+=1
            count=0
        else:
            continue
    return L
        
#def checkLength(S1,S2):
    #L=lengthofword(S1)
    #r=len(L)
    #l=len(S2)
    #flag=False
    #for i in range(r):
        #if L[i]==l:
            #flag=True
            #break
        #else:
            #continue
    #return flag



S1=raw_input("Enter String with no Extending spaces:- ")
S2=raw_input("Enter Key Word with no Extending spaces:- ")
count=matchwords(S1,S2)
if count==0:
    print "'",S2,"' is not present in '",S1,"'"
else:
    print "'",S2,"' is present in '",S1,"'",count,"number of time(s)"

