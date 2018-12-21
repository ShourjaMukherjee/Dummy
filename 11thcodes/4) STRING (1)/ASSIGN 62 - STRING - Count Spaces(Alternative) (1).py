def count_space(s):
    count=0
    for i in s:
        if i==' ':
            count+=1
    print "No. of spaces in the sentence are:- ",count

s=str(raw_input("Enter Sentence:- "))
count_space(s)
        
