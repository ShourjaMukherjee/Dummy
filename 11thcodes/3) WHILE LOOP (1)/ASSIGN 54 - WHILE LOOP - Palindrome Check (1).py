def rev(n):
    a=0
    while n>0:
        d=n%10
        a=a*10+d
        n//=10
    return a

def palindrome(val):
    b=rev(val)
    flag=True
    if val==b:
        flag=False
    return flag

num=int(raw_input("Enter Number:- "))
x=palindrome(num)
if x==False:
    print num,"is a Palindrome."
else:
    print num,"is not a Palindrome."

    
