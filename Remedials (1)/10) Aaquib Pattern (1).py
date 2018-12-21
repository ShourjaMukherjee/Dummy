def pattern(n):                                     #Defining a function to 
                                                    #display the required pattern
    for i in range(1,2*n,2):
        for j in range(2*(n-1),i,-2):               #range for spaces
            print " ",
        for k in range(1,i+1):                      #range for stars
            print "*",
        print
    for a in range(2*n-2,-1,-2):
        for b in range(2*(n-1),a-1,-2):             #range for spaces
            print " ",                              
        for c in range(2,a+1):                      #range for stars
            print "*",
        print
        
z=int(raw_input("Enter the no. of terms "))
pattern(z)
