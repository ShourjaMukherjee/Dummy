def towers_of_Hanoi(s,i,t,n):
    if n==1:
        print "Moving Disk",n,"from tower",s,"to",t
    if n>1:
        towers_of_Hanoi(s,t,i,n-1)
        movedisk(s,t,n)
        towers_of_Hanoi(i,s,t,n-1)

def movedisk(s,t,n):
    print "Moving Disk",n,"From tower",s,"to",t

n=3
towers_of_Hanoi("Source","Intermediate","Target",n)
