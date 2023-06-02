import random 

def scramble(chroms, size_n): 

    for chrom in chroms: 

        low = random.randrange(size_n) 

        up = random.randrange(size_n) 

        if low > up: 

            temp = up 

            up = low 

            low = temp 

        sample = chroms[low: up] 

        random.shuffle(sample) 

        chroms[low:up] = sample 

    return chroms