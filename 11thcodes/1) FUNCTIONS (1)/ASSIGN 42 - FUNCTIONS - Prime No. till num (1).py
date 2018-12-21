def countf(n):
    count=0
    for i in range(2,n/2+1):
        if n%i==0:
            count+=1
    return count
def prime(m):
    flag=False
    x=countf(m)
    if x==0:
        flag=True
    return flag
def listprime(n):
    for i in range(2,n+1):
        state=prime(i)
        if state==True:
            print i
num=int(raw_input("Enter Number:- "))
print "Prime number till",num,"are:-"
listprime(num)
