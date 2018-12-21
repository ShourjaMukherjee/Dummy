def str_stat(s):
    l=len(s)
    count_alpha=0
    count_space=0
    count_Cvowel=0
    count_vowels=0
    count_consonant=0
    count_digit=0
    count_other=0
    for i in range(l):
        if s[i].isspace()==True:
            count_space+=1
        elif s[i].isdigit()==True:
            count_digit+=1
        elif s[i].isalpha()==True:
            count_alpha+=1
        if s[i]=='a' or s[i]=='A' or s[i]=='e' or s[i]=='E' or s[i]=='i' or s[i]=='I' or s[i]=='o' or s[i]=='O' or s[i]=='u' or s[i]=='U':
            count_vowels+=1
    count_consonant=count_alpha-count_vowels
    count_other=l-(count_alpha+count_space)
    print s
    print "No. of Spaces:- ", count_space
    print "No. of Vowels:- ", count_vowels
    print "No. of Consonants:- ", count_consonant
    print "No. of Digits:- ", count_digit            
    print "No. of Other Characters:- ", count_other

s=raw_input("Enter Statement:- ")
str_stat(s)
    
