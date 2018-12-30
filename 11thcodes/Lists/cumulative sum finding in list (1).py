def cum():
    x=[]
    L=[1,2,3,4,5,6,7,8,9]
    lala=11
    l=len(L)
    flag=True
    for i in range(l-1,-1,-1):
        for j in range(i,-l,-1):
            for k in range(j,-1,-1):
                if L[i]+L[j]+L[k]==lala:
                    if L[i]!=L[k] and L[j]!=L[k] and L[i]!=L[j]:
                        print L[i],"+",L[j],'+',L[k]
                        break
            if L[i]+L[j]==lala:
                 if L[i]!=L[j]:
                      print L[i],'+',L[j]
                      
            if flag==False:
                break
                    
            
    
cum()
