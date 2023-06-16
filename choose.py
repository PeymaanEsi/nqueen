import random 

r = random.random()

def choose(chrom): 

    print(r, chrom[6])
    
    if r >= chrom[6][0] and r <= chrom[6][1]: 

        return chrom 

