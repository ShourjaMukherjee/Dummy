def isprime(n):                                             #Checks if Number is Prime
    flag=True
    for i in range(2,n/2+1):
        if n%i==0:
            flag=False
            break
    return flag

def cons_comp(n):                                       # returns a list with the length of longest chain and 
    N=[]                                                       # starting and final index of the longest chains 
    for i in range(2,n+2):
        flag=isprime(i)                                    # Calls isprime function to form a List of all Prime numbers
        if flag==True:
            N.append(i)
    l=len(N)
    g=0
    Q=[]
    for i in range(0,l-1):                              #in this loop, the difference of consecutive prime numbers in the 
        d=N[i+1]-N[i]                                   #list is compared and the highest difference gives (length of chain+1)
        if g<d:
            g=d            
            Q=[g]                                       #length of chain is appended to empty list
        if g==d:
                Q.append(N[i])                      #the prime numbers on both ends of composite chain is appended to list
                Q.append(N[i+1])
    return Q            

n=int(raw_input("Enter the Limit of the Search:- "))     #accepts Limit
T=cons_comp(n)
if len(T)==3:
    print "The Longest Chain of Composite Numbers is:-"
elif len(T)>3:
    r=(len(T)-1)/2
    print "There are",r,"Chains of Composite Numbers that tie for the Longest Chain."
    print "They are:-"
for i in range(1,len(T)-1,2):                     #this loop will print the chain or chains depending on length of
    for j in range(T[i]+1,T[i+1]):               #returned List   
        print j
    print
        
