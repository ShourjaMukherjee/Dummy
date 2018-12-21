
def combinations ( L, C, start, stop, index, r):
    if index == r:
        print C
    else:
        i = start
        while i<=stop and stop-i+1>=r-index:
            C[index] = L[i]
            combinations (L, C, i+1, stop, index+1, r)
            i+=1 

def generateCombinations (L, n, r):

    l = len (L)
    C = [0 for i in range (r)]

    combinations (L, C, 0, l-1, 0, r) 

L = [1,2,3,4,5]
l = len (L)

for i in range (1, l):
    generateCombinations (L, l, i) 
