def expo(n,b):
    p=1
    for i in range(1,n+1):
        p*=b
    return p

def digit_sum(n):
    sum=0
    while n>0:
        d=n%10
        c=expo(3,d)
        sum+=c
        n//=10
    return sum
def check_num(n):
    a=digit_sum(n)
    flag=False
    if a==n:
        flag=True
    return flag

num=int(raw_input("Enter Number:- "))
x=check_num(num)
if x==True:
    print num,"is an Armtrong Number."
else:
    print num,"is not an Armtrong Number."
