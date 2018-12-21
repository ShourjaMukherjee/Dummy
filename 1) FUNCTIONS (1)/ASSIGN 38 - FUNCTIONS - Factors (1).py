def fac(x,y):
    flag=False
    if x%y==0:
        flag=True
    return flag
num1=int(raw_input("Enter Value of Number:- "))
num2=int(raw_input("Enter Value of Probable Factor:- "))
fat=fac(num1,num2)
if fat==True:
    print num2,"is a factor of",num1
else:
    print num2,"is not a factor of",num1
