def FirstAndLast(S1,S2):            # displays the first and last occurances
    s1=len(S1)                      # of key S2 in string S1   
    flag=True
    state=True
    for i in range(s1):             # checks for the first Occurance
        if S1[i]==S2:
            f=i
            flag=True
            break
        else:
            flag=False
        
    for i in range(s1-1,-1,-1):     # checks for the last occurance
        if S1[i]==S2:
            l=i
            state=True
            break
        else:
            state=False
    if flag==True and state==True:  # if S2 occurs in S1, the foll. is carried out
        T=(f,l)
        if f==l:
            print "The First and Last Occurances are the same. Index of singular occurance is:- ",f
        else:
            print "The First and Last Occurances are:- ",T
    elif flag==False and state==False:     # if S2 does not occur in S1
            print "The Key",S2,"does not occur in string:- ",S1
S1=raw_input("Enter The String:- ")
S2=raw_input("Enter The Key:- ")
FirstAndLast(S1,S2)

