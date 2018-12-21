def evenodd(n):
    flag=False
    if n%2==0:
        flag=True
    return flag
num=int(raw_input("Enter Number:- "))
state=evenodd(num)
if state==True:
    print num,"is even."
else:
    print num,"is odd."
