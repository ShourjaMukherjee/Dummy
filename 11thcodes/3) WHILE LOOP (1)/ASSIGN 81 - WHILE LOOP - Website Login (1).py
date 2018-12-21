def validate(ID,PC,UN,PW):
    flag=True
    if UN!=ID:
        print "Incorrect Username or Password."
        print "Access Denied."
        flag=False
    else:
        if PC!=PW:
            print "Incorrect Username or Password."
            print "Access Denied."
            flag=False

    return flag

def menu():
    ID='Sam Reuel'
    PC='01543'
    flag=False
    while flag==False:
        UN=raw_input("Enter Username:- ")
        PW=raw_input("Enter Password:- ")
        flag=validate(ID,PC,UN,PW)
        print " "
    return flag

flag=menu()
if flag==True:
    print "Access Granted."
