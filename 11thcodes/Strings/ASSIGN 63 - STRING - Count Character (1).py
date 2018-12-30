def findchar(s,ch):
    count=0
    l=len(s)
    for i in range(l):
        if s[i]==ch:
            count+=1
    print "No. of times",ch,"is used in the sentence is:-",count

s=str(raw_input("Enter Sentence:-"))
ch=str(raw_input("Enter the character to be counted:- "))
findchar(s,ch)
