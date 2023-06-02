import random
from config import size_n

def crossover(chroms):
    mask = [random.randrange(2) for i in range(8)]
    print(mask)
    newchroms = []
    for i in range(0, len(chroms), 2):
        child1 = [0 for i in range(8)]
        child2 = [0 for i in range(8)]
        for j in range(0,size_n):
            if mask[j]==1: 
                child1[j] = chroms[i][j]
                child2[j] = chroms[i + 1][j]
            elif mask[j]==0: 
                child1[j] = chroms[i + 1][j]
                child2[j] = chroms[i][j]
        newchroms.append(child1)
        newchroms.append(child2)
    return newchroms