import random 

r = random.random()

def choose(chrom): 

    print(r, chrom[5])
    
    if r >= chrom[5][0] and r <= chrom[5][1]: 

        return chrom 

