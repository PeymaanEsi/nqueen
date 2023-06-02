import random
from config import size_n

def crossover(chroms):
    mask = [random.randrange(2) for i in range(8)]
    print(mask)
    newchroms = []
    if mask==1: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i].append(chroms[i])
                newchroms[i+1].append(chroms[i+1])
    elif mask==0: 
        for i in range(0,chroms,2):
            for j in range(0,size_n):
                newchroms[i].append(chroms[i+1])
                newchroms[i+1].apppend(chroms[i])
                
    # /   ///////
    
    # /   ////////
    return newchroms