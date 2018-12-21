def check_anagram(S1,S2):
    s1=len(S1)
    s2=len(S2)
    count=0
    for i in range(s1):
        for j in range(s2):
            if S1[i]==S2[j]:
                print S1[i],"is present in both."
                count+=1
    if s1!=s2:
        print S1,"and",S2,"are not anagrams."
    else:
        if count==s1:
            print S1,"and",S2,"are anagrams."
        else:
            print S1,"and",S2,"are not anagrams."

S1=raw_input("Enter First String:- ")
S2=raw_input("Enter Second String:- ")
check_anagram(S1,S2)
            
