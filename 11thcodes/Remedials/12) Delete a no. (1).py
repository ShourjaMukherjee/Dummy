def delete_pos(L,pos):            #To delete a no. in a particular poition
    x=L[pos]
    l=len(L)
    for i in range(pos,l-1):
        L[i]=L[i+1]
    k=[]
    for i in range(len(L)-1):
        k.append(L[i])
    print "The new list is",k
    return x

def accept_list(L):
    choice="y"
    while choice=="y":
        n=input("Enter the value")
        L.append(n)
        choice=raw_input("Enter y or n")
    return L

L=[1,2,3,4,5]
#L=accept_list(L)
pos=input("Enter the position to be deleted")

k=delete_pos(L,pos)
print "The no. deleted is",k
