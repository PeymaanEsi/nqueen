from config import size_n
from random import shuffle

def generate(chroms):
    l = []
    for i in range(chroms):
        l.append(list(range(size_n)))
        shuffle(l[i])
    return l

