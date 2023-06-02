import random

def crossover(chroms):
    mask = [random.randrange(2) for i in range(8)]
    print(mask)
    newchroms = []
       if mask==1: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i]=chroms[i], newchroms[i+1]=chroms[i+1]
        elif mask==0: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i]=chroms[i+1],newchroms[i+1]=chroms[i]
                
    # /   ///////
    
    # /   ////////
    return newchroms