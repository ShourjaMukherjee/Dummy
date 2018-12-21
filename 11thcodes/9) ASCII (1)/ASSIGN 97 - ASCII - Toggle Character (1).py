def toggleCharacter(S):              # checks no. of words that start with CAP letters
    l=len(S)
    L=[]
    R=list(S)
    for i in range(len(R)):     # checks if first letter of each word is Capitalized 
        for j in range(65,91):
            if S[i]==chr(j):
                R[i]=chr(j+32)
    for i in range(len(R)):      
        for j in range(97,123):
            if S[i]==chr(j):
                R[i]=chr(j-32)
    M=""
    for i in range(len(R)):
        M+=R[i]
    return M
S=raw_input("Enter Sentence:- ")
R=toggleCharacter(S)
print R


