from random import shuffle

size_n = 8

def generate(chrom):
    l = []
    for i in range(chrom):
        l.append(list(range(size_n)))
        shuffle(l[i])
    return l

print(generate(100))