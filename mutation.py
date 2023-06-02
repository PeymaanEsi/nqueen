from config import size_n

import random

def scramble(chroms):

    for chrom in chroms:

        low = random.randrange(8)
        up = random.randrange(8)

        if low > up:
            temp = up
            up = low
            low = temp

        print(low, up)
        sample = chroms[low: up]
        random.shuffle(sample)
        chroms[low:up] = sample

    return chroms