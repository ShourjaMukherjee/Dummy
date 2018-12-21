def listsum(L):           
    l=len(L)
    sum=0
    for i in range(l):
        sum+=L[i]
    return sum

def combinations (L,C,start,stop,index,r,num):      
    if index==r:
        if listsum(C)==num:
            print C
    else:
        i=start
        while i<=stop and stop-i+1>=r-index:
            C[index] = L[i]
            combinations (L, C, i+1, stop, index+1, r,num)
            i+=1 

def generateCombinations (L, n, r,num):
    l=len (L)
    C=[0 for i in range (r)]
    combinations(L,C,0,l-1,0,r,num) 

L=[1,2,3,4,5]
l=len (L)
num=6
for i in range (1, l):
    generateCombinations(L,l,i,num) 

