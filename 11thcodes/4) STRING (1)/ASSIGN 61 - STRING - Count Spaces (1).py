def count_space(s):
    count=0
    l=len(s)
    for i in range(l):
        if s[i]==' ':
            count+=1
    print "No. of spaces in the sentence are:- ",count

s=str(raw_input("Enter Sentence:- "))
count_space(s)
        
