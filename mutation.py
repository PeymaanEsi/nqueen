   if mask==1: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i]=chroms[i], newchroms[i+1]=chroms[i+1]
    elif mask==0: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i]=chroms[i+1],newchroms[i+1]=chroms[i]
                
    # /   ///////