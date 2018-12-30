def factor(n):
    sum=0
    for i in range(1,n/2+1):
        if n%i==0:
            sum+=i
    return sum

def check_num(val):
    x=factor(val)
    flag=False
    if x==val:
        flag=True
    return flag

num=int(raw_input("Enter Number:- "))
x=check_num(num)
if x==True:
    print num,"is a Perfect Number."
else:
    print num,"is not a Perfect Number."
    
