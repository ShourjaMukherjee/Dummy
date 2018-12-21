def ispresent(n,L):                                 #Checks if an element is present in the list
    l=len(L)
    flag=False
    for i in range(l):
        if L[i]==n:
            flag=True
            break
    return flag

def mod_str(L):                                    #removes duplicates and returns a List with the Duplicates Removed
    N=[]
    N.append(L[0])
    for i in range(1,len(L)):
        flag=ispresent(L[i],N)                  #calls ispresent Function
        if flag==False:                             #if i is NOT present in List L, L[i] is appended 
            N.append(L[i])                         #to new List with removed Duplicates N
    return N

def chr_freq(S):                                 #prints Frequency of each Character
    N=mod_str(S)                                # calls mod_str Function
    for i in range(len(N)):
        count=0
        for j in range(len(S)):
            if N[i]==S[j]:
                count+=1                            #if the character occurs more than once, value of count is incremended
        print N[i],"occurs",count,"times."
        
S=str(raw_input("Enter String:- "))     #accepts String
chr_freq(S)        
