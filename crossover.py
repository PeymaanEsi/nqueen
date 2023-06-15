import random

def crossover(parent1, parent2, size_n): 

    mask = [random.randrange(2) for i in range(size_n)] 

    print(mask) 

    print() 

    child1 = [0 for i in range(size_n)] 

    child2 = [0 for i in range(size_n)] 

    for i in range(0,size_n): 

        if mask[i]==1: 

            child1[i] = parent1[i]

            child2[i] = parent2[i] 

        elif mask[i]==0: 

            child1[i] = parent2[i] 

            child2[i] = parent1[i] 
        
    return [child1, child2] 

