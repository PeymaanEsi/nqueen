from config import size_n
import random 
import numpy as np 
def mutation(chroms):
    for chrom in chroms: 
        for i in chrom:
            low=np.random.randint(0,size_n-1)
            up=np.random.randint(1,size_n-1)
            scramble=np.random.choice(np.arange(low,up+1))
    return scramble
            