def  check_palindrome(s):
    l=len(s)
    flag=True
    for i in range(l/2):
        if s[i]!=s[-i-1]:
            flag=False
            break
    return flag

s=str(raw_input("Enter Word:- "))
x=check_palindrome(s)
if x==True:
    print s,"is a Palindrome."
else:
    print s,"is not a Palindrome."
